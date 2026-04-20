"""Streamlit dashboard for Tres Cantos flight noise impact analysis."""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import math
import random
import folium
from folium import MacroElement
from jinja2 import Template
from streamlit_folium import st_folium
from datetime import date, timedelta

from src.config import (
    ALTITUDE_NOISY,
    ALTITUDE_PERCEPTIBLE,
    BBOX_LAT_MAX,
    BBOX_LAT_MIN,
    BBOX_LON_MAX,
    BBOX_LON_MIN,
    CENTER_LAT,
    CENTER_LON,
)
from src.database import init_db, query_overflights, get_downloaded_ranges
from src.collector import collect_overflights
from src.analyzer import (
    flights_per_day,
    flights_per_hour,
    flights_per_weekday,
    altitude_distribution,
    heatmap_data,
    hourly_altitude_scatter,
    monthly_evolution,
    daily_series,
    nighttime_stats,
    DAYS_ES,
)

st.set_page_config(
    page_title="Tres Cantos Flight Tracker",
    page_icon="✈️",
    layout="wide",
)

init_db()

# --- Sidebar ---
st.sidebar.title("✈️ Tres Cantos Flight Tracker")
st.sidebar.markdown("Impacto acústico de despegues 36L (Barajas)")

st.sidebar.header("📥 Descargar datos")
col1, col2 = st.sidebar.columns(2)
with col1:
    dl_start = st.date_input("Desde", value=date.today() - timedelta(days=7), key="dl_start")
with col2:
    dl_end = st.date_input("Hasta", value=date.today() - timedelta(days=1), key="dl_end")

if st.sidebar.button("Descargar", type="primary", use_container_width=True):
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    def update_progress(progress: float, message: str):
        progress_bar.progress(progress)
        status_text.text(message)

    num = collect_overflights(dl_start, dl_end, progress_callback=update_progress)
    st.sidebar.success(f"✅ {num} sobrevuelos descargados")

# Show downloaded ranges
ranges = get_downloaded_ranges()
if ranges:
    st.sidebar.caption("Rangos disponibles:")
    for r in ranges:
        st.sidebar.caption(f"  {r['start_date']} → {r['end_date']} ({r['num_flights']} vuelos)")

st.sidebar.divider()
st.sidebar.header("🔍 Filtros")

# Date filter
col1, col2 = st.sidebar.columns(2)
with col1:
    filter_start = st.date_input("Desde", value=date.today() - timedelta(days=30), key="f_start")
with col2:
    filter_end = st.date_input("Hasta", value=date.today(), key="f_end")

# Altitude filter
altitude_filter = st.sidebar.multiselect(
    "Altitud",
    options=["< 1500m (molesto)", "1500-3000m (perceptible)"],
    default=["< 1500m (molesto)", "1500-3000m (perceptible)"],
)

# Hour filter
hour_range = st.sidebar.slider("Franja horaria", 0, 23, (0, 23))

# Day of week filter
days_filter = st.sidebar.multiselect(
    "Días de la semana",
    options=list(range(7)),
    format_func=lambda x: DAYS_ES[x],
    default=list(range(7)),
)

# Build altitude bounds
max_alt = ALTITUDE_PERCEPTIBLE
min_alt = 0
if "< 1500m (molesto)" in altitude_filter and "1500-3000m (perceptible)" not in altitude_filter:
    max_alt = ALTITUDE_NOISY
elif "1500-3000m (perceptible)" in altitude_filter and "< 1500m (molesto)" not in altitude_filter:
    min_alt = ALTITUDE_NOISY

# Query data
df = query_overflights(
    start_date=filter_start,
    end_date=filter_end,
    min_altitude=min_alt if min_alt > 0 else None,
    max_altitude=max_alt,
    hour_min=hour_range[0],
    hour_max=hour_range[1],
    days_of_week=days_filter if len(days_filter) < 7 else None,
)

# Export
if not df.empty:
    csv = df.to_csv(index=False).encode("utf-8")
    st.sidebar.download_button("📤 Exportar CSV", csv, "overflights.csv", "text/csv", use_container_width=True)

