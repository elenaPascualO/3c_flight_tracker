# Análisis de datos de ruido de AENA: contexto, fuentes y limitaciones

## Objetivo

Complementar la app de seguimiento de vuelos (datos OpenSky) con un análisis crítico de los datos oficiales de ruido que publica AENA para Tres Cantos. El objetivo final es poder cruzar datos de trayectorias independientes (OpenSky) con datos de ruido oficiales (AENA) e identificar inconsistencias, lagunas y posibles sesgos.

---

## 1. Validez de los datos de OpenSky frente a AENA

### Qué es OpenSky
- Red de investigación sin ánimo de lucro, mantenida por universidades y organizaciones gubernamentales (sede en Suiza).
- Más de 23 billones de mensajes ADS-B archivados, recogidos por más de 2.000 receptores (mayoritariamente en Europa).
- Los datos ADS-B son exactamente la misma fuente que usan los controladores aéreos y que AENA procesa en su sistema SIRMA.

### Validez para quejas formales
- AENA solo reconoce como oficiales sus propios datos (Webtrak/SIRMA).
- Los datos de OpenSky **no tienen peso legal directo** en una queja formal ante AENA.
- Sin embargo, sirven como **evidencia complementaria e independiente**, especialmente valiosos porque no dependen de AENA en absoluto.

### Valor real del análisis con OpenSky
- Documentación independiente de patrones de tráfico sobre Tres Cantos.
- Evidencia agregada (X aviones/día bajo Y metros durante Z meses) con peso periodístico, político y en redes sociales.
- Es exactamente el tipo de **estudio independiente** que el PSOE de Tres Cantos lleva pidiendo desde 2023 (moción aprobada por unanimidad en noviembre 2023) y que el ayuntamiento no ha ejecutado en más de año y medio.
- Si se cruza con datos oficiales de AENA y se detectan discrepancias, el valor probatorio aumenta enormemente.

---

## 2. Los medidores de ruido (TMR): propiedad y conflicto de interés

### Quién es el dueño
- **Todo el sistema de medición (SIRMA) es propiedad de AENA y gestionado por AENA.**
- Los 22 TMR (Terminales de Monitorado de Ruido) de Barajas son de AENA.
- El software que correlaciona ruido con trayectorias es de AENA.
- Los informes los publica AENA.
- El laboratorio que opera los TMR es **EMS Brüel & Kjaer** (ahora **Envirosuite Ibérica S.A.**), contratado por AENA.

### Conflicto de interés
- **El que genera el ruido es el que lo mide, lo analiza y publica los resultados.**
- No existe supervisión independiente de los datos en bruto.
- Existe acreditación ENAC (Entidad Nacional de Acreditación, reconocida en más de 90 países) según norma ISO 20906, pero esta acreditación certifica que **la metodología de medición es correcta**, no que los datos no puedan ser seleccionados o presentados de forma favorable.

### Implicación para el proyecto
- Los datos de los PDFs de AENA son la única fuente oficial disponible, pero no se pueden considerar 100% imparciales dado el conflicto de interés estructural.
- Un estudio independiente robusto requeriría medidores propios (un sonómetro Clase 1 cuesta entre 2.000 y 5.000 €).

---

## 3. Datos de ruido disponibles públicamente

### Informes mensuales y anuales (PDFs)
- AENA publica informes de ruido en PDF descargables desde su web: https://www.aena.es/en/corporative/environment-sustainability/noise/noise-monitoring-systems/as-madrid-barajas.html
- Contienen niveles LAeq (nivel continuo equivalente) por TMR, desglosados por periodo (día/tarde/noche) y por configuración (norte/sur).
- Disponibles informes mensuales desde al menos 2017 y anuales desde 2016.
- Los informes anuales de 2023, 2024 y 2025 están disponibles.

