"""Gráficas Plotly de la serie histórica de ruido del TMR-16 y TMR-61.

Combina los datos anuales (2019-2025) con los mensuales (2023-2026) para producir
series temporales de LAeq Total y Avión por periodo, con marcadores de validez
y líneas verticales en hitos relevantes (cambios de ubicación, incendio).

Las figuras se pueden embeber en Streamlit (st.plotly_chart), exportar a HTML
(fig.write_html) o a PNG (fig.write_image, requiere kaleido).
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go

from src.database import query_noise_annual, query_noise_monthly
from src.noise_metrics import RD_1367_RESIDENTIAL, WHO_2018_AIRCRAFT

PERIOD_LABELS = {
    "day": "Día (07-19h)",
    "evening": "Tarde (19-23h)",
    "night": "Noche (23-07h)",
}

# Hitos relevantes del TMR-16 (fecha como string ISO para add_vline)
TMR16_MILESTONES = [
    ("2023-07-01", "Traslado Vivero → King's College"),
    ("2025-08-15", "Incendio — TMR retirado"),
    ("2025-11-01", "TMR reinstalado"),
]


def _annual_to_midyear_timeseries(df: pd.DataFrame, metric: str, period: str) -> pd.DataFrame:
    """Convierte filas anuales al día 1 de julio del año (punto medio) y devuelve dataframe con fecha/valor/flags."""
    col_value = f"laeq_{metric}_{period}"
    col_flags = f"flags_{metric}_{period}"
    out = pd.DataFrame({
        "date": pd.to_datetime(df["year"].astype(int).astype(str) + "-07-01"),
        "value": df[col_value],
        "flags": df[col_flags].fillna(""),
        "source": "anual",
        "location_index": df["location_index"],
    })
    return out.dropna(subset=["value"])


def _monthly_to_timeseries(df: pd.DataFrame, metric: str, period_filter: str) -> pd.DataFrame:
    """Convierte filas mensuales al día 15 del mes."""
    col_value = f"laeq_{metric}"
    col_flags = f"flags_{metric}"
    filtered = df[df["period"] == period_filter].copy()
    filtered["date"] = pd.to_datetime(
        filtered["year"].astype(int).astype(str) + "-" +
        filtered["month"].astype(int).astype(str).str.zfill(2) + "-15"
    )
    out = pd.DataFrame({
        "date": filtered["date"],
        "value": filtered[col_value],
        "flags": filtered[col_flags].fillna(""),
        "source": "mensual",
        "location_index": 0,
    })
    return out.dropna(subset=["value"])


def build_tmr_timeseries(
    tmr_id: int,
    period: str,
    metric: str,
    db_path: str | None = None,
) -> pd.DataFrame:
    """Combina anual + mensual en una sola serie temporal.

    Para TMR-16 descarta las filas anuales con location_index distinto de 0 (las sub-ubicaciones
    de 2023 — TMR 16³ y TMR 16⁴ — aportan información redundante con los mensuales de 2023).
    """
    assert period in PERIOD_LABELS
    assert metric in ("total", "avion")
    annual_df = query_noise_annual(tmr_id=tmr_id, db_path=db_path)
    monthly_df = query_noise_monthly(tmr_id=tmr_id, db_path=db_path)
    # Para el TMR-16, nos quedamos con la fila consolidada (location_index=0) o, si no
    # existe, la primera sub-ubicación. Para el TMR-61 siempre location_index=0.
    annual_main = annual_df[annual_df["location_index"] == 0]
    years_with_monthly = set(monthly_df["year"].unique().tolist())
    annual_main = annual_main[~annual_main["year"].isin(years_with_monthly)]
    annual_series = _annual_to_midyear_timeseries(annual_main, metric, period)
    monthly_series = _monthly_to_timeseries(monthly_df, metric, period)
    combined = pd.concat([annual_series, monthly_series], ignore_index=True)
    return combined.sort_values("date").reset_index(drop=True)


def plot_tmr_period(
    tmr_id: int,
    period: str,
    db_path: str | None = None,
    show_milestones: bool = True,
    show_thresholds: bool = True,
) -> go.Figure:
    """Figura con Total y Avión para un TMR en un periodo (día/tarde/noche)."""
    total_df = build_tmr_timeseries(tmr_id, period, "total", db_path=db_path)
    avion_df = build_tmr_timeseries(tmr_id, period, "avion", db_path=db_path)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=total_df["date"], y=total_df["value"],
        name="LAeq Total", mode="lines+markers",
        line=dict(color="#1f77b4", width=2),
        text=total_df["flags"],
        hovertemplate="%{x|%Y-%m}<br>Total: %{y:.1f} dB %{text}<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=avion_df["date"], y=avion_df["value"],
        name="LAeq Avión", mode="lines+markers",
        line=dict(color="#ff7f0e", width=2),
        text=avion_df["flags"],
        hovertemplate="%{x|%Y-%m}<br>Avión: %{y:.1f} dB %{text}<extra></extra>",
    ))
    if show_thresholds:
        fig.add_hline(
            y=RD_1367_RESIDENTIAL[period], line_dash="dot", line_color="#2ca02c",
            annotation_text=f"RD 1367/2007 ({RD_1367_RESIDENTIAL[period]} dB)",
            annotation_position="top right",
        )
        if period == "night":
            fig.add_hline(
                y=WHO_2018_AIRCRAFT["lnight"], line_dash="dash", line_color="#d62728",
                annotation_text=f"OMS 2018 Lnight ({WHO_2018_AIRCRAFT['lnight']} dB)",
                annotation_position="bottom right",
            )
    if show_milestones and tmr_id == 16:
        for date, label in TMR16_MILESTONES:
            fig.add_shape(
                type="line", xref="x", yref="paper",
                x0=date, x1=date, y0=0, y1=1,
                line=dict(dash="dash", color="gray", width=1), opacity=0.5,
            )
            fig.add_annotation(
                x=date, yref="paper", y=1, text=label,
                showarrow=False, textangle=-30, xanchor="left",
                font=dict(size=10, color="gray"),
            )
    fig.update_layout(
        title=f"TMR-{tmr_id} — {PERIOD_LABELS[period]}",
        xaxis_title="Fecha",
        yaxis_title="LAeq (dB A)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
    )
    return fig


def plot_tmr_comparison(
    tmr_ids: list[int],
    period: str,
    metric: str,
    db_path: str | None = None,
) -> go.Figure:
    """Compara varios TMRs en el mismo periodo y métrica."""
    fig = go.Figure()
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    for i, tmr in enumerate(tmr_ids):
        df = build_tmr_timeseries(tmr, period, metric, db_path=db_path)
        fig.add_trace(go.Scatter(
            x=df["date"], y=df["value"],
            name=f"TMR-{tmr}", mode="lines+markers",
            line=dict(color=colors[i % len(colors)]),
            text=df["flags"],
            hovertemplate="%{x|%Y-%m}<br>%{y:.1f} dB %{text}<extra></extra>",
        ))
    metric_label = "LAeq Avión" if metric == "avion" else "LAeq Total"
    fig.update_layout(
        title=f"Comparativa TMR — {PERIOD_LABELS[period]} · {metric_label}",
        xaxis_title="Fecha",
        yaxis_title="dB A",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
    )
    return fig
