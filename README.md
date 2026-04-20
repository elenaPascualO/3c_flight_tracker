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

- **Interactive map** — click any overflight dot to see its full trajectory through the study area, color-coded by altitude (red < 1,500m, orange 1,500–3,000m). Click on any segment of the trajectory to see the altitude at that point.
- **Daily flight counts** with summary statistics (mean, median, max, min)
- **Weekly heatmap** (hour of day × day of week)
- **Altitude distribution** with thresholds: <1,500m (high noise) and 1,500–3,000m (perceptible)
- **Hour vs altitude scatter plot** to identify patterns (e.g. lower altitudes at night)
- **Monthly evolution** for trend analysis

## Quick start (demo with synthetic data)

No accounts or credentials needed — just Python and `uv`:

1. **Install uv** (if you don't have it):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and run:**
   ```bash
   git clone https://github.com/elenaPascualO/3c_flight_tracker.git
   cd 3c_flight_tracker
   uv sync
   uv run python scripts/generate_sample_data.py
   uv run streamlit run app.py
   ```

3. **View the dashboard:** open http://localhost:8501 in your browser. The sample data covers **October–December 2024**, so set the date filters in the sidebar to that range (e.g. `2024/10/01` to `2024/12/29`).

## Setup with real data

To collect real flight data, you need an OpenSky Network account with Trino access:

1. Register at https://opensky-network.org
2. Request data access: **My OpenSky > Request Data Access** (select "Trino")
3. Configure credentials:
   ```bash
   cp .streamlit/secrets.toml.example .streamlit/secrets.toml
   # Edit .streamlit/secrets.toml with your OpenSky credentials
   ```
4. Run the dashboard:
   ```bash
   uv run streamlit run app.py
   ```
5. Use the "Descargar datos" section in the sidebar to download flight data for specific date ranges.

## Project structure

| File | Description |
|------|-------------|
| `app.py` | Streamlit dashboard (entry point) |
| `src/config.py` | Constants: bounding box, altitude thresholds, airport config |
| `src/collector.py` | Data collection from OpenSky/Trino via the `traffic` library |
| `src/database.py` | SQLite schema, queries, and data management |
| `src/analyzer.py` | Statistical metrics computation |
| `scripts/generate_sample_data.py` | Generate synthetic demo data |
| `tests/` | Test suite (pytest) |

## Key parameters

| Parameter | Value |
|-----------|-------|
| Bounding box | lat 40.57–40.65, lon -3.76 to -3.65 |
| High noise threshold | < 1,500 m altitude |
| Perceptible threshold | 1,500–3,000 m altitude |
| Heading filter | 340°–20° (northbound, runway 36L) |
| Airport | LEMD (Madrid-Barajas) |

## Status

This project is under active development. We are currently awaiting approval for access to OpenSky Network's historical flight database (Trino). In the meantime, the dashboard can be tested with synthetic sample data (see [Quick start](#quick-start-demo-with-synthetic-data)).

The project will evolve over time based on data availability and feedback from contributors and users. Feature requests and contributions are welcome — feel free to open an issue or pull request.

## Data source

All flight data comes from [OpenSky Network](https://opensky-network.org/), a non-profit association that provides open air traffic data collected from a network of ADS-B receivers. This project queries historical state vectors via their Trino/SQL interface.

## License

MIT License. See [LICENSE](LICENSE) for details. Data from OpenSky Network is subject to their [terms of use](https://opensky-network.org/about/terms-of-use).

## Acknowledgements

- [OpenSky Network](https://opensky-network.org/) for providing open flight data
- [traffic](https://traffic-viz.github.io/) library for trajectory analysis
