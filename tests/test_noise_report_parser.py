"""Tests para el parser de informes de ruido de AENA."""

from pathlib import Path

import pytest

from src.noise_report_parser import (
    MONTH_TO_NUM,
    _extract_date_range,
    _iter_months,
    _normalize_text,
    _parse_monthly_from_text,
    _parse_summary_line,
    _parse_value_flags,
    parse_annual_summary,
    parse_monthly_report,
    parse_tmr_monthly,
)

REPORTS_DIR = Path(__file__).resolve().parent.parent / "doc" / "aena" / "informes_anuales_ruido"


# ---- Helpers unitarios -----------------------------------------------------


class TestParseValueFlags:
    def test_plain_value(self):
        s = ["55,1", "siguiente"]
        val, flags = _parse_value_flags(s)
        assert val == 55.1
        assert flags == ""
        assert s == ["siguiente"]

    def test_value_with_trailing_flag_separate_token(self):
        s = ["50,2", "*¹", "48,2"]
        val, flags = _parse_value_flags(s)
        assert val == 50.2
        assert flags == "*¹"
        assert s == ["48,2"]

    def test_value_with_prefix_flag(self):
        s = ["*40,5", "resto"]
        val, flags = _parse_value_flags(s)
        assert val == 40.5
        assert flags == "*"

    def test_value_with_trailing_flag_attached(self):
        s = ["44,4¹"]
        val, flags = _parse_value_flags(s)
        assert val == 44.4
        assert flags == "¹"

    def test_nd(self):
        s = ["ND", "siguiente"]
        val, flags = _parse_value_flags(s)
        assert val is None
        assert flags == ""
        assert s == ["siguiente"]


class TestNormalizeText:
    def test_joins_broken_month_names(self):
        text = "ene\nfeb\nm ar\nabr\nno v\ndic"
        out = _normalize_text(text)
        assert "mar" in out
        assert "nov" in out

    def test_joins_nd(self):
        text = "valor: N D final"
        out = _normalize_text(text)
        assert "ND" in out


class TestParseSummaryLine:
    def test_simple_tmr(self):
        line = "TMR 16 58,0 40,5 51,3 35,9 49,2 17,9"
        parsed = _parse_summary_line(line)
        assert parsed is not None
        assert parsed["tmr_id"] == 16
        assert parsed["location_index"] is None
        assert parsed["tmr_flag"] == ""
        vals = parsed["values"]
        assert vals[0] == (58.0, "")
        assert vals[5] == (17.9, "")

    def test_tmr_with_global_flag(self):
        line = "TMR 61* 54,7 44,8 49,8 42,4 44,8 32,2"
        parsed = _parse_summary_line(line)
        assert parsed["tmr_id"] == 61
        assert parsed["tmr_flag"] == "*"

    def test_tmr_with_inline_flags(self):
        line = "TMR 16 55,4 40,0 *¹ 52,0 33,4 49,9 16,3"
        parsed = _parse_summary_line(line)
        assert parsed is not None
        vals = parsed["values"]
        assert vals[0] == (55.4, "")
        assert vals[1] == (40.0, "*¹")

    def test_tmr_with_location_superscript(self):
        line = "TMR 163 54,8 *¹ 38,6 *¹ 51,4 *¹ 33,2 *¹ 50,1 *¹ 19,7 *¹"
        parsed = _parse_summary_line(line)
        assert parsed["tmr_id"] == 16
        assert parsed["location_index"] == 3

    def test_non_tmr_line(self):
        assert _parse_summary_line("Esto no es una fila") is None

    def test_header_line(self):
        assert _parse_summary_line("Indicadores anuales - 2022") is None


class TestParseMonthlyFromText:
    def test_interlaced_format(self):
        text = "\n".join([
            "ene", "53,2", "49,2",
            "ene", "48,6", "46,5",
            "ene", "43,6", "17,8",
            "feb", "55,9", "51,4",
            "feb", "50,5", "49,1",
            "feb", "39,8", "22,5",
        ])
        result = _parse_monthly_from_text(text)
        assert result["day"][1] == (53.2, "", 49.2, "")
        assert result["evening"][1] == (48.6, "", 46.5, "")
        assert result["night"][1] == (43.6, "", 17.8, "")
        assert result["day"][2] == (55.9, "", 51.4, "")

    def test_nd_handling(self):
        text = "sep\nND\nND\nsep\nND\nND\nsep\nND\nND"
        result = _parse_monthly_from_text(text)
        assert result["day"][9] == (None, "", None, "")
        assert result["night"][9] == (None, "", None, "")

    def test_flags_inline(self):
        text = "ago\n50,2 *¹\n48,2 *¹"
        result = _parse_monthly_from_text(text)
        assert result["day"][8] == (50.2, "*¹", 48.2, "*¹")


# ---- Tests de integración con PDFs reales ---------------------------------

pytestmark_real_pdfs = pytest.mark.skipif(
    not REPORTS_DIR.exists(),
    reason="PDFs de informes anuales no disponibles en el repo",
)


