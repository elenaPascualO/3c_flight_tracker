"""SQLite database management for flight overflight data."""

import sqlite3
from dataclasses import asdict
from datetime import date, datetime

import pandas as pd

from src.config import DB_PATH
from src.noise_report_parser import AnnualRow, MonthlyRow

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

CREATE TABLE IF NOT EXISTS noise_annual (
    year INTEGER NOT NULL,
    tmr_id INTEGER NOT NULL,
    location_index INTEGER,
    tmr_flag TEXT NOT NULL DEFAULT '',
    laeq_total_day REAL, flags_total_day TEXT NOT NULL DEFAULT '',
    laeq_avion_day REAL, flags_avion_day TEXT NOT NULL DEFAULT '',
    laeq_total_evening REAL, flags_total_evening TEXT NOT NULL DEFAULT '',
    laeq_avion_evening REAL, flags_avion_evening TEXT NOT NULL DEFAULT '',
    laeq_total_night REAL, flags_total_night TEXT NOT NULL DEFAULT '',
    laeq_avion_night REAL, flags_avion_night TEXT NOT NULL DEFAULT '',
    source_file TEXT NOT NULL,
    PRIMARY KEY (year, tmr_id, location_index)
);

CREATE TABLE IF NOT EXISTS noise_monthly (
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    tmr_id INTEGER NOT NULL,
    period TEXT NOT NULL,
    laeq_total REAL,
    flags_total TEXT NOT NULL DEFAULT '',
    laeq_avion REAL,
    flags_avion TEXT NOT NULL DEFAULT '',
    source_file TEXT NOT NULL,
    PRIMARY KEY (year, month, tmr_id, period)
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


def insert_noise_annual(rows: list[AnnualRow], source_file: str, db_path: str | None = None) -> int:
    """Insert/replace annual LAeq rows. Returns count inserted."""
    if not rows:
        return 0
    conn = get_connection(db_path)
    payload = []
    for r in rows:
        d = asdict(r)
        d["source_file"] = source_file
        # SQLite PRIMARY KEY no permite NULL en una columna de PK; usamos 0 como sentinel
        # para "ubicación única" y reservamos 1..N para sub-ubicaciones diferenciadas.
        if d["location_index"] is None:
            d["location_index"] = 0
        payload.append(d)
    cols = list(payload[0].keys())
    conn.executemany(
        f"INSERT OR REPLACE INTO noise_annual ({', '.join(cols)}) VALUES ({', '.join(':' + c for c in cols)})",
        payload,
    )
    conn.commit()
    conn.close()
    return len(payload)


def insert_noise_monthly(rows: list[MonthlyRow], source_file: str, db_path: str | None = None) -> int:
    """Insert/replace monthly LAeq rows. Returns count inserted."""
    if not rows:
        return 0
    conn = get_connection(db_path)
    payload = [{**asdict(r), "source_file": source_file} for r in rows]
    cols = list(payload[0].keys())
    conn.executemany(
        f"INSERT OR REPLACE INTO noise_monthly ({', '.join(cols)}) VALUES ({', '.join(':' + c for c in cols)})",
        payload,
    )
    conn.commit()
    conn.close()
    return len(payload)


def query_noise_annual(tmr_id: int | None = None, db_path: str | None = None) -> pd.DataFrame:
    """Query annual noise rows, optionally filtered by TMR id."""
    conn = get_connection(db_path)
    query = "SELECT * FROM noise_annual"
    params: list = []
    if tmr_id is not None:
        query += " WHERE tmr_id = ?"
        params.append(tmr_id)
    query += " ORDER BY year, tmr_id, location_index"
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


def query_noise_monthly(tmr_id: int | None = None, db_path: str | None = None) -> pd.DataFrame:
    """Query monthly noise rows, optionally filtered by TMR id."""
    conn = get_connection(db_path)
    query = "SELECT * FROM noise_monthly"
    params: list = []
    if tmr_id is not None:
        query += " WHERE tmr_id = ?"
        params.append(tmr_id)
    query += " ORDER BY year, month, tmr_id, period"
    df = pd.read_sql_query(query, conn, params=params)
    conn.close()
    return df


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