### Datos diarios
- Los datos diarios de los TMR se publican en la web de AENA en el apartado de mediciones acústicas.
- También accesibles a través del portal **Madrid Insightfull** (https://insightfull-mad.anoms.aero/niveles-de-ruido-diarios/).

### Webtrak
- Muestra niveles de ruido asociados a vuelos individuales en los TMR, pero solo de forma visual (no exportable como datos estructurados).
- Histórico de hasta 45-60 días.
- Datos de ruido disponibles con 24 horas de retraso.

### Limitación clave: no hay API pública
- No existe API para descargar datos brutos de los TMR de forma programática.
- Los datos están en PDFs (requieren scraping/extracción manual) o en Webtrak (solo visual).
- Para el proyecto: sería necesario extraer datos de los PDFs mensuales mediante parsing automatizado o crear manualmente una base de datos a partir de los valores tabulados.

---

## 4. TMR de Tres Cantos: hallazgos relevantes

Tres Cantos tiene **dos TMRs oficiales en la red SIRMA** (datos consolidados a 2026-04-22):

- **TMR-16** ("Tres Cantos-King's College" desde jul 2023; antes "Tres Cantos - Vivero municipal"). Acreditado ENAC cuando cumple disponibilidad, pero **5 de los últimos 7 años tiene sus datos bajo bandera `*` o `*¹`**.
- **TMR-61** ("Tres Cantos Norte"). Instalado en 2022. **Lleva 4 años consecutivos sin acreditación ENAC** (marcado con `*` permanente en todos los informes). No se cita en la correspondencia oficial de AENA con vecinos.

### Historial de ubicaciones del TMR-16

| Periodo | Ubicación | Notas |
|---|---|---|
| ≤ jun 2023 | Tres Cantos - Vivero municipal | Disponibilidad <70% crónica por "ruido de fondo" |
| jul 2023 – ago 2025 | Tres Cantos - King's College | Cambio sin explicación pública |
| ago 2025 – oct 2025 | **retirado** | "Incendio en la localización" (informe anual 2025) |
| nov 2025 – | King's College reinstalado | Disponibilidad <70% en nov |

Ningún documento público de AENA explica el motivo del traslado de jun/jul 2023 ni los detalles del incendio de ago 2025.

### Webtrak ↔ SIRMA
En Webtrak aparecen dos medidores en Tres Cantos:
- Etiquetado "Tres Cantos" (ubicado en Soto de Viñuelas, borde oeste del municipio) → corresponde al **TMR-16** oficial.
- Etiquetado `MAD6112` (al norte de Tres Cantos) → corresponde al **TMR-61** oficial.

Ambos están **en bordes del municipio, no en el núcleo urbano residencial**. Cualquier queja de un vecino del casco interior (p.ej. Avenida Juan Pablo II) está siendo evaluada con datos de medidores en su periferia.

---

## 5. Funcionalidades a desarrollar en el proyecto

### 5.1 Scraping de informes de ruido de AENA
- Descargar automáticamente los PDFs mensuales y anuales desde la web de AENA.
- Extraer las tablas de datos de cada TMR (LAeq Total, LAeq Avión, número de sucesos correlacionados).
- Filtrar datos del TMR16 (Tres Cantos).
- Almacenar en la base de datos SQLite del proyecto.

### 5.2 Análisis histórico del TMR16 (10-15 años)
- Reconstruir la serie histórica de niveles de ruido en Tres Cantos desde ~2010-2012 hasta la actualidad.
- Identificar:
  - Tendencias temporales (¿ha aumentado el ruido con el aumento de tráfico?).
  - Cambios de ubicación del TMR y su efecto en las mediciones.
  - Periodos con disponibilidad de datos inferior al 70%.
  - Periodos sin acreditación ENAC.
  - Correlación entre meses con mayor % de configuración norte y niveles de ruido.
  - Anomalías: periodos donde el tráfico aumentó pero el ruido registrado no.

### 5.3 Cruce de datos OpenSky + AENA
- Para un periodo reciente (últimos 45-60 días, limitado por el histórico de Webtrak):
  - Correlacionar número de vuelos sobre Tres Cantos (OpenSky) con niveles LAeq Avión del TMR16 (AENA).
  - Ejemplo: "El 15 de abril, OpenSky registró 180 vuelos bajo 1.500m sobre Tres Cantos. El TMR16 registró un LAeq Avión día de X dB."
  - Identificar días donde el volumen de tráfico fue alto pero el ruido registrado fue anormalmente bajo (posible indicio de datos inconsistentes).
- Para periodos históricos (meses/años):
  - Cruzar datos mensuales de operaciones de AENA (total despegues 36L) con niveles mensuales del TMR16.
  - Verificar si la relación tráfico-ruido es lineal o presenta quiebres inexplicados.

### 5.4 Informe de hallazgos
- Generar un informe automatizado (markdown o PDF) que resuma:
  - Volumen de tráfico sobre Tres Cantos (datos OpenSky).
  - Niveles de ruido oficiales (datos AENA).
  - Inconsistencias o lagunas detectadas.
  - Comparativa con otros TMR de municipios cercanos (Sanse, Algete) para verificar coherencia.
- Este informe podría adjuntarse a quejas formales o enviarse a medios de comunicación y representantes políticos.

---

## 6. Fuentes de datos y URLs

| Fuente | URL | Tipo |
|--------|-----|------|
| Informes mensuales/anuales ruido AENA | https://www.aena.es/en/corporative/environment-sustainability/noise/noise-monitoring-systems/as-madrid-barajas.html | PDFs descargables |
| Datos diarios TMR (Madrid Insightfull) | https://insightfull-mad.anoms.aero/niveles-de-ruido-diarios/ | Web interactiva |
| Webtrak Madrid-Barajas | https://webtrak.emsbk.com/mad3 | Web interactiva (histórico 45-60 días) |
| OpenSky Network API | https://openskynetwork.github.io/opensky-api/rest.html | REST API |
| OpenSky datos históricos (Trino) | https://opensky-network.org/data/trino | SQL (requiere registro) |
| Estadísticas tráfico AENA | https://www.aena.es/es/estadisticas/informes-mensuales.html | PDFs/web |
| Informes seguimiento ruido (Ministerio Transportes) | https://www.transportes.gob.es | PDFs |

---

## 7. Notas adicionales

- El PSOE de Tres Cantos denunció en julio 2025 que el estudio independiente de ruido aprobado por unanimidad en noviembre 2023 seguía sin ejecutarse más de año y medio después. El ayuntamiento solo daba "respuestas evasivas".
- San Sebastián de los Reyes tiene 5 TMR; Tres Cantos solo tiene 1 (reubicado). Desproporción dado el impacto declarado.
- La empresa que opera los TMR (Envirosuite Ibérica, antes EMS Brüel & Kjaer) trabaja exclusivamente para AENA en el ámbito aeroportuario español.
- Los informes de ruido incluyen una cláusula: "La reproducción total o parcial de este documento no está permitida sin la autorización previa y por escrito del Laboratorio de Monitorado de Envirosuite Ibérica S.A." — esto podría limitar la reproducción directa de tablas en publicaciones, pero no el análisis independiente de los datos.

---

## 8. Hallazgos confirmados (extraídos en abril 2026)

Base de datos: 10 informes anuales AENA (2016-2025), parseados y persistidos en `data/flights.db` (tablas `noise_annual` y `noise_monthly`). Parser en `src/noise_report_parser.py`. Tests en `tests/test_noise_report_parser.py` (22 tests pasando).

### 8.1 Serie histórica TMR-16 — LAeq Avión (dB)

| Año | Día (07-19h) | Tarde (19-23h) | Noche (23-07h) | Validez |
|---|---|---|---|---|
| 2019 | 40,5 | 35,9 | 17,9 | sin ENAC (día) |
| 2020 | 37,7 | 32,2 | **12,8** | oficial |
| 2021 | 38,9 | 31,7 | 18,4 | sin ENAC (día) |
| 2022 | 40,0 | 33,4 | 16,3 | sin ENAC + <70% disp. |
| 2023 Vivero (ene-jun) | 38,6 | 33,2 | 19,7 | sin ENAC + <70% |
| 2023 King's (jul-dic) | **49,0** | **46,3** | **25,5** | sin ENAC + <70% |
| 2024 | 50,1 | 46,8 | 24,2 | oficial |
| 2025 | 50,4 | 47,2 | 25,0 | oficial (valor citado por AENA) |

### 8.2 Hallazgos contundentes

1. **El cambio de ubicación de jul 2023 produjo un salto de +10 dB en LAeq Avión día** (40,0 → 50,1). No es aumento de tráfico, es cambio de sensor. AENA no lo explica en sus informes.
2. **6 de los 7 años previos a 2025 están bajo bandera `*` o `*¹`**: sin ENAC, o <70% de datos válidos, o ambas cosas. El dato "oficial" de 2025 que AENA cita es la excepción, no la regla.
3. **2020 LAeq Avión noche = 12,8 dB.** Por debajo del umbral de audición humana (~10 dB). Dato físicamente imposible publicado oficialmente sin bandera.
4. **TMR-61 Tres Cantos Norte sin ENAC en todos los años desde 2022.** En 2025, los dos TMRs del mismo municipio difieren **+7,6 dB en Avión noche** (TMR-16: 25,0 vs TMR-61: 32,6). AENA cita solo el menor.
5. **TMR-16 entre los peores de la red en calidad de dato.** 5 de 7 años con banderas (71%). Solo TMR-1 La Moraleja está peor (6/7). La mayoría de los otros TMRs no tienen ninguna bandera en el mismo periodo.

### 8.3 Cambio silencioso de metodología entre 2016 y 2019

- **2016 (informe antiguo)**: LAeq medido en solo dos periodos — día (16h) y noche (8h).
- **2019+ (informes Brüel & Kjær / Envirosuite)**: tres periodos según RD 1367/2007 — día (12h, 07-19h), tarde (4h, 19-23h), noche (8h, 23-07h).

El cambio de metodología no se anuncia en los informes y rompe la comparabilidad temporal. Los informes 2017-2018 (formato B&K antiguo) tienen los datos en imágenes y solo publican porcentajes de cumplimiento, no valores absolutos — pendiente de extracción por OCR o desde informes mensuales.

### 8.4 Operaciones sobre la 36L en 2025 (contexto de tráfico)

Del informe anual 2025, sección 2 (usos de pista):
- Despegues por 36L periodo día (07-19h): **57.049** (~156/día)
- Despegues por 36L periodo tarde (19-23h): **12.717** (~35/día)
- Despegues por 36L periodo noche (23-07h): **15.990** (~44/día)
- Configuración norte >80% todo el año (salvo feb-25 y nov-25).

Esta intensidad de tráfico sobre Tres Cantos, sostenida todos los días del año, es el contexto real que AENA no contextualiza al afirmar "se cumplen los objetivos de calidad acústica".

### 8.5 Estado técnico del proyecto

- **Parseado y persistido**: resúmenes anuales 2019-2025 (151 filas, 22 TMRs). Mensuales del TMR-16 y TMR-61 para 2024-2025 (144 filas).
- **Pendiente de extracción**: datos mensuales 2017-2023 (informes mensuales en `doc/aena/informes_mensuales_ruido/`, probable formato Envirosuite con texto extraíble — no verificado aún) y datos 2016 (imágenes, necesita OCR).
- **Pendiente de investigación**:
  - Motivo exacto del traslado TMR-16 jun/jul 2023 (noticias locales, FOI a AENA, actas del ayuntamiento).
  - Naturaleza del "incendio en la localización" de ago 2025 (prensa, bomberos).
  - Por qué TMR-61 nunca ha recibido acreditación ENAC.
  - Coordenadas exactas de TMR-16 y TMR-61 (cruce con catastro / mapa 2025 del informe AENA).
  - Comparativa RD 1367/2007 vs OMS 2018 vs Directiva 2002/49/CE — los umbrales españoles son mucho más laxos; el LAeq Total noche de 43,6 dB ya supera la guía OMS de 40 dB Lnight para ruido aeronáutico.
