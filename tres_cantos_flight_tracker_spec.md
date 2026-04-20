# Tres Cantos flight tracker

## Contexto

Tres Cantos (Madrid) está afectado por los despegues de la pista 36L del aeropuerto de Madrid-Barajas. En configuración norte (76% del tiempo), los aviones despegan hacia el norte y muchos giran al noroeste siguiendo el radial 322 del VOR de San Sebastián de los Reyes, sobrevolando Tres Cantos a baja altitud (por debajo de 1.500 m). Este proyecto busca recopilar, analizar y visualizar datos históricos de vuelo para documentar el impacto real sobre la zona.

## Fuente de datos

- **API principal:** OpenSky Network REST API (https://openskynetwork.github.io/opensky-api/rest.html)
- **Librería recomendada:** `traffic` (Python) para consulta y visualización de trayectorias (https://traffic-viz.github.io/)
- **Librería alternativa:** `pyopensky` para acceso directo a la API REST
- Registro gratuito necesario en https://opensky-network.org para acceso completo
- Para datos históricos extendidos (más de 1 hora), se puede solicitar acceso a la interfaz Trino/SQL

## Zona de interés

- **Bounding box Tres Cantos:** latitud 40.57 - 40.62, longitud -3.73 - -3.68 (ajustar según necesidad)
- **Aeropuerto de referencia:** LEMD (Madrid-Barajas)
- **Pista de interés principal:** 36L (despegues en configuración norte)
- **Altitud de filtrado:** por debajo de 3.000 m (ruido perceptible), con subfiltro por debajo de 1.500 m (ruido molesto)

## Funcionalidades

### 1. Recopilación de datos

- Consultar la API de OpenSky para obtener todos los despegues de LEMD en un rango de fechas
- Obtener las trayectorias (waypoints con posición, altitud, timestamp) de cada vuelo
- Filtrar los vuelos cuya trayectoria cruza el bounding box de Tres Cantos
- Almacenar los datos en una base de datos local SQLite para análisis posterior
- Campos a almacenar por cada paso sobre Tres Cantos:
  - icao24 (identificador de aeronave)
  - callsign (indicativo de vuelo)
  - timestamp de paso sobre la zona
  - latitud y longitud al cruzar la zona
  - altitud al cruzar la zona (en metros)
  - velocidad
  - heading (rumbo)
  - tipo de aeronave (si disponible)
  - origen/destino (si disponible)
  - día de la semana
  - hora local

### 2. Análisis y métricas

Generar las siguientes métricas a partir de los datos recopilados:

- **Vuelos por día** sobre Tres Cantos (media, mediana, máximo, mínimo)
- **Vuelos por franja horaria** (intervalos de 1 hora, de 07:00 a 23:00 y nocturno 23:00-07:00)
- **Vuelos por día de la semana** (lunes a domingo)
- **Distribución de altitudes** al cruzar la zona (histograma)
- **Vuelos por debajo de 1.500 m vs. entre 1.500-3.000 m vs. por encima de 3.000 m**
- **Detección de órbitas/holdings:** identificar vuelos que hacen giros de más de 270° dentro o cerca del bounding box (estos son los giros de 360° que se observan visualmente)
- **Comparativa por configuración:** si es posible inferir la configuración (norte/sur) a partir del volumen y dirección del tráfico, comparar días de config. norte vs. config. sur

### 3. Visualizaciones

Generar las siguientes gráficas, exportables como PNG:

- **Gráfica de barras:** número de vuelos por día sobre Tres Cantos (serie temporal)
- **Heatmap semanal:** eje X = hora del día (0-23), eje Y = día de la semana, color = número de vuelos
- **Histograma de altitudes:** distribución de altitudes de paso sobre la zona
- **Mapa de trayectorias:** sobre un mapa (usando cartopy o folium), dibujar las trazas de los vuelos que cruzan Tres Cantos, coloreadas por altitud
- **Gráfica de líneas:** evolución mensual del número de vuelos (si hay datos de varios meses)
- **Scatter plot:** hora del día vs. altitud de paso, para identificar patrones (¿los vuelos nocturnos pasan más bajo?)

### 4. Dashboard interactivo (opcional)

Si es viable, crear un dashboard con Streamlit o similar que permita:

- Seleccionar rango de fechas
- Filtrar por altitud mínima/máxima
- Filtrar por franja horaria
- Ver las gráficas actualizadas dinámicamente
- Exportar datos filtrados a CSV

## Estructura del proyecto

```
tres_cantos_tracker/
├── README.md
├── requirements.txt
├── config.py              # Credenciales OpenSky, bounding box, constantes
├── collector.py            # Recopilación de datos desde la API
├── database.py             # Gestión de la base de datos SQLite
├── analyzer.py             # Cálculo de métricas
├── visualizer.py           # Generación de gráficas
├── dashboard.py            # Dashboard Streamlit (opcional)
├── data/
│   └── flights.db          # Base de datos SQLite
└── output/
    └── charts/             # Gráficas exportadas
```

## Dependencias principales

- `pyopensky` o `traffic` (acceso a OpenSky)
- `pandas` (análisis de datos)
- `matplotlib` y/o `plotly` (visualización)
- `folium` o `cartopy` (mapas)
- `sqlite3` (base de datos, incluido en Python estándar)
- `streamlit` (dashboard, opcional)

## Notas técnicas

- La API REST de OpenSky tiene rate limiting: usuarios anónimos pueden hacer ~100 llamadas/día, usuarios registrados tienen más margen. Planificar la recopilación para no exceder los límites.
- Las trayectorias detalladas (endpoint `/tracks`) son experimentales y pueden no estar siempre disponibles. Como alternativa, usar el endpoint `/states/all` con bounding box y polling periódico.
- Los timestamps de OpenSky son Unix epoch en UTC. Convertir a hora local de Madrid (UTC+1 en invierno, UTC+2 en verano) para los análisis.
- Webtrak de AENA muestra altitudes en metros. OpenSky usa metros para altitud geométrica y pies para barométrica. Unificar en metros.
- Para inferir si un vuelo es un despegue de la 36L, buscar vuelos con origen LEMD cuya trayectoria inicial va en rumbo ~360° (norte) y que cruzan la zona a altitud ascendente.

## Posibles extensiones futuras

- Integrar datos meteorológicos (dirección del viento) para correlacionar automáticamente con configuración norte/sur
- Estimación de nivel de ruido basado en tipo de aeronave y altitud (usando tablas de certificación ICAO)
- Comparativa con los datos de los informes mensuales de ruido de AENA (TMR16 Tres Cantos)
- Sistema de alertas: notificación cuando se detecten holdings/órbitas sobre la zona
- Exportar informes automáticos para adjuntar a quejas formales en Webtrak
