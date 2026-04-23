"""OCR de valores LAeq del TMR16 en informes mensuales 2017-2023.

Los informes tienen una serie rolling de 13 meses con gráficos de barras y tablas
de valores bajo cada gráfico. pdfplumber/PyMuPDF no extraen esos valores (están
embebidos como imagen), así que usamos tesseract.

Clave del enfoque: **redundancia**. Cada mes aparece en hasta 13 informes distintos
(el rolling de 13 meses). Extraemos los 13 valores de cada fila de cada informe y
luego agregamos por (año, mes, periodo, métrica) usando la mediana de todas las
lecturas. Esto neutraliza errores puntuales de OCR.

Salidas:
 - data/tmr16_raw_readings.csv: una fila por (informe, posicion, periodo, métrica).
 - data/tmr16_aggregated.csv:   una fila por (año, mes, periodo, métrica) con mediana,
                                nº de lecturas, dispersión y flag de sospecha.
"""
from __future__ import annotations

import csv
import io
import re
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image

BASE = Path("doc/aena/informes_mensuales_ruido")
OUT_RAW = Path("data/tmr16_raw_readings.csv")
OUT_AGG = Path("data/tmr16_aggregated.csv")
OUT_VALID = Path("data/tmr16_validation.md")

TMR16_MARKERS = [
    re.compile(r"TMR[\s\-_]*16[\*¹²³⁴]*\s*[:.]?\s*Tres\s*Cantos", re.IGNORECASE),
    re.compile(r"TMR[\s\-_]*16[³⁴]", re.IGNORECASE),
]
MONTH_LABELS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
PERIODS = ["day", "evening", "night"]
METRICS = ["total", "avion"]


@dataclass
class Reading:
    src_year: int
    src_month: int
    position: int      # 0..12 (0 = hace 12 meses, 12 = mes del informe)
    year: int          # año al que corresponde esta lectura
    month: int         # mes 1..12
    period: str
    metric: str
    value: float | None
    flags: str
    conf: float
    raw_token: str
    parse_issue: str


def find_tmr16_page(doc: pymupdf.Document) -> int | None:
    """Preferimos la página donde el marcador TMR16 aparece en las primeras líneas
    (es la de los gráficos) y descartamos las de introducción (texto general)."""
    candidates = []
    for i in range(len(doc)):
        txt = doc[i].get_text()
        for m in TMR16_MARKERS:
            match = m.search(txt)
            if match:
                # Penalizamos páginas donde el marker aparece tarde en el texto
                # o donde hay cadenas como "análisis" / "rutas" (páginas introductorias).
                intro_penalty = 1000 if any(k in txt.lower() for k in ("análisis", "rutas nominales", "afección acústica")) else 0
                candidates.append((match.start() + intro_penalty, i))
                break
    if not candidates:
        return None
    candidates.sort()
    return candidates[0][1]


def ocr_page(doc: pymupdf.Document, page_idx: int, dpi: int) -> list[dict]:
    pix = doc[page_idx].get_pixmap(dpi=dpi)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    data = pytesseract.image_to_data(img, lang="eng", output_type=pytesseract.Output.DICT, config="--psm 6")
    tokens = []
    for k in range(len(data["text"])):
        text = (data["text"][k] or "").strip()
        if not text:
            continue
        tokens.append({
            "text": text, "left": data["left"][k], "top": data["top"][k],
            "width": data["width"][k], "height": data["height"][k],
            "conf": float(data["conf"][k]) if data["conf"][k] != "-1" else -1.0,
        })
    return tokens


def cluster_rows(tokens: list[dict], tol: int = 8) -> list[list[dict]]:
    if not tokens:
        return []
    tokens = sorted(tokens, key=lambda t: t["top"])
    rows: list[list[dict]] = [[tokens[0]]]
    for t in tokens[1:]:
        if abs(t["top"] - rows[-1][-1]["top"]) <= tol:
            rows[-1].append(t)
        else:
            rows.append([t])
    for r in rows:
        r.sort(key=lambda t: t["left"])
    return rows


def detect_month_rows(rows: list[list[dict]]) -> list[int]:
    """Devuelve los índices de las 3 filas cabecera de meses (día/tarde/noche)."""
    results = []
    for idx, r in enumerate(rows):
        month_tokens = [t for t in r if t["text"].lower() in MONTH_LABELS]
        numeric_tokens = [t for t in r if re.search(r"^\d{2,}", t["text"])]
        if len(month_tokens) >= 4 and len(numeric_tokens) < 4:
            results.append(idx)
    return results


