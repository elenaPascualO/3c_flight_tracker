"""Extrae datos de ruido de los informes anuales de AENA y los persiste en SQLite.

Uso:
    uv run python -m src.noise_extract
"""

from __future__ import annotations

import re
from pathlib import Path

from src.database import init_db, insert_noise_annual, insert_noise_monthly
from src.noise_report_parser import parse_annual_summary, parse_tmr_monthly

REPORTS_DIR = Path(__file__).resolve().parent.parent / "doc" / "aena" / "informes_anuales_ruido"


def extract_all(reports_dir: Path = REPORTS_DIR, db_path: str | None = None) -> None:
    init_db(db_path)
    for pdf in sorted(reports_dir.glob("*.pdf")):
        m = re.match(r"(\d{4})_informe_anual\.pdf", pdf.name)
        if not m:
            continue
        year = int(m.group(1))
        annual = parse_annual_summary(pdf, year)
        n_annual = insert_noise_annual(annual, source_file=pdf.name, db_path=db_path)
        # Mensual para TMR-16 y TMR-61
        n_monthly = 0
        for tmr_id in (16, 61):
            rep = parse_tmr_monthly(pdf, tmr_id, year)
            if rep and rep.monthly:
                n_monthly += insert_noise_monthly(rep.monthly, source_file=pdf.name, db_path=db_path)
        print(f"{year}: {n_annual} anuales, {n_monthly} mensuales")


if __name__ == "__main__":
    extract_all()
