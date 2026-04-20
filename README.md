# Tres Cantos Flight Tracker

Open-source tool to document the noise impact of LEMD runway 36L departures over Tres Cantos (Madrid, Spain).

## Context

Tres Cantos is a residential town north of Madrid directly under the departure path of runway 36L at Madrid-Barajas airport. When the airport operates in north configuration (~76% of the time), departing aircraft follow the 322 radial northwestbound, overflying residential areas at altitudes as low as 1,000–1,500 meters. This project aims to provide objective, data-driven evidence of the overflight frequency and altitude patterns to support formal noise complaints to the Tres Cantos municipality and AENA (Spanish airport authority).

## What it does

- Collects historical flight trajectory data from [OpenSky Network](https://opensky-network.org/) via Trino
- Filters departures that cross the Tres Cantos area below 3,000m with northbound heading (runway 36L)
- Detects holding patterns (360° turns) over the area
- Presents statistics, charts, and an interactive map in a Streamlit dashboard
- Allows data export (CSV) for use in formal complaints

## Dashboard

The dashboard includes:

- **Interactive map** of overflight positions, color-coded by altitude
- **Daily flight counts** with summary statistics
- **Weekly heatmap** (hour of day × day of week)
- **Altitude distribution** with thresholds: <1,500m (high noise) and 1,500–3,000m (perceptible)
- **Hour vs altitude scatter plot** to identify patterns (e.g. lower altitudes at night)
- **Monthly evolution** for trend analysis

## Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- An [OpenSky Network](https://opensky-network.org/) account with Trino access (for historical data)

### Installation

```bash
uv sync
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Edit .streamlit/secrets.toml with your OpenSky credentials
streamlit run app.py
```

### OpenSky Trino access

Historical flight data requires approved access to OpenSky's Trino database:

1. Register at https://opensky-network.org
2. Request data access: **My OpenSky > Request Data Access**
3. Select "Trino" as data type
4. Access is granted for research and non-commercial use

## Project structure

| File | Description |
|------|-------------|
| `app.py` | Streamlit dashboard (entry point) |
| `src/config.py` | Constants: bounding box, altitude thresholds, airport config |
| `src/collector.py` | Data collection from OpenSky/Trino via the `traffic` library |
| `src/database.py` | SQLite schema, queries, and data management |
| `src/analyzer.py` | Statistical metrics computation |
| `tests/` | Test suite (pytest) |

## Key parameters

| Parameter | Value |
|-----------|-------|
| Bounding box | lat 40.57–40.65, lon -3.76 to -3.65 |
| High noise threshold | < 1,500 m altitude |
| Perceptible threshold | 1,500–3,000 m altitude |
| Heading filter | 340°–20° (northbound, runway 36L) |
| Airport | LEMD (Madrid-Barajas) |

## Data source

All flight data comes from [OpenSky Network](https://opensky-network.org/), a non-profit association that provides open air traffic data collected from a network of ADS-B receivers. This project queries historical state vectors via their Trino/SQL interface.

## License

This project is open source. Data from OpenSky Network is subject to their [terms of use](https://opensky-network.org/about/terms-of-use).

## Acknowledgements

- [OpenSky Network](https://opensky-network.org/) for providing open flight data
- [traffic](https://traffic-viz.github.io/) library for trajectory analysis