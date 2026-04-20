"""Generate realistic sample overflight data for demo purposes.

Run with: uv run python scripts/generate_sample_data.py
"""

import random
import sys
import os
from datetime import datetime, timedelta

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.config import (
    BBOX_LAT_MIN, BBOX_LAT_MAX, BBOX_LON_MIN, BBOX_LON_MAX, TZ,
)
from src.database import init_db, insert_overflights

# Realistic fleet mix for LEMD
AIRCRAFT_TYPES = [
    ("A320", 30), ("B738", 25), ("A321", 15), ("A319", 8),
    ("B77W", 5), ("A332", 4), ("B789", 4), ("E190", 4),
    ("A20N", 3), ("B38M", 2),
]

CALLSIGN_PREFIXES = [
    ("IBE", 25), ("VLG", 20), ("RYR", 15), ("AEA", 10),
    ("DLH", 5), ("BAW", 5), ("AFR", 5), ("UAE", 3),
    ("SWR", 3), ("KLM", 3), ("TAP", 3), ("THY", 3),
]


def weighted_choice(items):
    population, weights = zip(*items)
    return random.choices(population, weights=weights, k=1)[0]


def generate_sample_data(start_date: datetime, num_days: int = 90) -> pd.DataFrame:
    """Generate realistic sample overflight data."""
    random.seed(42)
    records = []

    # Hourly flight distribution (more flights during day, fewer at night)
    hourly_weights = {
        0: 2, 1: 1, 2: 1, 3: 0, 4: 0, 5: 1, 6: 5, 7: 12, 8: 15, 9: 14,
        10: 13, 11: 12, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 14,
        18: 13, 19: 11, 20: 10, 21: 8, 22: 5, 23: 3,
    }

    for day_offset in range(num_days):
        current_date = start_date + timedelta(days=day_offset)
        weekday = current_date.weekday()

        # Fewer flights on weekends
        day_factor = 0.75 if weekday >= 5 else 1.0

        # ~76% of days are north config (36L active)
        if random.random() > 0.76:
            continue  # South config day, no overflights

        # 30-70 flights per day over Tres Cantos
        base_flights = random.randint(30, 70)
        num_flights = int(base_flights * day_factor)

        for _ in range(num_flights):
            # Pick hour based on distribution
            hour = random.choices(
                list(hourly_weights.keys()),
                weights=list(hourly_weights.values()),
                k=1,
            )[0]
            minute = random.randint(0, 59)
            second = random.randint(0, 59)

            local_dt = current_date.replace(
                hour=hour, minute=minute, second=second,
                tzinfo=TZ,
            )
            timestamp = int(local_dt.timestamp())

            # Position within bounding box (clustered around departure path)
            lat = random.gauss(40.605, 0.015)
            lat = max(BBOX_LAT_MIN, min(BBOX_LAT_MAX, lat))
            lon = random.gauss(-3.705, 0.02)
            lon = max(BBOX_LON_MIN, min(BBOX_LON_MAX, lon))

            # Altitude: bimodal — many below 1500m, some between 1500-3000m
            if random.random() < 0.6:
                altitude = random.gauss(1200, 200)
                altitude = max(500, min(1499, altitude))
            else:
                altitude = random.gauss(2000, 400)
                altitude = max(1500, min(2999, altitude))

            # Heading: roughly north with some variation
            heading = random.gauss(355, 8) % 360

            # Velocity: 220-310 knots typical for departures
            velocity = random.gauss(265, 25)

            # Aircraft type and callsign
            aircraft_type = weighted_choice(AIRCRAFT_TYPES)
            prefix = weighted_choice(CALLSIGN_PREFIXES)
            callsign = f"{prefix}{random.randint(1000, 9999)}"

            # ~3% chance of holding pattern
            is_holding = 1 if random.random() < 0.03 else 0

            records.append({
                "icao24": f"{random.randint(0x300000, 0x3fffff):06x}",
                "callsign": callsign,
                "timestamp": timestamp,
                "lat": round(lat, 6),
                "lon": round(lon, 6),
                "altitude": round(altitude, 1),
                "velocity": round(velocity, 1),
                "heading": round(heading, 1),
                "aircraft_type": aircraft_type,
                "day_of_week": weekday,
                "local_hour": hour,
                "is_holding": is_holding,
            })

    return pd.DataFrame(records)


if __name__ == "__main__":
    init_db()
    start = datetime(2024, 10, 1)
    df = generate_sample_data(start, num_days=90)
    count = insert_overflights(df)
    print(f"Generated {count} sample overflights ({start.date()} to {(start + timedelta(days=89)).date()})")
