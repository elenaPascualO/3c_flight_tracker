"""OCR de los valores LAeq del TMR16 en informes mensuales 2017-2023.

Los informes mensuales contienen una serie móvil de 13 meses del TMR16 con gráficos
de barras y tablas de valores bajo cada gráfico. pdfplumber/PyMuPDF no extraen esos
valores (están embebidos como imagen), así que usamos tesseract.

Estrategia:
 1. Localizar página del TMR16 en cada PDF mensual.
 2. Renderizar la página a 300 dpi.
 3. OCR con image_to_data para obtener tokens con bounding boxes y confianza.
 4. Clusterizar tokens en filas por posición Y; dentro de cada fila ordenar por X.
 5. Parsear cada token como (valor, flags). Flags típicos: ``*``, ``¹``, ``²``, ``³``,
    ``⁴``, y prefijos/sufijos ``* 41.0`` o ``40.0*¹``.
 6. Emparejar filas con períodos (día/tarde/noche) × métricas (Total/Avión) usando la
    posición relativa en la página.
 7. Para cada valor extraído: flag de sospecha si conf<70, fuera de rango [15, 75],
    o la fila tiene != 13 valores (deben ser 13 meses rolling).

Salida: CSV con una fila por (año, mes, periodo, métrica, valor, flags, conf, sospechoso).
"""
from __future__ import annotations

import csv
import io
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import pymupdf
import pytesseract
from PIL import Image

BASE = Path("doc/aena/informes_mensuales_ruido")
OUT_CSV = Path("data/tmr16_monthly_ocr.csv")

# Marcadores para localizar la página del TMR16 (varía de "TMR-16" a "TMR 16:" a "TMR 16³/⁴").
TMR16_MARKERS = [
    re.compile(r"TMR[\s\-_]*16[\*¹²³⁴]*\s*[:.]?\s*Tres\s*Cantos", re.IGNORECASE),
    re.compile(r"TMR[\s\-_]*16[³⁴]", re.IGNORECASE),
]
# Meses como etiquetas de columnas.
MONTH_LABELS = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
MONTH_TO_NUM = {m: i + 1 for i, m in enumerate(MONTH_LABELS)}

# Orden esperado de filas de valores en cada página (top→bottom):
#   día Total, día Avión, tarde Total, tarde Avión, noche Total, noche Avión
EXPECTED_ROWS = [
    ("day", "total"), ("day", "avion"),
    ("evening", "total"), ("evening", "avion"),
    ("night", "total"), ("night", "avion"),
]


@dataclass
class Value:
    year: int
    month: int
    period: str      # "day" | "evening" | "night"
    metric: str      # "total" | "avion"
    value: float | None
    flags: str       # "", "*", "*¹", etc.
    conf: float      # confianza media OCR [0, 100]
    suspicious: str  # razón ("" si OK)


def find_tmr16_page(doc: pymupdf.Document) -> int | None:
    """Devuelve el índice de página con los gráficos del TMR16 (NO la de texto anterior)."""
    candidates = []
    for i in range(len(doc)):
        txt = doc[i].get_text()
        if any(m.search(txt) for m in TMR16_MARKERS):
            candidates.append(i)
    if not candidates:
        return None
    # Preferimos la página cuyo texto es principalmente el encabezado + pie (la página del gráfico
    # tiene poco texto porque casi todo es imagen).
    best = None
    best_len = 10**9
    for i in candidates:
        txt_len = len(doc[i].get_text())
        if txt_len < best_len:
            best_len = txt_len
            best = i
    return best


def ocr_page(doc: pymupdf.Document, page_idx: int, dpi: int = 300) -> tuple[Image.Image, list[dict]]:
    """Renderiza la página y devuelve (imagen, lista de tokens OCR con bounding box).

    Cada token incluye: text, left, top, width, height, conf.
    """
    pix = doc[page_idx].get_pixmap(dpi=dpi)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    # PSM 6 = asume un bloque uniforme de texto (funciona bien para tablas densas).
    data = pytesseract.image_to_data(
        img, lang="eng", output_type=pytesseract.Output.DICT, config="--psm 6"
    )
    tokens = []
    for k in range(len(data["text"])):
        text = (data["text"][k] or "").strip()
        if not text:
            continue
        tokens.append({
            "text": text,
            "left": data["left"][k],
            "top": data["top"][k],
            "width": data["width"][k],
            "height": data["height"][k],
            "conf": float(data["conf"][k]) if data["conf"][k] != "-1" else -1.0,
        })
    return img, tokens


# -- Parse de tokens ---------------------------------------------------------