# --- Main content ---
st.title("Impacto acústico sobre Tres Cantos")
st.caption("Despegues pista 36L — Aeropuerto de Madrid-Barajas")

if df.empty:
    st.info("No hay datos para los filtros seleccionados. Descarga datos desde la barra lateral.")
    st.stop()

# KPIs
stats = flights_per_day(df)
alt_dist = altitude_distribution(df)
night = nighttime_stats(df)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total vuelos", len(df))
kpi2.metric("Media diaria", stats["mean"])
kpi3.metric("% bajo 1500m", f"{round(alt_dist['below_1500'] / len(df) * 100, 1)}%")
kpi4.metric("Máx. en un día", stats["max"])

# Tabs
tab_map, tab_daily, tab_heatmap, tab_altitude, tab_scatter, tab_monthly = st.tabs([
    "🗺️ Mapa", "📊 Por día", "🔥 Heatmap semanal",
    "📏 Altitudes", "⏰ Hora vs Altitud", "📈 Evolución mensual",
])

# --- Helper: draw base map with bbox ---
def _make_base_map():
    m = folium.Map(location=[CENTER_LAT, CENTER_LON], zoom_start=13, tiles="CartoDB positron")
    folium.Rectangle(
        bounds=[[BBOX_LAT_MIN, BBOX_LON_MIN], [BBOX_LAT_MAX, BBOX_LON_MAX]],
        color="blue",
        fill=False,
        weight=2,
        dash_array="5",
        popup="Zona de estudio: Tres Cantos",
    ).add_to(m)
    return m


def _generate_full_trajectory(row):
    """Generate a synthetic trajectory that passes through the recorded point.

    Builds a trajectory backwards and forwards from the recorded position
    using the heading, so the line always crosses the dot on the map.
    """
    rng = random.Random(hash(row["callsign"]) + row["timestamp"])

    heading_rad = math.radians(row["heading"])
    cos_heading = math.cos(heading_rad)
    sin_heading = math.sin(heading_rad)
    cos_lat = math.cos(math.radians(row["lat"]))

    step = 0.0015  # ~170m per point
    jitter = 0.00015  # slight wobble for realism

    # How many points before and after the recorded position
    # Extend backward to bbox south edge, forward to bbox north edge
    back_dist = (row["lat"] - BBOX_LAT_MIN) / max(abs(cos_heading), 0.3)
    fwd_dist = (BBOX_LAT_MAX - row["lat"]) / max(abs(cos_heading), 0.3)
    n_back = min(int(back_dist / step), 30)
    n_fwd = min(int(fwd_dist / step), 30)

    # Altitude gradient: climbing through the bbox
    alt_per_step = rng.uniform(15, 35)  # meters per step

    points = []

    # Points before the recorded position (going backwards)
    for i in range(n_back, 0, -1):
        lat = row["lat"] - i * step * cos_heading + rng.gauss(0, jitter)
        lon = row["lon"] - i * step * sin_heading / cos_lat + rng.gauss(0, jitter)
        alt = row["altitude"] - i * alt_per_step
        points.append({"lat": round(lat, 6), "lon": round(lon, 6), "alt": round(max(300, alt), 0)})

    # The recorded position itself
    points.append({"lat": row["lat"], "lon": row["lon"], "alt": round(row["altitude"], 0)})

    # Points after the recorded position (going forward)
    for i in range(1, n_fwd + 1):
        lat = row["lat"] + i * step * cos_heading + rng.gauss(0, jitter)
        lon = row["lon"] + i * step * sin_heading / cos_lat + rng.gauss(0, jitter)
        alt = row["altitude"] + i * alt_per_step
        points.append({"lat": round(lat, 6), "lon": round(lon, 6), "alt": round(alt, 0)})

    return points


