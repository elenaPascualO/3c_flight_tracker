"""Análisis estadístico y gráficas del cruce config Sur × TMR16.

Produce:
 - ``doc/figures/scatter_pctsur_vs_laeq.png``: scatter + regresión por sensor.
 - ``doc/figures/timeseries_pctsur_laeq.png``: serie temporal con línea de cambio de sensor.
 - ``doc/figures/residuals_outliers.png``: residuos de la regresión (top outliers).
 - ``data/analysis_results.json``: estadísticos (correlación, regresión, outliers).
"""
from __future__ import annotations

import csv
import json
from datetime import date
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

CSV_IN = Path("data/config_sur_vs_tmr16.csv")
FIG_DIR = Path("doc/figures")
RESULTS_JSON = Path("data/analysis_results.json")


def load() -> list[dict]:
    rows = []
    with CSV_IN.open() as f:
        for row in csv.DictReader(f):
            # Convertir floats
            for k in list(row.keys()):
                if k in ("year", "month"):
                    row[k] = int(row[k])
                elif k.startswith("laeq_") and not k.endswith(("_flags", "_n_readings", "_review")):
                    row[k] = float(row[k]) if row[k] else None
                elif k in ("pct_horas_sur", "pct_ops_sur", "pct_acum_horas_sur", "horas_sur"):
                    row[k] = float(row[k]) if row[k] else None
            rows.append(row)
    return rows


def ym_to_date(row: dict) -> date:
    return date(row["year"], row["month"], 1)


def analyze_correlation(rows: list[dict], sensor: str, period: str, metric: str) -> dict | None:
    """Correlación entre pct_horas_sur y LAeq del TMR16 para un sensor/periodo/métrica."""
    col = f"laeq_{metric}_{period}"
    x = []
    y = []
    meta = []  # guardar referencia (year, month)
    for r in rows:
        if r["sensor"] != sensor:
            continue
        if r["pct_horas_sur"] is None or r[col] is None:
            continue
        x.append(r["pct_horas_sur"])
        y.append(r[col])
        meta.append((r["year"], r["month"]))
    if len(x) < 4:
        return None
    x_arr = np.array(x)
    y_arr = np.array(y)
    pearson_r, pearson_p = stats.pearsonr(x_arr, y_arr)
    spearman_r, spearman_p = stats.spearmanr(x_arr, y_arr)
    # Regresión lineal
    slope, intercept, r_value, p_value, std_err = stats.linregress(x_arr, y_arr)
    y_pred = slope * x_arr + intercept
    residuals = y_arr - y_pred
    # Outliers: |residual| > 2 * std
    resid_std = float(np.std(residuals))
    outliers = []
    for (yr, mo), res in zip(meta, residuals):
        if abs(res) > 2 * resid_std:
            outliers.append({"year": yr, "month": mo, "residual": float(res)})
    outliers.sort(key=lambda o: -abs(o["residual"]))
    return {
        "sensor": sensor,
        "period": period,
        "metric": metric,
        "n": len(x),
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_r": float(spearman_r),
        "spearman_p": float(spearman_p),
        "regression": {"slope": float(slope), "intercept": float(intercept), "r_squared": float(r_value ** 2), "p_value": float(p_value), "std_err": float(std_err)},
        "residuals_std": resid_std,
        "outliers": outliers[:10],
        "x": x, "y": y, "meta": meta,
    }


