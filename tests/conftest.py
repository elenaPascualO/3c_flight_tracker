"""Shared fixtures for tests."""

import pandas as pd
import pytest

from src.database import init_db


@pytest.fixture
def sample_overflights() -> pd.DataFrame:
    """Sample overflight data for testing."""
    return pd.DataFrame([
        {
            "icao24": "3c4b26", "callsign": "DLH1234", "timestamp": 1710000000,
            "lat": 40.60, "lon": -3.70, "altitude": 1200.0, "velocity": 250.0,
            "heading": 350.0, "aircraft_type": "A320", "day_of_week": 0,
            "local_hour": 10, "is_holding": 0,
        },
        {
            "icao24": "3c4b27", "callsign": "IBE5678", "timestamp": 1710003600,
            "lat": 40.61, "lon": -3.71, "altitude": 1800.0, "velocity": 270.0,
            "heading": 355.0, "aircraft_type": "B738", "day_of_week": 0,
            "local_hour": 11, "is_holding": 0,
        },
        {
            "icao24": "3c4b28", "callsign": "RYR9012", "timestamp": 1710090000,
            "lat": 40.59, "lon": -3.69, "altitude": 900.0, "velocity": 240.0,
            "heading": 5.0, "aircraft_type": "B738", "day_of_week": 1,
            "local_hour": 2, "is_holding": 1,
        },
        {
            "icao24": "3c4b29", "callsign": "VLG3456", "timestamp": 1710093600,
            "lat": 40.62, "lon": -3.72, "altitude": 2500.0, "velocity": 280.0,
            "heading": 345.0, "aircraft_type": "A321", "day_of_week": 1,
            "local_hour": 14, "is_holding": 0,
        },
        {
            "icao24": "3c4b30", "callsign": "UAE7890", "timestamp": 1710097200,
            "lat": 40.58, "lon": -3.68, "altitude": 1100.0, "velocity": 260.0,
            "heading": 2.0, "aircraft_type": "B77W", "day_of_week": 1,
            "local_hour": 23, "is_holding": 0,
        },
    ])


@pytest.fixture
def tmp_db(tmp_path) -> str:
    """Create a temporary database for testing."""
    db_path = str(tmp_path / "test_flights.db")
    init_db(db_path)
    return db_path