def _add_clickable_markers(m, flight_df, max_flights=200):
    """Add dot markers that show trajectory on click, info shown outside map."""
    sample = flight_df.head(max_flights)

    # Build all trajectories and flight info for JS
    all_trajectories = {}
    all_flight_info = {}

    for idx, (_, row) in enumerate(sample.iterrows()):
        color = "red" if row["altitude"] < ALTITUDE_NOISY else "orange"
        traj = _generate_full_trajectory(row)

        segments = []
        for i in range(len(traj) - 1):
            p1, p2 = traj[i], traj[i + 1]
            avg_alt = (p1["alt"] + p2["alt"]) / 2
            seg_color = "#d32f2f" if avg_alt < ALTITUDE_NOISY else "#ff9800"
            segments.append({
                "coords": [[p1["lat"], p1["lon"]], [p2["lat"], p2["lon"]]],
                "color": seg_color,
                "alt": round(avg_alt),
            })

        marker_id = f"flight_{idx}"
        all_trajectories[marker_id] = segments
        all_flight_info[marker_id] = {
            "callsign": row["callsign"],
            "altitude": round(row["altitude"]),
            "hour": row["local_hour"],
            "aircraft_type": row["aircraft_type"],
            "heading": round(row["heading"]),
        }

        # Marker without popup — use tooltip only for callsign on hover
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=5,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7,
            tooltip=row["callsign"],
            popup=folium.Popup(
                f'<div data-flight-id="{marker_id}" style="display:none"></div>',
                max_width=1,
            ),
        ).add_to(m)

    # JS: on click draw trajectory, on click elsewhere clear it
    traj_json = json.dumps(all_trajectories)
    info_json = json.dumps(all_flight_info)

    click_handler = MacroElement()
    click_handler._template = Template(
        "{%% macro script(this, kwargs) %%}"
        "var trajectories = %s;"
        "var flightInfo = %s;"
        "var activeLines = [];"
        "var infoDiv = null;"
        "function clearLines() {"
        "    activeLines.forEach(function(l) { l.remove(); });"
        "    activeLines = [];"
        "    if (infoDiv) { infoDiv.remove(); infoDiv = null; }"
        "}"
        "var _currentFlightId = null;"
        "function updatePanel(info, alt) {"
        "    if (infoDiv) infoDiv.remove();"
        "    var borderColor = alt < 1500 ? '#d32f2f' : '#ff9800';"
        "    infoDiv = L.control({position: 'bottomleft'});"
        "    infoDiv.onAdd = function() {"
        "        var d = L.DomUtil.create('div', 'flight-info-panel');"
        "        d.style.cssText = 'background:white;padding:10px 14px;border-radius:8px;"
        "border:2px solid '+borderColor+';font:13px/1.5 sans-serif;"
        "box-shadow:0 2px 8px rgba(0,0,0,0.2);min-width:180px';"
        "        d.innerHTML = '<b style=\"font-size:15px\">'+info.callsign+'</b><br>'"
        "            +'Altitud: <b>'+alt+'m</b><br>'"
        "            +'Hora: '+('0'+info.hour).slice(-2)+':00<br>'"
        "            +'Tipo: '+info.aircraft_type+'<br>'"
        "            +'Heading: '+info.heading+'°';"
        "        return d;"
        "    };"
        "    infoDiv.addTo({{ this._parent.get_name() }});"
        "}"
        "function showInfo(id) {"
        "    var info = flightInfo[id];"
        "    if (!info) return;"
        "    _currentFlightId = id;"
        "    clearLines();"
        "    var segs = trajectories[id];"
        "    if (segs) {"
        "        segs.forEach(function(seg) {"
        "            var line = L.polyline(seg.coords, {"
        "                color: seg.color, weight: 3.5, opacity: 0.85"
        "            }).addTo({{ this._parent.get_name() }});"
        "            line.on('click', function() {"
        "                updatePanel(info, seg.alt);"
        "            });"
        "            activeLines.push(line);"
        "        });"
        "    }"
        "    updatePanel(info, info.altitude);"
        "}"
        "{{ this._parent.get_name() }}.on('popupopen', function(e) {"
        "    var raw = e.popup.getContent();"
        "    var content = (typeof raw === 'string') ? raw : raw.innerHTML || '';"
        "    var match = content.match(/data-flight-id=\\\"([^\\\"]+)\\\"/);"
        "    if (match) showInfo(match[1]);"
        "    {{ this._parent.get_name() }}.closePopup();"
        "});"
        "{{ this._parent.get_name() }}.on('click', function(e) {"
        "    if (!e.originalEvent.target.closest('.leaflet-interactive')) {"
        "        clearLines();"
        "    }"
        "});"
        "{%% endmacro %%}" % (traj_json, info_json)
    )
    m.add_child(click_handler)

    return all_flight_info


