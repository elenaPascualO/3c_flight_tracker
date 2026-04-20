"""Data collection from OpenSky Network via Trino (historical data)."""

from datetime import date, datetime, timedelta

import pandas as pd
from traffic.data import opensky

from src.config import (
    ALTITUDE_PERCEPTIBLE,
    BBOX_LAT_MAX,
    BBOX_LAT_MIN,
    BBOX_LON_MAX,
    BBOX_LON_MIN,
    HEADING_36L_MAX,
    HEADING_36L_MIN,
    TZ,
)
from src.database import insert_overflights, register_collection_run


def is_heading_north(heading: float) -> bool:
    """Check if heading is roughly north (340-360 or 0-20)."""
    if heading is None:
        return False
    return heading >= HEADING_36L_MIN or heading <= HEADING_36L_MAX


def detect_holding(flight) -> bool:
    """Detect if a flight performs a holding pattern (>270° turn) near the bbox."""
    try:
        if flight.data is None or len(flight.data) < 10:
            return False
        headings = flight.data["heading"].dropna()
        if len(headings) < 5:
            return False
        # Calculate cumulative heading change
        diffs = headings.diff().dropna()
        # Normalize to -180..180
        diffs = diffs.apply(lambda x: (x + 180) % 360 - 180)
        total_turn = abs(diffs.sum())
        return total_turn > 270
    except Exception:
        return False


def collect_overflights(
    start_date: date,
    end_date: date,
    progress_callback=None,
) -> int:
    """
    Collect overflight data for Tres Cantos from OpenSky Trino.

    Args:
        start_date: Start of date range to collect
        end_date: End of date range to collect
        progress_callback: Optional callable(progress: float, message: str)

    Returns:
        Number of overflights found and stored
    """
    total_days = (end_date - start_date).days + 1
    all_overflights = []

    for day_offset in range(total_days):
        current_date = start_date + timedelta(days=day_offset)
        progress = day_offset / total_days

        if progress_callback:
            progress_callback(progress, f"Consultando {current_date.isoformat()}...")

        try:
            day_overflights = _collect_day(current_date)
            all_overflights.extend(day_overflights)
        except Exception as e:
            if progress_callback:
                progress_callback(progress, f"Error en {current_date}: {e}")
            continue

    if not all_overflights:
        register_collection_run(start_date, end_date, 0)
        return 0

    df = pd.DataFrame(all_overflights)
    num_inserted = insert_overflights(df)
    register_collection_run(start_date, end_date, num_inserted)

    if progress_callback:
        progress_callback(1.0, f"Completado: {num_inserted} sobrevuelos encontrados")

    return num_inserted


def _collect_day(target_date: date) -> list[dict]:
    """Collect overflights for a single day."""
    start = datetime(target_date.year, target_date.month, target_date.day, 0, 0, 0)
    end = start + timedelta(days=1)

    # Query flights in the bounding box from Trino
    flights = opensky.history(
        start=start,
        stop=end,
        bounds=(BBOX_LAT_MIN, BBOX_LON_MIN, BBOX_LAT_MAX, BBOX_LON_MAX),
    )

    if flights is None:
        return []

    overflights = []

    for flight in flights:
        if flight.data is None or flight.data.empty:
            continue

        # Filter points within bbox and below altitude threshold
        data = flight.data
        in_bbox = data[
            (data["latitude"] >= BBOX_LAT_MIN)
            & (data["latitude"] <= BBOX_LAT_MAX)
            & (data["longitude"] >= BBOX_LON_MIN)
            & (data["longitude"] <= BBOX_LON_MAX)
            & (data["altitude"].notna())
            & (data["altitude"] <= ALTITUDE_PERCEPTIBLE)
        ]

        if in_bbox.empty:
            continue

        # Check if it's a northbound departure (36L)
        avg_heading = in_bbox["heading"].mean()
        if not is_heading_north(avg_heading):
            continue

        # Take the first point in bbox as the crossing point
        crossing = in_bbox.iloc[0]

        timestamp = int(crossing["timestamp"].timestamp())
        local_dt = crossing["timestamp"].astimezone(TZ)

        is_holding = detect_holding(flight)

        overflights.append({
            "icao24": flight.icao24 or "",
            "callsign": (flight.callsign or "").strip(),
            "timestamp": timestamp,
            "lat": crossing["latitude"],
            "lon": crossing["longitude"],
            "altitude": crossing["altitude"],
            "velocity": crossing.get("groundspeed") or crossing.get("velocity"),
            "heading": crossing["heading"],
            "aircraft_type": getattr(flight, "typecode", None) or "",
            "day_of_week": local_dt.weekday(),
            "local_hour": local_dt.hour,
            "is_holding": int(is_holding),
        })

    return overflights