def infer_month_columns(
    src_year: int, src_month: int, month_tokens: list[dict]
) -> list[tuple[int, int, float]]:
    """Dadas las etiquetas de mes detectadas por OCR, reconstruye las 13 columnas.

    Devuelve una lista de 13 tuplas (year, month, x_center). Como el OCR puede perder
    algunas etiquetas, reconstruimos las faltantes por interpolación uniforme entre
    las detectadas, sabiendo que las 13 columnas son consecutivas del mes src-12 al src.
    """
    # Posiciones teóricas 0..12, donde 12 = (src_year, src_month).
    theoretical_months = []
    for pos in range(13):
        total = src_year * 12 + (src_month - 1) - (12 - pos)
        y, m0 = divmod(total, 12)
        theoretical_months.append((y, m0 + 1))

    # Para cada etiqueta OCR, identificar a qué posición corresponde.
    # El OCR da mes abreviado pero no año → ambiguo si el rango cruza años.
    # Usamos la posición relativa en X: ordenar labels por X y mapear en orden a los 13 meses.
    # Si hay N<13 labels detectadas, tenemos N puntos (pos, X); interpolamos linealmente.
    labels_sorted = sorted(month_tokens, key=lambda t: t["left"] + t["width"] / 2)
    # Identificamos qué posición ocupa cada label buscando el match con los meses teóricos.
    label_positions: list[tuple[int, float]] = []  # (pos_0_to_12, x_center)
    cursor = 0
    for lbl in labels_sorted:
        name = lbl["text"].lower()
        if name not in MONTH_LABELS:
            continue
        m_num = MONTH_LABELS.index(name) + 1
        # Encontrar el siguiente mes teórico a partir del cursor que coincida.
        for i in range(cursor, 13):
            if theoretical_months[i][1] == m_num:
                x_center = lbl["left"] + lbl["width"] / 2
                label_positions.append((i, x_center))
                cursor = i + 1
                break
    if len(label_positions) < 2:
        return []
    # Interpolación lineal para obtener los 13 centros en X.
    # Regresión: x = a + b*pos.
    xs = [p[1] for p in label_positions]
    ps = [p[0] for p in label_positions]
    n = len(ps)
    sum_p = sum(ps); sum_x = sum(xs); sum_pp = sum(p*p for p in ps); sum_px = sum(p*x for p, x in zip(ps, xs))
    denom = n * sum_pp - sum_p * sum_p
    if denom == 0:
        return []
    b = (n * sum_px - sum_p * sum_x) / denom
    a = (sum_x - b * sum_p) / n
    result = []
    for pos in range(13):
        x = a + b * pos
        y, mm = theoretical_months[pos]
        result.append((y, mm, x))
    return result


def assign_values_to_columns(
    value_tokens: list[dict], columns: list[tuple[int, int, float]], tol_x: float | None = None
) -> dict[int, dict]:
    """Asigna cada token al número de columna (0..12) por cercanía en X.

    Devuelve {position: token} con el token más cercano a cada centro de columna.
    """
    if not columns or not value_tokens:
        return {}
    # Calcular ancho medio de columna.
    xs = [c[2] for c in columns]
    col_pitch = (max(xs) - min(xs)) / 12 if len(columns) > 1 else 60
    tol = tol_x if tol_x is not None else col_pitch * 0.5

    assigned: dict[int, dict] = {}
    for t in value_tokens:
        tx = t["left"] + t["width"] / 2
        # Mejor columna
        best_pos = min(range(13), key=lambda i: abs(columns[i][2] - tx))
        if abs(columns[best_pos][2] - tx) > tol:
            continue  # fuera de cualquier columna
        # Si ya hay token para esa posición, elegir el de mayor confianza / más cercano.
        if best_pos in assigned:
            prev = assigned[best_pos]
            prev_dist = abs(columns[best_pos][2] - (prev["left"] + prev["width"] / 2))
            cur_dist = abs(columns[best_pos][2] - tx)
            if cur_dist < prev_dist:
                assigned[best_pos] = t
        else:
            assigned[best_pos] = t
    return assigned


def find_value_rows(rows: list[list[dict]], month_row_idx: int) -> list[list[dict]]:
    """Devuelve las 2 filas de valores (Total + Avión) que siguen a la cabecera."""
    val_rows = []
    for j in range(month_row_idx + 1, min(month_row_idx + 8, len(rows))):
        r = rows[j]
        if any("dB" in t["text"] for t in r):
            continue
        numeric = [t for t in r if re.search(r"^[\*¹²³⁴'\"`]*\d", t["text"])]
        nd_count = sum(1 for t in r if t["text"].upper() in ("ND", "N.D", "N.D."))
        # Fila válida si tiene al menos 1 número o si tiene muchos ND (caso King's College recién instalado).
        if numeric and (len(numeric) + nd_count >= 3):
            val_rows.append(numeric)
        if len(val_rows) == 2:
            break
    return val_rows