# --- Tab: Map ---
with tab_map:
    st.subheader("Mapa de sobrevuelos")

    map_hour = st.slider("Franja horaria", 0, 23, (7, 22), key="map_hour")
    map_df = df[(df["local_hour"] >= map_hour[0]) & (df["local_hour"] <= map_hour[1])]

    m = _make_base_map()
    _add_clickable_markers(m, map_df)
    st_folium(m, use_container_width=True, height=500)

    st.caption(f"Mostrando {min(len(map_df), 200)} vuelos entre las {map_hour[0]:02d}:00 y {map_hour[1]:02d}:00")
    st.caption("🔴 < 1500m | 🟠 1500-3000m — haz clic en un punto para ver la trayectoria")

# --- Tab: Daily ---
with tab_daily:
    st.subheader("Vuelos por día")
    daily = daily_series(df)
    if not daily.empty:
        fig = px.bar(daily, x="date", y="count", color_discrete_sequence=["#d32f2f"])
        fig.update_layout(xaxis_title="Fecha", yaxis_title="Nº vuelos", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Media", stats["mean"])
    col2.metric("Mediana", stats["median"])
    col3.metric("Máximo", stats["max"])
    col4.metric("Mínimo", stats["min"])

# --- Tab: Heatmap ---
with tab_heatmap:
    st.subheader("Heatmap: hora × día de la semana")
    heatmap = heatmap_data(df)
    fig = go.Figure(data=go.Heatmap(
        z=heatmap.values,
        x=[f"{h:02d}:00" for h in range(24)],
        y=DAYS_ES,
        colorscale="YlOrRd",
        colorbar=dict(title="Vuelos"),
    ))
    fig.update_layout(xaxis_title="Hora", yaxis_title="Día")
    st.plotly_chart(fig, use_container_width=True)

# --- Tab: Altitude ---
with tab_altitude:
    st.subheader("Distribución de altitudes")
    fig = px.histogram(
        df, x="altitude", nbins=30,
        color_discrete_sequence=["#d32f2f"],
        labels={"altitude": "Altitud (m)", "count": "Nº vuelos"},
    )
    fig.add_vline(x=ALTITUDE_NOISY, line_dash="dash", line_color="red",
                  annotation_text="1500m (molesto)")
    fig.add_vline(x=ALTITUDE_PERCEPTIBLE, line_dash="dash", line_color="orange",
                  annotation_text="3000m (perceptible)")
    fig.update_layout(yaxis_title="Nº vuelos")
    st.plotly_chart(fig, use_container_width=True)

    # Summary
    col1, col2, col3 = st.columns(3)
    col1.metric("< 1500m", alt_dist["below_1500"])
    col2.metric("1500-3000m", alt_dist["between_1500_3000"])
    col3.metric("> 3000m", alt_dist["above_3000"])

# --- Tab: Scatter ---
with tab_scatter:
    st.subheader("Hora vs Altitud")
    scatter_df = hourly_altitude_scatter(df)
    if not scatter_df.empty:
        fig = px.scatter(
            scatter_df, x="local_hour", y="altitude",
            color="altitude", color_continuous_scale="YlOrRd_r",
            labels={"local_hour": "Hora", "altitude": "Altitud (m)"},
            opacity=0.6,
        )
        fig.add_hline(y=ALTITUDE_NOISY, line_dash="dash", line_color="red")
        fig.update_layout(xaxis=dict(dtick=1))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"**Vuelos nocturnos (23-07):** {night['count']} ({night['percentage']}%) — "
                f"Altitud media: {night['mean_altitude']:.0f}m")

# --- Tab: Monthly ---
with tab_monthly:
    st.subheader("Evolución mensual")
    monthly = monthly_evolution(df)
    if not monthly.empty:
        fig = px.line(monthly, x="month", y="count", markers=True, color_discrete_sequence=["#d32f2f"])
        fig.update_layout(xaxis_title="Mes", yaxis_title="Nº vuelos")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Se necesitan datos de varios meses para esta gráfica.")