# Un valor puede venir como:
#  - "56.2"       → (56.2, "")
#  - "*41.0"      → (41.0, "*")
#  - "40.0*¹"     → (40.0, "*¹")
#  - "36.372"     → (36.3, "*¹")   OCR corrompe *¹ como "72"
#  - "39.7%"      → (39.7, "*¹")   OCR corrompe *¹ como %
#  - "378)"       → (37.8, "*¹")   falta el punto + paréntesis erróneo
#  - "547"        → (54.7, "")     falta el punto decimal (común)
#  - "4007"       → (40.0, "*¹")   falta el punto + sufijo corrompido
#  - "0"          → (0.0, "")
#
# Estrategia: buscar la forma canónica XX.X en el token; si no está, intentar
# reconstruirla a partir de los primeros dígitos con un decimal implícito.

CORE_DEC_RE = re.compile(r"(\d{2,3})[.,](\d)")  # 36.3, 54.7, etc.


def parse_value_token(tok: str, prefix_flag: str = "") -> tuple[float | None, str, str]:
    """Parsea un token a (valor, flags_limpios, razon_sospecha).

    ``prefix_flag`` se pasa cuando el token previo era un '*' aislado (flag prefix).
    """
    raw = tok.replace(",", ".").strip()
    if raw in ("0", "0.0"):
        return 0.0, prefix_flag, ""

    # Caso 1: hay XX.X explícito en el token.
    m = CORE_DEC_RE.search(raw)
    if m:
        try:
            val = float(f"{m.group(1)}.{m.group(2)}")
        except ValueError:
            return None, "", "parse_error"
        rest = raw[:m.start()] + raw[m.end():]
        flags = _infer_flags(rest, prefix_flag)
        return val, flags, _range_check(val)

    # Caso 2: solo dígitos. Asumimos que falta el punto decimal entre las dos
    # primeras cifras y la siguiente; el resto son flags.
    digits = re.sub(r"\D", "", raw)
    if 3 <= len(digits) <= 4:
        val = float(f"{digits[:2]}.{digits[2]}")
        # El 4º dígito suele ser el "¹" corrompido como 1 o 7.
        flags = _infer_flags(digits[3:], prefix_flag)
        return val, flags, _range_check(val)

    return None, "", "parse_error"


def _range_check(val: float) -> str:
    """LAeq típico en TMR16: 40-70 (Total), 15-55 (Avión), 0 legítimo (noche sin ops)."""
    if val == 0.0:
        return ""
    if 10.0 <= val <= 75.0:
        return ""
    return "out_of_range"


def _infer_flags(rest: str, prefix_flag: str) -> str:
    """Infiere flags "*" / "¹" a partir del residuo y un flag previo."""
    has_star = "*" in rest or "*" in prefix_flag
    has_sup = bool(re.search(r"[¹²³⁴]", rest + prefix_flag))
    # Caracteres espurios que suelen aparecer donde iba "¹" o "*¹".
    suspicious_chars = re.search(r"[%)}\]'\"`12347]", rest)
    if suspicious_chars and not has_sup:
        # Considerar que había una marca. Asumimos "*¹" si ya había "*".
        has_sup = True
        if not has_star and suspicious_chars.group(0) in "%)':\"1":
            has_star = True  # típicamente "*¹" viene junto
    return ("*" if has_star else "") + ("¹" if has_sup else "")


# -- Clustering de filas ------------------------------------------------------

def cluster_rows(tokens: list[dict], tol: int = 12) -> list[list[dict]]:
    """Agrupa tokens en filas por Y-position (cluster de una dimensión)."""
    if not tokens:
        return []
    tokens = sorted(tokens, key=lambda t: t["top"])
    rows: list[list[dict]] = [[tokens[0]]]
    for t in tokens[1:]:
        last_top = rows[-1][-1]["top"]
        if abs(t["top"] - last_top) <= tol:
            rows[-1].append(t)
        else:
            rows.append([t])
    for r in rows:
        r.sort(key=lambda t: t["left"])
    return rows


def detect_month_rows(rows: list[list[dict]]) -> list[tuple[int, list[str]]]:
    """Devuelve índices de filas que son cabeceras de meses (contienen ≥ 6 etiquetas de mes).

    Los informes tienen 3 cabeceras de mes (una por gráfico día/tarde/noche).
    """
    results = []
    for idx, r in enumerate(rows):
        month_tokens = [t["text"].lower() for t in r if t["text"].lower() in MONTH_LABELS]
        if len(month_tokens) >= 6:
            results.append((idx, month_tokens))
    return results


