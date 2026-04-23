"""Tests de la capa de visualización (Plotly)."""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import pytest

from src.database import init_db, insert_noise_annual, insert_noise_monthly
from src.noise_report_parser import AnnualRow, MonthlyRow
from src.noise_viz import (
    build_tmr_timeseries,
    plot_tmr_comparison,
    plot_tmr_period,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
REAL_DB = REPO_ROOT / "data" / "flights.db"


@pytest.fixture
def populated_db(tmp_db) -> str:
    """DB temporal con datos sintéticos mínimos (TMR-16 anual + mensual)."""
    annual_rows = [
        AnnualRow(
            year=y, tmr_id=16, location_index=None, tmr_flag="",
            laeq_total_day=55.0, flags_total_day="",
            laeq_avion_day=50.0, flags_avion_day="",
            laeq_total_evening=50.0, flags_total_evening="",
            laeq_avion_evening=45.0, flags_avion_evening="",
            laeq_total_night=44.0, flags_total_night="",
            laeq_avion_night=20.0, flags_avion_night="",
        )
        for y in range(2019, 2023)
    ]
    insert_noise_annual(annual_rows, source_file="test.pdf", db_path=tmp_db)
    monthly_rows = [
        MonthlyRow(
            year=y, month=m, tmr_id=16, period=p,
            laeq_total=55.0, flags_total="",
            laeq_avion=50.0, flags_avion="",
        )
        for y in (2024, 2025) for m in range(1, 13) for p in ("day", "evening", "night")
    ]
    insert_noise_monthly(monthly_rows, source_file="test.pdf", db_path=tmp_db)
    return tmp_db


class TestBuildTMRTimeseries:
    def test_combines_annual_and_monthly(self, populated_db):
        df = build_tmr_timeseries(16, "day", "total", db_path=populated_db)
        # 4 anuales (2019-2022) + 24 mensuales (2024-2025) = 28
        assert len(df) == 28

    def test_annual_years_covered_by_monthly_are_excluded(self, populated_db):
        """Las filas anuales de años con datos mensuales no deben aparecer duplicadas."""
        df = build_tmr_timeseries(16, "day", "total", db_path=populated_db)
        assert (df["source"] == "anual").sum() == 4
        assert (df["source"] == "mensual").sum() == 24

    def test_sorted_by_date(self, populated_db):
        df = build_tmr_timeseries(16, "night", "avion", db_path=populated_db)
        assert df["date"].is_monotonic_increasing


class TestPlotFunctions:
    def test_plot_tmr_period_returns_figure(self, populated_db):
        fig = plot_tmr_period(16, "night", db_path=populated_db)
        assert isinstance(fig, go.Figure)
        assert len(fig.data) == 2  # Total + Avión

    def test_plot_tmr_period_all_periods(self, populated_db):
        for period in ("day", "evening", "night"):
            fig = plot_tmr_period(16, period, db_path=populated_db)
            assert isinstance(fig, go.Figure)

    def test_plot_tmr_comparison(self, populated_db):
        fig = plot_tmr_comparison([16], "night", "avion", db_path=populated_db)
        assert isinstance(fig, go.Figure)
        assert len(fig.data) == 1


@pytest.mark.skipif(
    not REAL_DB.exists(),
    reason="Necesita la DB ya populada por noise_extract",
)
class TestWithRealData:
    def test_builds_combined_series_for_tmr16(self):
        df = build_tmr_timeseries(16, "night", "total", db_path=str(REAL_DB))
        assert len(df) > 0
        # Debe haber filas anuales (pre-2023) y mensuales (2023+)
        assert (df["source"] == "anual").sum() > 0
        assert (df["source"] == "mensual").sum() > 0

    def test_plot_renders_real_data(self):
        fig = plot_tmr_period(16, "night", db_path=str(REAL_DB))
        assert isinstance(fig, go.Figure)

    def test_comparison_tmr16_tmr61(self):
        fig = plot_tmr_comparison([16, 61], "night", "total", db_path=str(REAL_DB))
        assert isinstance(fig, go.Figure)
        assert len(fig.data) == 2
