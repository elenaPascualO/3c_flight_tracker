"""Re-ejecuta la agregación y generación de archivos a partir del raw_readings.csv.

Útil cuando ajustas la lógica de agregación sin querer re-correr el OCR."""
from __future__ import annotations

import csv
from dataclasses import asdict
from pathlib import Path

import sys
sys.path.insert(0, "scripts")
from ocr_tmr16_monthly import Reading, aggregate, write_validation_md, OUT_AGG, OUT_RAW, OUT_VALID


def load_readings(path: Path) -> list[Reading]:
    rs = []
    with path.open() as f:
        for row in csv.DictReader(f):
            rs.append(Reading(
                src_year=int(row["src_year"]), src_month=int(row["src_month"]),
                position=int(row["position"]), year=int(row["year"]), month=int(row["month"]),
                period=row["period"], metric=row["metric"],
                value=float(row["value"]) if row["value"] else None,
                flags=row["flags"], conf=float(row["conf"]) if row["conf"] else -1.0,
                raw_token=row["raw_token"], parse_issue=row["parse_issue"],
            ))
    return rs


def main() -> None:
    readings = load_readings(OUT_RAW)
    agg = aggregate(readings)
    with OUT_AGG.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(asdict(agg[0]).keys()))
        writer.writeheader()
        for a in agg:
            writer.writerow(asdict(a))
    print(f"Agregado → {OUT_AGG} ({len(agg)} filas)")
    write_validation_md(agg, readings)
    print(f"Validación → {OUT_VALID}")


if __name__ == "__main__":
    main()