# -- Parseo de tokens -------------------------------------------------------

CORE_DEC_RE = re.compile(r"(\d{2,3})[.,](\d)")


def parse_value_token(tok: str) -> tuple[float | None, str, str]:
    raw = tok.replace(",", ".").strip()
    if raw in ("0", "0.0"):
        return 0.0, "", ""

    m = CORE_DEC_RE.search(raw)
    if m:
        val = float(f"{m.group(1)}.{m.group(2)}")
        rest = raw[:m.start()] + raw[m.end():]
        return val, _infer_flags(rest), _range_check(val)

    digits = re.sub(r"\D", "", raw)
    if 3 <= len(digits) <= 4:
        val = float(f"{digits[:2]}.{digits[2]}")
        return val, _infer_flags(digits[3:]), _range_check(val) or "no_decimal_dot"

    return None, "", "parse_error"


def _infer_flags(rest: str) -> str:
    has_star = "*" in rest
    has_sup = bool(re.search(r"[¹²³⁴]", rest))
    if not has_sup and re.search(r"[%)}\]'\"`1234567]", rest):
        has_sup = True
    return ("*" if has_star else "") + ("¹" if has_sup else "")


def _range_check(val: float) -> str:
    if val == 0.0 or 10.0 <= val <= 75.0:
        return ""
    return "out_of_range"


# -- Extracción de las 13 posiciones --------------------------------------

def extract_row_values(value_tokens: list[dict]) -> list[tuple[float | None, str, float, str, str]]:
    """Parsea una fila y devuelve 13 posiciones [pos0..pos12].

    Cada posición: (valor, flags, conf, raw_token, parse_issue).
    Si hay más o menos de 13 tokens, recortamos o rellenamos (con None).
    """
    # Filtrar tokens que son claramente etiquetas de la columna izquierda (LAeq, Total, Avión…).
    values = []
    for t in value_tokens:
        txt = t["text"]
        if re.search(r"^[\*¹²³⁴'\"`]*\d", txt):
            values.append(t)
    # Tomar los últimos 13 (algunos OCR añaden espurios al principio por las etiquetas).
    target = values[-13:] if len(values) >= 13 else values
    out = []
    # Alinear con 13 posiciones. Si faltan, rellenar por la izquierda.
    pad = 13 - len(target)
    for _ in range(pad):
        out.append((None, "", -1.0, "", "missing_token"))
    for t in target:
        val, flags, issue = parse_value_token(t["text"])
        out.append((val, flags, t["conf"], t["text"], issue))
    return out


# -- Mapeo posición → (año, mes) ------------------------------------------

def position_to_year_month(src_year: int, src_month: int, position: int) -> tuple[int, int]:
    """Position 12 = mes del informe. Position 0 = hace 12 meses."""
    total = src_year * 12 + (src_month - 1) - (12 - position)
    y, m0 = divmod(total, 12)
    return y, m0 + 1


# -- Pipeline por PDF ------------------------------------------------------

def process_pdf(pdf_path: Path, dpi: int = 400) -> list[Reading]:
    m = re.search(r"(\d{4})-(\d{2})", pdf_path.name)
    if not m:
        return []
    src_year, src_month = int(m.group(1)), int(m.group(2))

    doc = pymupdf.open(pdf_path)
    page_idx = find_tmr16_page(doc)
    if page_idx is None:
        return []

    tokens = ocr_page(doc, page_idx, dpi=dpi)
    rows = cluster_rows(tokens)
    mrows = detect_month_rows(rows)
    if len(mrows) < 3:
        tokens = ocr_page(doc, page_idx, dpi=500)
        rows = cluster_rows(tokens)
        mrows = detect_month_rows(rows)

    readings: list[Reading] = []
    for chart_idx in range(3):
        period = PERIODS[chart_idx]
        if chart_idx >= len(mrows):
            for metric in METRICS:
                for pos in range(13):
                    y, mm = position_to_year_month(src_year, src_month, pos)
                    readings.append(Reading(src_year, src_month, pos, y, mm, period, metric,
                                             None, "", -1, "", "chart_not_detected"))
            continue

        mrow = rows[mrows[chart_idx]]
        month_labels = [t for t in mrow if t["text"].lower() in MONTH_LABELS]
        columns = infer_month_columns(src_year, src_month, month_labels)

        val_rows = find_value_rows(rows, mrows[chart_idx])
        for metric_idx in range(2):
            metric = METRICS[metric_idx]
            if metric_idx >= len(val_rows) or not columns:
                for pos in range(13):
                    y, mm = position_to_year_month(src_year, src_month, pos)
                    readings.append(Reading(src_year, src_month, pos, y, mm, period, metric,
                                             None, "", -1, "", "row_not_detected"))
                continue
            # Filtrar solo tokens numéricos (no etiquetas como "LAeq", "Total", "Avión").
            numeric_tokens = [t for t in val_rows[metric_idx]
                              if re.search(r"^[\*¹²³⁴'\"`]*\d", t["text"])]
            assigned = assign_values_to_columns(numeric_tokens, columns)
            for pos in range(13):
                y, mm = columns[pos][:2]
                tok = assigned.get(pos)
                if tok is None:
                    readings.append(Reading(src_year, src_month, pos, y, mm, period, metric,
                                             None, "", -1, "", "no_token_at_pos"))
                    continue
                val, flags, issue = parse_value_token(tok["text"])
                readings.append(Reading(src_year, src_month, pos, y, mm, period, metric,
                                         val, flags, tok["conf"], tok["text"], issue))
    return readings