def find_value_rows(rows: list[list[dict]], month_row_idx: int) -> list[list[dict]]:
    """Dado el índice de una fila de meses, devuelve las 2 filas siguientes (Total + Avión)."""
    val_rows = []
    for j in range(month_row_idx + 1, min(month_row_idx + 6, len(rows))):
        r = rows[j]
        # Extraer solo los tokens que parezcan valores numéricos.
        numeric_toks = [t for t in r if re.search(r"\d", t["text"])]
        # Filtrar filas que son realmente cabeceras de siguiente gráfico (contienen "dB").
        if any("dB" in t["text"] for t in r):
            continue
        if len(numeric_toks) >= 8:  # umbral para aceptar la fila como "tabla de valores"
            val_rows.append(numeric_toks)
        if len(val_rows) == 2:
            break
    return val_rows


# -- Pipeline por PDF --------------------------------------------------------

def process_pdf(pdf_path: Path, year: int, month: int) -> list[Value]:
    """Procesa un PDF mensual y devuelve los valores extraídos para el mes indicado.

    Del set rolling de 13 meses tomamos SOLO el último (el mes objetivo del informe),
    que corresponde al valor más reciente y único por informe.
    """
    doc = pymupdf.open(pdf_path)
    page_idx = find_tmr16_page(doc)
    if page_idx is None:
        return []

    _img, tokens = ocr_page(doc, page_idx)
    rows = cluster_rows(tokens)
    month_rows = detect_month_rows(rows)
    if len(month_rows) < 3:
        # No hemos localizado las tres cabeceras de mes → datos sospechosos todos.
        return [Value(year, month, p, m, None, "", -1, "layout_not_detected")
                for p, m in EXPECTED_ROWS]

    # Tomamos las 3 primeras cabeceras de mes y las 2 filas de valores bajo cada una.
    results: list[Value] = []
    period_order = ["day", "evening", "night"]
    for chart_idx, (mrow_idx, _months) in enumerate(month_rows[:3]):
        period = period_order[chart_idx]
        val_rows = find_value_rows(rows, mrow_idx)
        metrics = ["total", "avion"]
        for metric_idx, vr in enumerate(val_rows[:2]):
            metric = metrics[metric_idx]
            # Último token numérico de la fila = mes objetivo.
            if not vr:
                results.append(Value(year, month, period, metric, None, "", -1, "no_tokens"))
                continue
            # Limpiar tokens que son etiquetas no numéricas (Total, Avión, L, Aeq…).
            numeric_toks = [t for t in vr if re.search(r"^[\*¹²³⁴'\"`]*\d", t["text"])]
            # Solo marcamos si faltan muchos tokens: cuando hay 10-13 el último
            # (mes objetivo) suele ser correcto; con <10 hay riesgo de solaparse con ejes.
            if len(numeric_toks) < 10:
                sus = f"found_only_{len(numeric_toks)}_of_13"
            else:
                sus = ""
            if not numeric_toks:
                results.append(Value(year, month, period, metric, None, "", -1, "no_numeric"))
                continue
            target = numeric_toks[-1]
            val, flags, parse_sus = parse_value_token(target["text"])
            conf = target["conf"]
            reasons = [r for r in (sus, parse_sus) if r]
            if conf >= 0 and conf < 70:
                reasons.append("low_conf")
            results.append(Value(
                year=year, month=month, period=period, metric=metric,
                value=val, flags=flags, conf=conf,
                suspicious="|".join(reasons),
            ))
    return results


def month_from_path(pdf_path: Path) -> tuple[int, int] | None:
    m = re.search(r"(\d{4})-(\d{2})", pdf_path.name)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def main(years: list[int]) -> None:
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    all_values: list[Value] = []
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
            ym = month_from_path(pdf_path)
            if ym is None:
                continue
            year, month = ym
            try:
                vals = process_pdf(pdf_path, year, month)
            except Exception as e:  # noqa: BLE001
                print(f"[error] {pdf_path.name}: {e}", file=sys.stderr)
                continue
            all_values.extend(vals)
            sus = sum(1 for v in vals if v.suspicious)
            print(f"  {pdf_path.name}: {len(vals)} valores, {sus} sospechosos")

    with OUT_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["year", "month", "period", "metric", "value", "flags", "conf", "suspicious"])
        writer.writeheader()
        for v in all_values:
            writer.writerow(asdict(v))
    print(f"\nEscrito {OUT_CSV} con {len(all_values)} valores")


if __name__ == "__main__":
    years = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else list(range(2017, 2024))
    main(years)
