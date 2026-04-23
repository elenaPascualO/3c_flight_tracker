"""Extrae datos de ruido de los informes de AENA (anuales y mensuales) y los persiste en SQLite.

Uso:
    uv run python -m src.noise_extract               # todos
    uv run python -m src.noise_extract annual        # solo informes anuales
    uv run python -m src.noise_extract monthly       # solo informes mensuales
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from src.database import init_db, insert_noise_annual, insert_noise_monthly
from src.noise_report_parser import (
    parse_annual_summary,
    parse_monthly_report,
    parse_tmr_monthly,
)

ROOT = Path(__file__).resolve().parent.parent
ANNUAL_DIR = ROOT / "doc" / "aena" / "informes_anuales_ruido"
MONTHLY_DIR = ROOT / "doc" / "aena" / "informes_mensuales_ruido"


def extract_annual(reports_dir: Path = ANNUAL_DIR, db_path: str | None = None) -> None:
    for pdf in sorted(reports_dir.glob("*.pdf")):
        m = re.match(r"(\d{4})_informe_anual\.pdf", pdf.name)
        if not m:
            continue
        year = int(m.group(1))
        annual = parse_annual_summary(pdf, year)
        n_annual = insert_noise_annual(annual, source_file=pdf.name, db_path=db_path)
        n_monthly = 0
        for tmr_id in (16, 61):
            rep = parse_tmr_monthly(pdf, tmr_id, year)
            if rep and rep.monthly:
                n_monthly += insert_noise_monthly(rep.monthly, source_file=pdf.name, db_path=db_path)
        print(f"  anual {year}: {n_annual} filas resumen, {n_monthly} filas mensuales")


def extract_monthly(reports_dir: Path = MONTHLY_DIR, db_path: str | None = None) -> None:
    """Procesa los informes mensuales Envirosuite (texto extraíble: 2024-2025)."""
    for year_dir in sorted(reports_dir.iterdir()):
        if not year_dir.is_dir():
            continue
        for pdf in sorted(year_dir.glob("*_informe_ruido.pdf")):
            m = re.match(r"(\d{4})-(\d{2})_informe_ruido\.pdf", pdf.name)
            if not m:
                continue
            total = 0
            for tmr_id in (16, 61):
                try:
                    rep = parse_monthly_report(pdf, tmr_id)
                except Exception as e:
                    print(f"  {pdf.name} TMR{tmr_id}: ERROR {e}")
                    continue
                if rep and rep.monthly:
                    total += insert_noise_monthly(rep.monthly, source_file=pdf.name, db_path=db_path)
            print(f"  mensual {pdf.name}: {total} filas")


def main(scope: str = "all", db_path: str | None = None) -> None:
    init_db(db_path)
    if scope in ("all", "annual"):
        print("-- Informes anuales --")
        extract_annual(db_path=db_path)
    if scope in ("all", "monthly"):
        print("-- Informes mensuales --")
        extract_monthly(db_path=db_path)


if __name__ == "__main__":
    scope = sys.argv[1] if len(sys.argv) > 1 else "all"
    main(scope)
