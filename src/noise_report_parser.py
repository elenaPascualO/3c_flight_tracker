"""Parseo de informes anuales de ruido de AENA (Envirosuite / Brüel & Kjær).

Extrae de los PDFs:
- Tabla resumen anual por TMR (LAeq Total / Avión × día / tarde / noche).
- Valores mensuales del TMR indicado (normalmente TMR-16 Tres Cantos, TMR-61 Tres Cantos Norte).

Formatos soportados: 2019-2025. Años 2016-2018 tienen los datos en imágenes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pdfplumber

MONTHS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MONTH_TO_NUM = {name: i + 1 for i, name in enumerate(MONTHS)}

# Para parsear títulos como "Junio 2024 – Diciembre 2025".
MONTH_LONG_TO_NUM = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
}

PERIODS = ["day", "evening", "night"]


@dataclass
class AnnualRow:
    year: int
    tmr_id: int
    location_index: int | None  # superíndice indicando sub-ubicación si el TMR tuvo varias en el año
    tmr_flag: str  # "*" si el TMR en conjunto está marcado (p.ej. TMR 61 sin ENAC)
    laeq_total_day: float | None
    flags_total_day: str
    laeq_avion_day: float | None
    flags_avion_day: str
    laeq_total_evening: float | None
    flags_total_evening: str
    laeq_avion_evening: float | None
    flags_avion_evening: str
    laeq_total_night: float | None
    flags_total_night: str
    laeq_avion_night: float | None
    flags_avion_night: str


@dataclass
class MonthlyRow:
    year: int
    month: int  # 1..12
    tmr_id: int
    period: str  # "day" | "evening" | "night"
    laeq_total: float | None  # None si ND
    flags_total: str
    laeq_avion: float | None  # None si ND
    flags_avion: str


@dataclass
class TMRReport:
    tmr_id: int
    tmr_flag: str  # "*" si el encabezado del TMR está marcado
    location_name: str  # p.ej. "Tres Cantos-King's College"
    year: int
    monthly: list[MonthlyRow] = field(default_factory=list)
    availability_note: str = ""  # nota de disponibilidad <70%, incendios, cambios de ubicación, etc.


# Helpers ---------------------------------------------------------------------

_FLAG_CHARS = "*¹²³"


def _normalize_text(text: str) -> str:
    """Junta letras sueltas separadas por espacios (artefactos de pdfplumber).

    Ejemplos: "m ar" -> "mar", "no v" -> "nov", "N D" -> "ND".
    """
    # Meses: construimos una regex que acepta espacios opcionales entre letras.
    for month in MONTHS:
        pattern = r"\b" + r"\s*".join(month) + r"\b"
        text = re.sub(pattern, month, text, flags=re.IGNORECASE)
    # ND (no data)
    text = re.sub(r"\bN\s*D\b", "ND", text)
    return text


def _parse_value_flags(token_stream: list[str]) -> tuple[float | None, str]:
    """Dado un stream de tokens empezando por un valor numérico, devuelve (valor, flags).

    Consume del stream los tokens que formen parte del valor. Ejemplo:
    - ["50,2", "*¹"]      -> (50.2, "*¹"),  consume 2 tokens
    - ["*40,5"]           -> (40.5, "*"),   consume 1
    - ["40,0", "*¹", ...] -> (40.0, "*¹"),  consume 2
    - ["ND"]              -> (None, ""),    consume 1
    """
    if not token_stream:
        return None, ""
    tok = token_stream.pop(0)
    if tok.upper() == "ND":
        return None, ""
    # Prefix flag: "*40,5" o "*¹40,5"
    m = re.match(rf"^([{re.escape(_FLAG_CHARS)}]+)?(\d+[,.]\d+)([{re.escape(_FLAG_CHARS)}]+)?$", tok)
    if not m:
        return None, ""
    pre, val, post = m.group(1) or "", m.group(2), m.group(3) or ""
    # Siguiente token podría ser flag separado: ["50,2", "*¹"]
    if token_stream and re.fullmatch(rf"[{re.escape(_FLAG_CHARS)}]+", token_stream[0]):
        post += token_stream.pop(0)
    return float(val.replace(",", ".")), pre + post


# --- Resumen anual -----------------------------------------------------------

def _find_annual_summary_page(pdf: pdfplumber.PDF) -> int | None:
    for i, p in enumerate(pdf.pages):
        txt = p.extract_text() or ""
        if "Resumen de niveles" in txt and "anuales" in txt and "TMR" in txt:
            return i
    return None


def _parse_summary_line(line: str) -> dict | None:
    """Parsea una fila tipo 'TMR 16 58,0 *40,5 51,3 35,9 49,2 17,9' o
    'TMR 61 * 54,7 44,8 49,8 42,4 44,8 32,2'.

    También maneja filas con superíndice de sub-ubicación, que pdfplumber aplasta a dígito normal:
    'TMR 163' (= TMR 16³), 'TMR 164' (= TMR 16⁴).
    """
    m = re.match(r"^\s*TMR\s*(\d+)\s*([*]?)\s+(.*)$", line)
    if not m:
        return None
    raw_id = int(m.group(1))
    tmr_flag = m.group(2)
    # Heurística: los TMR reales de SIRMA no superan 2 dígitos. Si el id tiene 3+ dígitos,
    # el último es un superíndice de sub-ubicación aplanado por pdfplumber.
    if raw_id >= 100:
        tmr_id = raw_id // 10
        location_index: int | None = raw_id % 10
    else:
        tmr_id = raw_id
        location_index = None
    rest = m.group(3).strip()
    tokens = rest.split()
    values: list[tuple[float | None, str]] = []
    while tokens and len(values) < 6:
        val, flags = _parse_value_flags(tokens)
        values.append((val, flags))
    if len(values) != 6 or all(v[0] is None for v in values):
        return None
    return {
        "tmr_id": tmr_id,
        "location_index": location_index,
        "tmr_flag": tmr_flag,
        "values": values,
    }


def parse_annual_summary(pdf_path: str | Path, year: int) -> list[AnnualRow]:
    """Extrae la tabla resumen anual (LAeq por TMR y periodo) de un informe anual."""
    rows: list[AnnualRow] = []
    with pdfplumber.open(pdf_path) as pdf:
        idx = _find_annual_summary_page(pdf)
        if idx is None:
            return rows
        text = _normalize_text(pdf.pages[idx].extract_text() or "")
        for raw_line in text.splitlines():
            parsed = _parse_summary_line(raw_line)
            if not parsed:
                continue
            v = parsed["values"]
            rows.append(
                AnnualRow(
                    year=year,
                    tmr_id=parsed["tmr_id"],
                    location_index=parsed["location_index"],
                    tmr_flag=parsed["tmr_flag"],
                    laeq_total_day=v[0][0], flags_total_day=v[0][1],
                    laeq_avion_day=v[1][0], flags_avion_day=v[1][1],
                    laeq_total_evening=v[2][0], flags_total_evening=v[2][1],
                    laeq_avion_evening=v[3][0], flags_avion_evening=v[3][1],
                    laeq_total_night=v[4][0], flags_total_night=v[4][1],
                    laeq_avion_night=v[5][0], flags_avion_night=v[5][1],
                )
            )
    return rows


# --- Valores mensuales por TMR ----------------------------------------------

def _find_tmr_monthly_pages(pdf: pdfplumber.PDF, tmr_id: int) -> list[int]:
    """Páginas con datos mensuales del TMR (detectadas por densidad numérica y presencia de meses)."""
    pat = re.compile(rf"TMR\s*{tmr_id}\b")
    hits = []
    for i, p in enumerate(pdf.pages):
        txt = _normalize_text(p.extract_text() or "")
        if not pat.search(txt):
            continue
        if "Resumen" in txt:
            continue
        n_dec = len(re.findall(r"\d+,\d+", txt))
        months_hit = sum(1 for m in MONTHS if m in txt.lower())
        if n_dec >= 30 and months_hit >= 6:
            hits.append(i)
    return hits


def _parse_monthly_from_text(text: str) -> dict[str, dict[int, tuple[float | None, str, float | None, str]]]:
    """Parsea los valores mensuales desde un texto de informe Envirosuite.

    El formato es: cada mes aparece 3 veces consecutivas (día, tarde, noche).
    Ejemplo: ``ene 53,2 49,2 ene 48,6 46,5 ene 43,6 17,8 feb ...``
    Devuelve ``{"day": {1: (total, f_total, avion, f_avion), ...}, "evening": {...}, "night": {...}}``.
    """
    tokens: list[str] = []
    for ln in text.splitlines():
        ln = ln.strip()
        if ln:
            tokens.extend(ln.split())
    result: dict[str, dict[int, tuple]] = {p: {} for p in PERIODS}
    month_counts: dict[int, int] = {}  # nº de veces visto cada mes
    i = 0
    while i < len(tokens):
        tok = tokens[i].lower()
        if tok in MONTH_TO_NUM:
            month = MONTH_TO_NUM[tok]
            count = month_counts.get(month, 0)
            if count >= 3:
                i += 1
                continue
            # Consumir mes + 2 valores del flujo
            sub = tokens[i + 1:]
            total_val, total_flags = _parse_value_flags(sub)
            avion_val, avion_flags = _parse_value_flags(sub)
            consumed = len(tokens) - 1 - len(sub) - i
            period = PERIODS[count]
            result[period][month] = (total_val, total_flags, avion_val, avion_flags)
            month_counts[month] = count + 1
            i += 1 + consumed
        else:
            i += 1
    return result


def _extract_date_range(text: str) -> tuple[tuple[int, int] | None, tuple[int, int] | None]:
    """Extrae rango de fechas de un título tipo 'Junio 2024 – Junio 2025'.

    Devuelve ((start_year, start_month), (end_year, end_month)) o (None, None).
    """
    # Normalizar guión largo –/— a guión normal para la regex
    t = text.replace("–", "-").replace("—", "-").lower()
    pattern = re.compile(
        r"(" + "|".join(MONTH_LONG_TO_NUM.keys()) + r")\s+(\d{4})\s*-\s*(" + "|".join(MONTH_LONG_TO_NUM.keys()) + r")\s+(\d{4})",
        re.IGNORECASE,
    )
    m = pattern.search(t)
    if not m:
        return None, None
    return (
        (int(m.group(2)), MONTH_LONG_TO_NUM[m.group(1).lower()]),
        (int(m.group(4)), MONTH_LONG_TO_NUM[m.group(3).lower()]),
    )


def _iter_months(start: tuple[int, int], end: tuple[int, int]):
    """Itera (year, month) desde start hasta end inclusive."""
    y, m = start
    ey, em = end
    while (y, m) <= (ey, em):
        yield (y, m)
        m += 1
        if m > 12:
            m = 1
            y += 1


def parse_monthly_report(pdf_path: str | Path, tmr_id: int) -> TMRReport | None:
    """Parsea un informe MENSUAL Envirosuite (2024-2025).

    Cada informe mensual tiene ventana móvil de 13 meses (el mes actual + 12 anteriores).
    Para cada mes del rango, el texto presenta 3 tripletas consecutivas (día, tarde, noche):
    ``jun 52,4 50,1 jun 49,1 46,8 jun 42,5 23,3 jul ...``

    Devuelve un TMRReport con hasta 13×3 filas mensuales.
    """
    with pdfplumber.open(pdf_path) as pdf:
        # Buscar páginas del TMR
        pages = _find_tmr_monthly_pages(pdf, tmr_id)
        if not pages:
            return None
        best_idx = pages[0]
        for idx in pages:
            txt = _normalize_text(pdf.pages[idx].extract_text() or "")
            if re.search(rf"TMR\s*{tmr_id}\s*[:]", txt):
                best_idx = idx
                break
        text = _normalize_text(pdf.pages[best_idx].extract_text() or "")
        # Encabezado y rango de fechas
        header_match = re.search(rf"TMR\s*{tmr_id}\s*[:]\s*([^\n]+)", text)
        location = ""
        tmr_flag = ""
        if header_match:
            location = header_match.group(1).strip()
            if location.endswith("*"):
                tmr_flag = "*"
                location = location.rstrip("*").strip()
        date_start, date_end = _extract_date_range(text)
        if not date_start or not date_end:
            return None
        expected_months = list(_iter_months(date_start, date_end))
        # Tokenizar el texto y consumir tripletas por orden cronológico
        tokens: list[str] = []
        # Aislar solo la sección después del encabezado para evitar ruido de leyendas
        # El primer mes corto del rango marca el inicio de la serie
        first_short = MONTHS[date_start[1] - 1]
        lower = text.lower()
        offset = lower.find(first_short)
        if offset < 0:
            return None
        body = text[offset:]
        for ln in body.splitlines():
            ln = ln.strip()
            if ln:
                tokens.extend(ln.split())
        monthly: list[MonthlyRow] = []
        idx_tok = 0
        for (yr, mn) in expected_months:
            expected_name = MONTHS[mn - 1]
            for period in PERIODS:
                # Buscar el siguiente token que sea el mes esperado
                while idx_tok < len(tokens) and tokens[idx_tok].lower() != expected_name:
                    idx_tok += 1
                if idx_tok >= len(tokens):
                    break
                # Consumir mes + 2 valores
                idx_tok += 1
                sub = tokens[idx_tok:]
                total_val, total_flags = _parse_value_flags(sub)
                avion_val, avion_flags = _parse_value_flags(sub)
                consumed = len(tokens) - idx_tok - len(sub)
                idx_tok += consumed
                monthly.append(
                    MonthlyRow(
                        year=yr, month=mn, tmr_id=tmr_id, period=period,
                        laeq_total=total_val, flags_total=total_flags,
                        laeq_avion=avion_val, flags_avion=avion_flags,
                    )
                )
        return TMRReport(
            tmr_id=tmr_id,
            tmr_flag=tmr_flag,
            location_name=location,
            year=date_end[0],  # año del informe
            monthly=monthly,
            availability_note="",
        )


def parse_tmr_monthly(pdf_path: str | Path, tmr_id: int, year: int) -> TMRReport | None:
    """Extrae datos mensuales del TMR indicado de un informe anual."""
    with pdfplumber.open(pdf_path) as pdf:
        pages = _find_tmr_monthly_pages(pdf, tmr_id)
        if not pages:
            return None
        # En algunos años hay más de una página (p.ej. primera es texto introductorio).
        # Tomamos la primera que contiene el patrón "TMR <id>:" (encabezado Envirosuite).
        best_idx = None
        for idx in pages:
            txt = _normalize_text(pdf.pages[idx].extract_text() or "")
            if re.search(rf"TMR\s*{tmr_id}\s*[:\-]", txt) or re.search(rf"TMR\s*{tmr_id}\*?\s*\n", txt):
                best_idx = idx
                break
        if best_idx is None:
            best_idx = pages[0]
        text = _normalize_text(pdf.pages[best_idx].extract_text() or "")
        # Encabezado: "TMR 16: Tres Cantos-King's College" o "TMR 61: Tres Cantos Norte*".
        # Exigimos ':' para no capturar párrafos narrativos que mencionan el TMR.
        header_match = re.search(rf"TMR\s*{tmr_id}\s*[:]\s*([^\n]+)", text)
        tmr_flag = ""
        location = ""
        if header_match:
            location = header_match.group(1).strip()
            # El asterisco final indica sin-ENAC.
            if location.endswith("*"):
                tmr_flag = "*"
                location = location.rstrip("*").strip()
        # Nota de disponibilidad (línea que incluye "disponibilidad" o "incendio" o "cambio de ubicación")
        availability_note = ""
        for line in text.splitlines():
            low = line.lower()
            if any(k in low for k in ("disponibilidad", "incendio", "cambio de ubicación", "retirada", "retirado")):
                availability_note += line.strip() + " | "
        availability_note = availability_note.rstrip(" |")

        blocks = _parse_monthly_from_text(text)
        monthly: list[MonthlyRow] = []
        for period in PERIODS:
            for month, (total, tflag, avion, aflag) in sorted(blocks.get(period, {}).items()):
                monthly.append(
                    MonthlyRow(
                        year=year, month=month, tmr_id=tmr_id, period=period,
                        laeq_total=total, flags_total=tflag,
                        laeq_avion=avion, flags_avion=aflag,
                    )
                )
        return TMRReport(
            tmr_id=tmr_id,
            tmr_flag=tmr_flag,
            location_name=location,
            year=year,
            monthly=monthly,
            availability_note=availability_note,
        )
