"""Extrae el % de configuración Sur mes a mes desde los informes mensuales de AENA."""
from __future__ import annotations

import re
from pathlib import Path

import pdfplumber

BASE = Path("doc/aena/informes_mensuales_ruido")
OUT_CSV = Path("data/config_sur_monthly.csv")

# Regex sobre el bloque "Operatividad" del informe ejecutivo (página 3).
# Ejemplo:
#   "operó 103,2 horas en configuración Sur, un 14,3% del tiempo total."
#   "Se realizaron un 17,6% de operaciones bajo condiciones de configuración Sur"
#   "El porcentaje acumulado de horas en configuración Sur en junio de 2025 ha sido de un 22,5%."
RE_HOURS = re.compile(r"oper[óo]\s+([\d,]+)\s*horas?\s+en\s+configuración\s+Sur[^%]*?([\d,]+)\s*%", re.IGNORECASE | re.DOTALL)
# Permitimos palabras intermedias (pdfplumber a veces intercala el encabezado lateral "Operatividad").
RE_OPS = re.compile(r"([\d,]+)\s*%\s+(?:\w+\s+){0,3}de\s+(?:\w+\s+){0,3}operaciones\s+bajo\s+condiciones\s+de\s+configuración\s+Sur", re.IGNORECASE)
RE_CUM = re.compile(r"porcentaje\s+acumulado\s+de\s+horas\s+en\s+configuración\s+Sur[^%]*?([\d,]+)\s*%", re.IGNORECASE | re.DOTALL)


def _num(s: str) -> float:
    return float(s.replace(",", "."))


def extract(pdf_path: Path) -> dict | None:
    with pdfplumber.open(pdf_path) as pdf:
        # El informe ejecutivo suele estar en las páginas 3-6 según plantilla (2017-2021 vs 2022+).
        text = ""
        for i in range(min(8, len(pdf.pages))):
            text += "\n" + (pdf.pages[i].extract_text() or "")
    # Normalizar saltos de línea que rompen los matches.
    flat = re.sub(r"\s+", " ", text)
    m_h = RE_HOURS.search(flat)
    m_o = RE_OPS.search(flat)
    m_c = RE_CUM.search(flat)
    if not (m_h and m_o):
        return None
    return {
        "horas_sur": _num(m_h.group(1)),
        "pct_horas_sur": _num(m_h.group(2)),
        "pct_ops_sur": _num(m_o.group(1)),
        "pct_acum_horas_sur": _num(m_c.group(1)) if m_c else None,
    }


def main() -> None:
    import csv
    results: list[tuple[int, int, dict]] = []
    for year_dir in sorted(BASE.iterdir()):
        if not year_dir.is_dir():
            continue
        try:
            year = int(year_dir.name)
        except ValueError:
            continue
        for pdf_path in sorted(year_dir.glob("*.pdf")):
            m = re.search(r"(\d{4})-(\d{2})", pdf_path.name)
            if not m:
                continue
            month = int(m.group(2))
            data = extract(pdf_path)
            if data is None:
                print(f"  [skip] {pdf_path.name}: no match")
                continue
            results.append((year, month, data))

    print(f"\n{'Año-Mes':<10} {'Horas Sur':>10} {'% Horas':>9} {'% Oper':>9} {'% Acum':>9}")
    print("-" * 50)
    for year, month, d in results:
        acum = f"{d['pct_acum_horas_sur']:.1f}%" if d['pct_acum_horas_sur'] is not None else "—"
        print(f"{year}-{month:02d}     {d['horas_sur']:>9.1f}  {d['pct_horas_sur']:>7.1f}%  {d['pct_ops_sur']:>7.1f}%  {acum:>8}")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["year", "month", "horas_sur", "pct_horas_sur", "pct_ops_sur", "pct_acum_horas_sur"])
        for year, month, d in results:
            writer.writerow([year, month, d["horas_sur"], d["pct_horas_sur"], d["pct_ops_sur"], d["pct_acum_horas_sur"]])
    print(f"\nCSV → {OUT_CSV}")


if __name__ == "__main__":
    main()