@pytestmark_real_pdfs
class TestParseAnnualSummaryReal:
    def test_2025_tmr16_matches_aena_letter(self):
        """Los valores del TMR-16 en 2025 deben coincidir con la carta de AENA
        (expediente 2026/MA000106): 55,1 / 50,4 / 49,9 / 47,2 / 43,6 / 25,0."""
        rows = parse_annual_summary(REPORTS_DIR / "2025_informe_anual.pdf", 2025)
        tmr16 = next(r for r in rows if r.tmr_id == 16 and r.location_index is None)
        assert tmr16.laeq_total_day == 55.1
        assert tmr16.laeq_avion_day == 50.4
        assert tmr16.laeq_total_evening == 49.9
        assert tmr16.laeq_avion_evening == 47.2
        assert tmr16.laeq_total_night == 43.6
        assert tmr16.laeq_avion_night == 25.0

    def test_2023_has_two_tmr16_locations(self):
        """En 2023 el TMR-16 se movió a mitad de año: deben aparecer ubicaciones 3 y 4."""
        rows = parse_annual_summary(REPORTS_DIR / "2023_informe_anual.pdf", 2023)
        tmr16_rows = [r for r in rows if r.tmr_id == 16]
        indexes = sorted(r.location_index for r in tmr16_rows if r.location_index)
        assert indexes == [3, 4]

    def test_2022_has_tmr61(self):
        """TMR-61 apareció a partir de 2022, siempre con bandera '*' (sin ENAC)."""
        rows = parse_annual_summary(REPORTS_DIR / "2022_informe_anual.pdf", 2022)
        tmr61 = next(r for r in rows if r.tmr_id == 61)
        assert tmr61.tmr_flag == "*"


@pytestmark_real_pdfs
class TestParseTMRMonthlyReal:
    def test_2025_tmr16_returns_36_rows(self):
        rep = parse_tmr_monthly(REPORTS_DIR / "2025_informe_anual.pdf", 16, 2025)
        assert rep is not None
        assert len(rep.monthly) == 36  # 12 meses × 3 periodos

    def test_2025_tmr16_september_october_are_nd(self):
        """En 2025 el TMR-16 estuvo fuera de servicio sep-oct (incendio)."""
        rep = parse_tmr_monthly(REPORTS_DIR / "2025_informe_anual.pdf", 16, 2025)
        for month in (9, 10):
            for period in ("day", "evening", "night"):
                row = next(r for r in rep.monthly if r.month == month and r.period == period)
                assert row.laeq_total is None
                assert row.laeq_avion is None

    def test_2025_tmr16_location_name(self):
        rep = parse_tmr_monthly(REPORTS_DIR / "2025_informe_anual.pdf", 16, 2025)
        assert "Tres Cantos" in rep.location_name
        assert "King" in rep.location_name


class TestDateRange:
    def test_extract_date_range(self):
        start, end = _extract_date_range("Junio 2024 – Junio 2025")
        assert start == (2024, 6)
        assert end == (2025, 6)

    def test_extract_date_range_ascii_dash(self):
        start, end = _extract_date_range("Enero 2024 - Diciembre 2025")
        assert start == (2024, 1)
        assert end == (2025, 12)

    def test_no_date_range(self):
        start, end = _extract_date_range("sin fechas aquí")
        assert start is None and end is None


class TestIterMonths:
    def test_spans_year_boundary(self):
        months = list(_iter_months((2024, 11), (2025, 2)))
        assert months == [(2024, 11), (2024, 12), (2025, 1), (2025, 2)]

    def test_single_month(self):
        assert list(_iter_months((2025, 5), (2025, 5))) == [(2025, 5)]


MONTHLY_REPORTS_DIR = Path(__file__).resolve().parent.parent / "doc" / "aena" / "informes_mensuales_ruido"


@pytest.mark.skipif(
    not MONTHLY_REPORTS_DIR.exists(),
    reason="PDFs de informes mensuales no disponibles",
)
class TestParseMonthlyReportReal:
    def test_2025_06_returns_13_months_per_period(self):
        """Informe mensual jun-2025 cubre jun-2024 a jun-2025 = 13 meses."""
        rep = parse_monthly_report(
            MONTHLY_REPORTS_DIR / "2025" / "2025-06_informe_ruido.pdf", 16
        )
        assert rep is not None
        assert len(rep.monthly) == 13 * 3
        years = {r.year for r in rep.monthly}
        assert years == {2024, 2025}

    def test_2025_06_matches_annual(self):
        """Los valores de 2025-01 a 2025-06 en el informe jun-2025 deben coincidir
        con los del informe anual 2025."""
        rep_m = parse_monthly_report(
            MONTHLY_REPORTS_DIR / "2025" / "2025-06_informe_ruido.pdf", 16
        )
        rep_a = parse_tmr_monthly(REPORTS_DIR / "2025_informe_anual.pdf", 16, 2025)
        # Mapa (month, period) -> (total, avion) en ambos
        m_map = {(r.month, r.period): (r.laeq_total, r.laeq_avion)
                 for r in rep_m.monthly if r.year == 2025}
        a_map = {(r.month, r.period): (r.laeq_total, r.laeq_avion)
                 for r in rep_a.monthly if r.month <= 6}
        for key in a_map:
            assert m_map[key] == a_map[key], f"mismatch at {key}"