# -- Agregación ------------------------------------------------------------

@dataclass
class Aggregated:
    year: int
    month: int
    period: str
    metric: str
    median: float | None
    n_readings: int
    iqr: float | None       # dispersión entre lecturas válidas
    min_val: float | None
    max_val: float | None
    flags_consensus: str    # flags más frecuente
    needs_review: str       # razón("" si OK)


def aggregate(readings: list[Reading]) -> list[Aggregated]:
    groups: dict[tuple[int, int, str, str], list[Reading]] = defaultdict(list)
    for r in readings:
        groups[(r.year, r.month, r.period, r.metric)].append(r)

    excluded_issues = {"parse_error", "missing_token", "chart_not_detected",
                       "row_not_detected", "no_token_at_pos", "out_of_range"}
    out = []
    for (y, m, p, mt), rs in sorted(groups.items()):
        vals = [r.value for r in rs if r.value is not None and r.parse_issue not in excluded_issues]
        flags_list = [r.flags for r in rs if r.value is not None and r.parse_issue not in excluded_issues]
        if not vals:
            out.append(Aggregated(y, m, p, mt, None, len(rs), None, None, None, "", "no_valid_readings"))
            continue
        med = statistics.median(vals)
        mn, mx = min(vals), max(vals)
        iqr = mx - mn
        # Flags: tomar el más frecuente, o vacío si no hay.
        if flags_list:
            flag_counts: dict[str, int] = defaultdict(int)
            for f in flags_list:
                flag_counts[f] += 1
            consensus_flag = max(flag_counts.items(), key=lambda kv: kv[1])[0]
        else:
            consensus_flag = ""
        # Razón de review: dispersión alta, pocas lecturas, o muchos tokens corruptos.
        reasons = []
        if iqr > 5.0:
            reasons.append(f"high_spread_{iqr:.1f}")
        if len(vals) < 3:
            reasons.append(f"only_{len(vals)}_readings")
        # Si los valores difieren mucho entre sí (std > 2)
        if len(vals) >= 3:
            std = statistics.stdev(vals)
            if std > 2.0:
                reasons.append(f"std_{std:.1f}")
        out.append(Aggregated(y, m, p, mt, med, len(vals), iqr, mn, mx, consensus_flag, "|".join(reasons)))
    return out


# -- Generación de archivo de validación manual ----------------------------

