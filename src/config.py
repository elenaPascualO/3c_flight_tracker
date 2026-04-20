"""Configuration constants for Tres Cantos flight tracker."""

import os
from zoneinfo import ZoneInfo

# Bounding box Tres Cantos (lat_min, lat_max, lon_min, lon_max)
BBOX_LAT_MIN = 40.57
BBOX_LAT_MAX = 40.65
BBOX_LON_MIN = -3.76
BBOX_LON_MAX = -3.65

# Center point for map
CENTER_LAT = (BBOX_LAT_MIN + BBOX_LAT_MAX) / 2
CENTER_LON = (BBOX_LON_MIN + BBOX_LON_MAX) / 2

# Airport
AIRPORT_ICAO = "LEMD"
RUNWAY = "36L"

# Altitude thresholds (meters)
ALTITUDE_NOISY = 1500  # Ruido molesto
ALTITUDE_PERCEPTIBLE = 3000  # Ruido perceptible

# Timezone
TZ = ZoneInfo("Europe/Madrid")

# Heading range for 36L departures (roughly north)
HEADING_36L_MIN = 340
HEADING_36L_MAX = 20  # wraps around 360

# Database
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "flights.db")


def get_opensky_credentials() -> tuple[str, str]:
    """Get OpenSky OAuth2 credentials (client_id, client_secret)."""
    try:
        import streamlit as st
        client_id = st.secrets["opensky"]["client_id"]
        client_secret = st.secrets["opensky"]["client_secret"]
    except Exception:
        client_id = os.environ.get("OPENSKY_CLIENT_ID", "")
        client_secret = os.environ.get("OPENSKY_CLIENT_SECRET", "")
    return client_id, client_secret
