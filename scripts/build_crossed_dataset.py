"""Cruza el dataset de configuración Sur con el del TMR16 y produce:

 - ``data/config_sur_vs_tmr16.csv``: una fila por (año, mes) con ambos datasets.
 - ``data/config_sur_vs_tmr16_summary.md``: resumen con stats agregadas.

La serie del TMR16 se divide en dos a partir de julio 2023, cuando el sensor se
reubicó de "Tres Cantos" (Vivero municipal) a "Tres Cantos-King's College".
Las dos series NO son comparables directamente: las distancias a las rutas de
vuelo, el ruido de fondo y el perfil de calibración cambiaron.
"""
from __future__ import annotations

import csv
from pathlib import Path

CFG = Path("data/config_sur_monthly.csv")
TMR = Path("data/tmr16_aggregated.csv")
OUT = Path("data/config_sur_vs_tmr16.csv")


def main() -> None:
    cfg: dict[tuple[int, int], dict] = {}
    with CFG.open() as f:
        for row in csv.DictReader(f):
            key = (int(row["year"]), int(row["month"]))
            cfg[key] = {k: float(v) if v else None for k, v in row.items() if k not in ("year", "month")}

    tmr: dict[tuple[int, int, str, str], dict] = {}
    with TMR.open() as f:
        for row in csv.DictReader(f):
            key = (int(row["year"]), int(row["month"]), row["period"], row["metric"])
            tmr[key] = row

    rows = []
    all_months = sorted(set(cfg.keys()) | {(int(r["year"]), int(r["month"])) for r in tmr.values()})
    for ym in all_months:
        y, m = ym
        if y < 2017 or y > 2026:
            continue
        # Sensor ID: Vivero hasta jun 2023 incluido; King's College desde jul 2023.
        if (y, m) < (2023, 7):
            sensor = "vivero"
        else:
            sensor = "kings_college"

        row: dict = {"year": y, "month": m, "sensor": sensor}

        c = cfg.get(ym, {})
        row["pct_horas_sur"] = c.get("pct_horas_sur")
        row["pct_ops_sur"] = c.get("pct_ops_sur")
        row["pct_acum_horas_sur"] = c.get("pct_acum_horas_sur")
        row["horas_sur"] = c.get("horas_sur")

        for period in ("day", "evening", "night"):
            for metric in ("total", "avion"):
                t = tmr.get((y, m, period, metric), {})
                col = f"laeq_{metric}_{period}"
                row[col] = t.get("median") or None
                row[f"{col}_flags"] = t.get("flags_consensus") or ""
                row[f"{col}_n_readings"] = t.get("n_readings") or 0
                row[f"{col}_review"] = t.get("needs_review") or ""
        rows.append(row)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        print("No rows to write")
        return
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Merged CSV → {OUT} ({len(rows)} filas)")

    # Quick coverage summary
    with_sur = sum(1 for r in rows if r["pct_horas_sur"])
    with_tmr_day = sum(1 for r in rows if r["laeq_avion_day"])
    with_both = sum(1 for r in rows if r["pct_horas_sur"] and r["laeq_avion_day"])
    print(f"  Meses con dato config sur:         {with_sur}/{len(rows)}")
    print(f"  Meses con laeq_avion_day TMR16:    {with_tmr_day}/{len(rows)}")
    print(f"  Meses con AMBOS (cruzables):       {with_both}/{len(rows)}")


if __name__ == "__main__":
    main()