def write_validation_md(
    aggregated: list[Aggregated], readings: list[Reading],
    year_range: tuple[int, int] = (2017, 2026),
) -> None:
    """Para celdas sospechosas: imprime año-mes, período, métrica, todas las lecturas.

    Excluye meses fuera de ``year_range`` (normalmente los "residuos" del rolling
    que caen 1 año antes del primer informe OCR'd).
    """
    readings_idx: dict[tuple[int, int, str, str], list[Reading]] = defaultdict(list)
    for r in readings:
        readings_idx[(r.year, r.month, r.period, r.metric)].append(r)

    yr_min, yr_max = year_range
    suspicious = [a for a in aggregated if a.needs_review and yr_min <= a.year <= yr_max]
    # Ordenar por severidad: no_valid_readings → high_spread → std → only_N.
    def severity(a: Aggregated) -> int:
        if "no_valid_readings" in a.needs_review:
            return 0
        if "high_spread" in a.needs_review:
            return 1
        if a.needs_review.startswith("std_"):
            return 2
        return 3

    suspicious.sort(key=lambda a: (severity(a), a.year, a.month, a.period, a.metric))
    by_month: dict[tuple[int, int], list[Aggregated]] = defaultdict(list)
    for a in suspicious:
        by_month[(a.year, a.month)].append(a)

    # Contadores para resumen.
    counts = {"no_valid_readings": 0, "high_spread": 0, "std": 0, "few_readings": 0}
    for a in suspicious:
        if "no_valid_readings" in a.needs_review:
            counts["no_valid_readings"] += 1
        elif "high_spread" in a.needs_review:
            counts["high_spread"] += 1
        elif a.needs_review.startswith("std_"):
            counts["std"] += 1
        else:
            counts["few_readings"] += 1

    lines = [
        "# Validación manual de valores OCR del TMR16",
        "",
        f"Rango analizado: {yr_min}-{yr_max}. **Total celdas sospechosas: {len(suspicious)}**",
        "",
        "Desglose por tipo:",
        f"- `no_valid_readings` (ninguna lectura OCR — revisar manualmente): **{counts['no_valid_readings']}**",
        f"- `high_spread` (rango >5 dB entre lecturas — posible confusión Total/Avión o mezcla de meses): **{counts['high_spread']}**",
        f"- `std_X` (desviación típica >2 dB): **{counts['std']}**",
        f"- `only_N_readings` (pocas lecturas <3): **{counts['few_readings']}**",
        "",
        "## Cómo validar",
        "",
        "Para cada celda dudosa:",
        "1. Mira la **mediana** propuesta (columna `median` en el CSV) y las lecturas individuales.",
        "2. Si la mediana parece razonable (Total 40-70 dB; Avión 15-55 dB; noche Avión puede ser 0), suele estar OK.",
        "3. Si no, abre el PDF del informe origen más cercano (p.ej. si buscas jun 2020, abre `2020-06` o `2020-07`) y busca la página del TMR16 (mirar marker `TMR[\\s\\-]?16`). Anota el valor correcto.",
        "4. Edita `data/tmr16_aggregated.csv` para corregir la mediana (opcionalmente añade una columna `manual_value`).",
        "",
    ]
    for (y, m), cells in sorted(by_month.items()):
        lines.append(f"## {y}-{m:02d}")
        lines.append("")
        for c in sorted(cells, key=lambda x: (PERIODS.index(x.period), METRICS.index(x.metric))):
            lines.append(f"### {c.period} / {c.metric} — mediana: **{c.median}**  (razón: `{c.needs_review}`, {c.n_readings} lecturas, rango {c.min_val}–{c.max_val})")
            lines.append("")
            lines.append("| informe | pos | valor | flags | conf | raw | issue |")
            lines.append("|---|---|---|---|---|---|---|")
            for r in readings_idx[(y, m, c.period, c.metric)]:
                lines.append(f"| {r.src_year}-{r.src_month:02d} | {r.position} | {r.value} | {r.flags} | {r.conf:.0f} | `{r.raw_token}` | {r.parse_issue} |")
            lines.append("")
    OUT_VALID.write_text("\n".join(lines))


# -- Main ------------------------------------------------------------------

def main(years: list[int]) -> None:
    OUT_RAW.parent.mkdir(parents=True, exist_ok=True)
    all_readings: list[Reading] = []
    for year_dir in sorted(BASE.iterdir()):
        if not year_dir.is_dir():
            continue
        try:
            yr = int(year_dir.name)
        except ValueError:
            continue
        if years and yr not in years:
            continue
        for pdf_path in sorted(year_dir.glob("*.pdf")):
            try:
                rs = process_pdf(pdf_path)
            except Exception as e:  # noqa: BLE001
                print(f"[error] {pdf_path.name}: {e}", file=sys.stderr)
                continue
            all_readings.extend(rs)
            valid = sum(1 for r in rs if r.value is not None)
            print(f"  {pdf_path.name}: {valid}/{len(rs)} lecturas válidas")

    # Escribir raw
    with OUT_RAW.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(all_readings[0]).keys()))
        writer.writeheader()
        for r in all_readings:
            writer.writerow(asdict(r))
    print(f"\nRaw readings → {OUT_RAW} ({len(all_readings)} filas)")

    # Agregar
    agg = aggregate(all_readings)
    with OUT_AGG.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(agg[0]).keys()))
        writer.writeheader()
        for a in agg:
            writer.writerow(asdict(a))
    print(f"Agregado → {OUT_AGG} ({len(agg)} filas)")

    # Validación manual
    write_validation_md(agg, all_readings)
    print(f"Validación manual → {OUT_VALID}")


if __name__ == "__main__":
    years = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else list(range(2017, 2027))
    main(years)
