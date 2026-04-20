"""SQLite database management for flight overflight data."""

import sqlite3
from datetime import date, datetime

import pandas as pd

from src.config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS overflights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    icao24 TEXT NOT NULL,
    callsign TEXT,
    timestamp INTEGER NOT NULL,
    lat REAL NOT NULL,
    lon REAL NOT NULL,
    altitude REAL NOT NULL,
    velocity REAL,
    heading REAL,
    aircraft_type TEXT,
    day_of_week INTEGER NOT NULL,
    local_hour INTEGER NOT NULL,
    is_holding INTEGER DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_timestamp ON overflights(timestamp);
CREATE INDEX IF NOT EXISTS idx_altitude ON overflights(altitude);
CREATE INDEX IF NOT EXISTS idx_day_of_week ON overflights(day_of_week);
CREATE INDEX IF NOT EXISTS idx_local_hour ON overflights(local_hour);

CREATE TABLE IF NOT EXISTS collection_runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'completed',
    num_flights INTEGER DEFAULT 0,
    collected_at TEXT NOT NULL
);
"""


def get_connection(db_path: str | None = None) -> sqlite3.Connection:
    """Get a connection to the SQLite database."""
    conn = sqlite3.connect(db_path or DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_path: str | None = None) -> None:
    """Initialize database schema."""
    conn = get_connection(db_path)
    conn.executescript(SCHEMA)
    conn.close()


def insert_overflights(df: pd.DataFrame, db_path: str | None = None) -> int:
    """Insert overflight records from a DataFrame. Returns number of rows inserted."""
    if df.empty:
        return 0
    conn = get_connection(db_path)
    cols = [
        "icao24", "callsign", "timestamp", "lat", "lon", "altitude",
        "velocity", "heading", "aircraft_type", "day_of_week", "local_hour", "is_holding",
    ]
    records = df[cols].to_dict("records")
    conn.executemany(
        f"INSERT INTO overflights ({', '.join(cols)}) VALUES ({', '.join('?' * len(cols))})",
        [tuple(r[c] for c in cols) for r in records],
    )
    conn.commit()
    count = len(records)
    conn.close()
    return count


def register_collection_run(start_date: date, end_date: date, num_flights: int, db_path: str | None = None) -> None:
    """Register a completed data collection run."""
    conn = get_connection(db_path)
    conn.execute(
        "INSERT INTO collection_runs (start_date, end_date, num_flights, collected_at) VALUES (?, ?, ?, ?)",
        (start_date.isoformat(), end_date.isoformat(), num_flights, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()


def get_downloaded_ranges(db_path: str | None = None) -> list[dict]:
    """Get list of already-downloaded date ranges."""
    conn = get_connection(db_path)
    rows = conn.execute(
        "SELECT start_date, end_date, num_flights, collected_at FROM collection_runs ORDER BY start_date"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def query_overflights(
    start_date: date | None = None,
    end_date: date | None = None,
    min_altitude: float | None = None,
    max_altitude: float | None = None,
    hour_min: int | None = None,
    hour_max: int | None = None,
    days_of_week: list[int] | None = None,
    db_path: str | None = None,
) -> pd.DataFrame:
    """Query overflights with optional filters. Returns a DataFrame."""
    conn = get_connection(db_path)
    query = "SELECT * FROM overflights WHERE 1=1"
    params: list = []

    if start_date:
        start_ts = int(datetime.combine(start_date, datetime.min.time()).timestamp())
        query += " AND timestamp >= ?"
        params.append(start_ts)
    if end_date:
        end_ts = int(datetime.combine(end_date, datetime.max.time()).timestamp())
        query += " AND timestamp <= ?"
        params.append(end_ts)
    if min_altitude is not None:
        query += " AND altitude >= ?"
        params.append(min_altitude)
    if max_altitude is not None:
        query += " AND altitude <= ?"
        params.append(max_altitude)
    if hour_min is not None:
        query += " AND local_hour >= ?"
        params.append(hour_min)
    if hour_max is not None:
        query += " AND local_hour <= ?"
        params.append(hour_max)
    if days_of_week:
        placeholders = ", ".join("?" * len(days_of_week))
        query += f" AND day_of_week IN ({placeholders})"
        params.extend(days_of_week)

    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df
