# Tres Cantos Flight Tracker

## What is this?

App para documentar el impacto acústico de los despegues de la pista 36L de Barajas sobre Tres Cantos (Madrid). Recopila datos históricos de vuelo desde OpenSky Network (Trino), los almacena en SQLite y los presenta en un dashboard Streamlit.

## Stack

- Python 3.12+
- `traffic` (acceso a OpenSky/Trino + análisis de trayectorias)
- `streamlit` (dashboard)
- `plotly` (gráficas interactivas)
- `folium` + `streamlit-folium` (mapa interactivo)
- `pandas` (análisis de datos)
- SQLite (almacenamiento local)
- `uv` (gestión de dependencias)
- `pytest` (testing)

## How to run

```bash
uv sync                    # instalar dependencias
streamlit run app.py       # lanzar dashboard
```

## How to test

```bash
uv run pytest              # ejecutar todos los tests
uv run pytest tests/test_analyzer.py  # un archivo específico
uv run pytest -v           # verbose
```

## Project structure

- `src/config.py` — constantes, bounding box, credenciales
- `src/database.py` — SQLite: esquema, insert, queries
- `src/collector.py` — recopilación de datos desde OpenSky/Trino
- `src/analyzer.py` — cálculo de métricas estadísticas
- `app.py` — dashboard Streamlit (entry point)
- `tests/` — tests con pytest

## Key constants

- Bounding box Tres Cantos: lat 40.57-40.65, lon -3.76 a -3.65
- Altitud molesta: <1500m | Perceptible: 1500-3000m
- Timezone: Europe/Madrid
- Aeropuerto: LEMD, pista 36L

## Testing policy

- Toda nueva funcionalidad testeable DEBE ir acompañada de tests.
- Al terminar un desarrollo, ejecutar `uv run pytest` y verificar que todos los tests pasan antes de dar el trabajo por válido.
- Los tests de collector.py no deben requerir conexión a Trino (usar mocks o testear solo funciones puras).

## Deployment

Streamlit Community Cloud. Secrets se configuran en la UI de Streamlit Cloud (no en el repo).