def plot_scatter_by_sensor(results: list[dict], out_path: Path) -> None:
    """Scatter % horas sur vs LAeq Avión día para ambos sensores."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
    for ax, sensor, color in zip(axes, ("vivero", "kings_college"), ("#d62728", "#1f77b4")):
        res = next((r for r in results if r["sensor"] == sensor and r["period"] == "day" and r["metric"] == "avion"), None)
        if not res:
            ax.set_title(f"{sensor}: sin datos suficientes")
            continue
        x = np.array(res["x"])
        y = np.array(res["y"])
        ax.scatter(x, y, color=color, alpha=0.7, label=f"n={res['n']}")
        # Regresión
        xs = np.linspace(x.min(), x.max(), 50)
        ys = res["regression"]["slope"] * xs + res["regression"]["intercept"]
        ax.plot(xs, ys, color="black", linestyle="--", label=f"r={res['pearson_r']:.2f}, p={res['pearson_p']:.3g}")
        # Outliers etiquetados
        for o in res["outliers"][:5]:
            # Buscar x, y correspondientes
            for (yr, mo), xv, yv in zip(res["meta"], x, y):
                if yr == o["year"] and mo == o["month"]:
                    ax.annotate(f"{yr}-{mo:02d}", (xv, yv), fontsize=8, xytext=(4, 4), textcoords="offset points")
        ax.set_xlabel("% horas en configuración Sur")
        ax.set_ylabel("LAeq Avión día (TMR16, dB)")
        ax.set_title(f"Sensor {sensor.replace('_', ' ').title()}\n({_range_label(res['meta'])})")
        ax.legend()
        ax.grid(alpha=0.3)
    fig.suptitle("Relación entre configuración Sur y ruido de avión diurno (TMR16)", fontsize=13)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    print(f"  {out_path}")


def _range_label(meta: list[tuple[int, int]]) -> str:
    if not meta:
        return ""
    first = min(meta)
    last = max(meta)
    return f"{first[0]}-{first[1]:02d} a {last[0]}-{last[1]:02d}"


def plot_timeseries(rows: list[dict], out_path: Path) -> None:
    """Serie temporal: % horas Sur + LAeq Avión día, con línea vertical en el cambio de sensor."""
    rows_sorted = sorted([r for r in rows if r["pct_horas_sur"] is not None], key=ym_to_date)
    dates = [ym_to_date(r) for r in rows_sorted]
    pct_sur = [r["pct_horas_sur"] for r in rows_sorted]
    laeq = [r["laeq_avion_day"] for r in rows_sorted]

    fig, ax1 = plt.subplots(figsize=(13, 5))
    ax1.bar(dates, pct_sur, width=25, color="#ffcc00", alpha=0.5, label="% horas en config Sur", edgecolor="#cc9900")
    ax1.set_xlabel("Fecha")
    ax1.set_ylabel("% horas Sur", color="#cc9900")
    ax1.tick_params(axis="y", labelcolor="#cc9900")
    ax1.set_ylim(0, 60)

    ax2 = ax1.twinx()
    ax2.plot(dates, laeq, color="#d62728", marker="o", markersize=3, linewidth=1.2, label="LAeq Avión día (TMR16)")
    ax2.set_ylabel("LAeq Avión día TMR16 (dB)", color="#d62728")
    ax2.tick_params(axis="y", labelcolor="#d62728")

    # Línea vertical en el cambio de sensor (1 julio 2023)
    ax1.axvline(date(2023, 7, 1), color="black", linestyle="--", alpha=0.7)
    ax1.text(date(2023, 7, 15), 58, "Cambio sensor\n(Vivero → King's College)", fontsize=8, ha="left", va="top")

    ax1.set_title("Serie temporal: configuración Sur vs ruido de avión diurno en Tres Cantos (TMR16)")
    ax1.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    print(f"  {out_path}")


def plot_residuals(results: list[dict], out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    for ax, sensor in zip(axes, ("vivero", "kings_college")):
        res = next((r for r in results if r["sensor"] == sensor and r["period"] == "day" and r["metric"] == "avion"), None)
        if not res:
            continue
        x = np.array(res["x"])
        y = np.array(res["y"])
        y_pred = res["regression"]["slope"] * x + res["regression"]["intercept"]
        residuals = y - y_pred
        dates = [date(yr, mo, 1) for yr, mo in res["meta"]]
        # Ordenar por fecha
        order = sorted(range(len(dates)), key=lambda i: dates[i])
        dates_sorted = [dates[i] for i in order]
        res_sorted = [residuals[i] for i in order]
        ax.bar(dates_sorted, res_sorted, width=25, color="#444", alpha=0.7)
        ax.axhline(0, color="black", linewidth=0.5)
        two_std = 2 * res["residuals_std"]
        ax.axhline(two_std, color="red", linestyle="--", alpha=0.5, label=f"±2σ = ±{two_std:.1f} dB")
        ax.axhline(-two_std, color="red", linestyle="--", alpha=0.5)
        # Anotar outliers
        for o in res["outliers"][:3]:
            ax.annotate(f"{o['year']}-{o['month']:02d}", (date(o["year"], o["month"], 1), o["residual"]),
                        fontsize=8, xytext=(2, 4 if o["residual"] > 0 else -10), textcoords="offset points")
        ax.set_title(f"Residuos regresión — {sensor.replace('_', ' ').title()}")
        ax.set_ylabel("Residual (dB)")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    print(f"  {out_path}")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    rows = load()

    results = []
    for sensor in ("vivero", "kings_college"):
        for period in ("day", "evening", "night"):
            for metric in ("total", "avion"):
                r = analyze_correlation(rows, sensor, period, metric)
                if r:
                    results.append(r)

    # Guardar resultados (sin los arrays x/y/meta pesados).
    trimmed = []
    for r in results:
        copy = {k: v for k, v in r.items() if k not in ("x", "y", "meta")}
        trimmed.append(copy)
    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_JSON.write_text(json.dumps(trimmed, indent=2, default=str))
    print(f"Resultados estadísticos → {RESULTS_JSON}")

    # Gráficas principales (centradas en día/avión — relevantes para despegues Norte sobre TC).
    print("\nGeneradas:")
    plot_scatter_by_sensor(results, FIG_DIR / "scatter_pctsur_vs_laeq.png")
    plot_timeseries(rows, FIG_DIR / "timeseries_pctsur_laeq.png")
    plot_residuals(results, FIG_DIR / "residuals_outliers.png")


if __name__ == "__main__":
    main()
