# Investigación del ruido aeronáutico sobre Tres Cantos

**Documento vivo.** Es a la vez la memoria de la investigación y la especificación funcional de la app pública que la materializa. Última revisión: 2026-04-23.

## Índice

1. [Misión y audiencia](#1-misión-y-audiencia)
2. [Mapa de la app (spec funcional)](#2-mapa-de-la-app-spec-funcional)
3. [Ejes de la investigación](#3-ejes-de-la-investigación)
4. [Datos: fuentes, cobertura y limitaciones](#4-datos-fuentes-cobertura-y-limitaciones)
5. [Normativa comparada (resumen)](#5-normativa-comparada-resumen)
6. [Historia del TMR y del conflicto (resumen)](#6-historia-del-tmr-y-del-conflicto-resumen)
7. [Stack técnico y despliegue](#7-stack-técnico-y-despliegue)
8. [Hallazgos contundentes a día de hoy](#8-hallazgos-contundentes-a-día-de-hoy)
9. [Preguntas abiertas](#9-preguntas-abiertas)
10. [Referencias y convención de citas](#10-referencias-y-convención-de-citas)

---

## 1. Misión y audiencia

Esta investigación documenta públicamente las **incongruencias, lagunas y opacidades** de los datos oficiales de ruido que AENA publica sobre Tres Cantos (Madrid), partiendo del caso concreto de la pista 36L del Aeropuerto Adolfo Suárez Madrid-Barajas.

El proyecto tiene dos capas:
- **La investigación**: cruce de datos independientes (OpenSky Network, ADS-B) con los datos oficiales de AENA (informes de ruido, Webtrak), análisis contra estándares internacionales (OMS, Directiva 2002/49/CE) y reconstrucción de la historia política y normativa del conflicto.
- **La app**: un dashboard público construido en Streamlit que expone los hallazgos de forma navegable y reproducible, y permite que otras poblaciones afectadas (San Sebastián de los Reyes, Algete, Paracuellos, Soto del Real, Colmenar Viejo) se sumen.

### Audiencia

- **Ciudadanía de Tres Cantos y poblaciones vecinas**: para entender qué dicen (y qué no dicen) los datos de AENA sobre su entorno y poder fundamentar quejas formales.
- **Prensa local y nacional**: material verificable con fuentes primarias citadas para reportajes.
- **Gobierno local y grupos municipales**: evidencia técnica independiente para mociones, recursos, sanciones y para exigir al ayuntamiento la ejecución del estudio de ruido aprobado por unanimidad el 01-12-2023 (ver §6).
- **PA3CA** (Plataforma de Afectados por el Riesgo y el Ruido de los Aviones de Tres Cantos) y asociaciones vecinales.
- **AENA misma**, como recordatorio público de que sus datos están siendo auditados.

### Lo que la app no pretende

- No sustituye a un sonómetro clase 1 acreditado. Los datos crudos son los de AENA y los de OpenSky — nosotros no tomamos medidas propias.
- No tiene valor legal por sí misma en un expediente administrativo (ver §8 sobre el papel de OpenSky frente a AENA).
- No es una plataforma reivindicativa con consignas; es una herramienta de análisis y transparencia. Las conclusiones se extraen de los datos, no al revés.

---

## 2. Mapa de la app (spec funcional)

La app es un dashboard multipágina. Cada página responde a una pregunta concreta del visitante y enlaza con las demás.

Estado de cada página:
- ✅ **Existe**: ya funciona en el código actual.
- 🔨 **Por construir**: datos disponibles, falta la vista Streamlit.
- 🔍 **Requiere investigación previa**: faltan datos o hechos por confirmar antes de poder construir la página.

### 2.1 Home / landing 🔨

**Objetivo**: que un visitante sin contexto entienda en 60 segundos qué pasa con el ruido de los aviones sobre Tres Cantos.

**Contenido**:
- Hero con los 3 hallazgos más fuertes (ver §8), cada uno en una tarjeta grande: cifra + titular + link a la página que lo desarrolla.
- Párrafo de contexto (2-3 líneas) sobre qué es Barajas 36L y por qué afecta a Tres Cantos.
- Barra de navegación a todas las secciones.
- Botón prominente de contacto (§2.12).

**Fuentes**: §8 de este documento; `data/flights.db` para cifras recientes.

### 2.2 Vuelos en tiempo cuasi-real (OpenSky) ✅

**Objetivo**: mostrar el tráfico real sobre Tres Cantos con datos independientes de AENA.

**Contenido**: el dashboard actual de `app.py` — mapa con trayectorias, KPIs, histograma de altitudes, heatmap hora × día, evolución mensual, scatter hora-altitud.

**Fuentes**: `data/flights.db` tablas OpenSky; descarga vía `src/collector.py`.

**Estado**: funciona; se integrará como una sección más del dashboard multipágina sin reescribir la lógica.

### 2.3 Serie histórica mensual TMR-16 y TMR-61 🔨

**Objetivo**: permitir al visitante explorar mes a mes cómo han evolucionado los niveles de ruido en los dos medidores oficiales de Tres Cantos.

**Contenido**:
- Selector vertical de años (2015, 2016, …, 2026).
- Al elegir un año, se muestran dos gráficos de barras interactivos:
  - **TMR-16**: 12 meses × 3 periodos (día 07-19h / tarde 19-23h / noche 23-07h), con toggle entre **LAeq Total** y **LAeq Avión**.
  - **TMR-61**: idem para los años en que hay dato (≥2022).
- Líneas horizontales con los umbrales RD 1367/2007, OMS 2018 y Directiva 2002/49/CE (ver §5).
- Banderas visuales en barras sin ENAC (`*`) o con disponibilidad <70% (`¹`).
- Nota honesta de cobertura: **huecos 2015-2023 explícitos** con la causa (datos en imágenes, OCR en curso; formato B&K antiguo sin valores absolutos).

**Fuentes**: tabla `noise_monthly` en `data/flights.db`, alimentada por `src/noise_report_parser.py` y `scripts/ocr_tmr16_monthly.py`.

### 2.4 Serie anual 2015-2025 🔨

**Objetivo**: visión de conjunto con anotaciones históricas.

**Contenido**:
- 4 gráficas de líneas interactivas:
  - LAeq **Total** TMR-16 (día / tarde / noche)
  - LAeq **Avión** TMR-16 (día / tarde / noche)
  - LAeq **Total** TMR-61 (día / tarde / noche)
  - LAeq **Avión** TMR-61 (día / tarde / noche)
- Marcadores verticales sobre eventos: **traslado TMR-16 jul 2023** (Vivero → King's College), **incendio ago 2025** (TMR retirado), **reinstalación nov 2025**, **entrada en servicio del radial 322** (2005), **apertura Terminal 4** (2006).
- Líneas horizontales de umbrales RD/OMS/UE.
- Toggle: "mostrar solo años con acreditación ENAC" / "incluir datos bajo bandera `*` o `¹`".
- Comentario al lado de cada gráfica con la interpretación (p.ej. "+10 dB LAeq Avión día entre 2022 y 2024 se explica por el cambio de ubicación").

**Fuentes**: tabla `noise_annual` en `data/flights.db`.

### 2.5 Historia del TMR (mapa + timeline) 🔨

**Objetivo**: mostrar dónde han estado los sensores oficiales de AENA en Tres Cantos.

**Contenido**:
- Mapa Folium con marcadores de las ubicaciones conocidas del TMR-16 (Vivero municipal, King's College) y del TMR-61 (zona norte).
- Timeline vertical con los hitos: instalación, traslados, retirada por incendio, reinstalaciones.
- Nota explícita: ambos TMRs están **en los bordes del municipio**, no en el núcleo urbano denso.

**Fuentes**: `doc/historia_tmr.md`. Coordenadas GPS exactas pendientes de confirmar (ver §9).

### 2.6 Normativa y umbrales comparados 🔨

**Objetivo**: responder "¿se está cumpliendo la ley? ¿qué dicen las recomendaciones internacionales?".

**Contenido**:
- Explicación corta de cada norma: qué mide, quién la hace, qué valor tiene (obligatorio / recomendación).
- Tabla comparativa: **RD 1367/2007** (España) vs **OMS 2018** vs **Directiva 2002/49/CE** vs **Francia** (Arrêté PEB) vs **Alemania** (FluLärmG) vs **Reino Unido** (CAA Night Noise Restrictions) vs **Países Bajos** (Schiphol Lden).
- Evaluación de Tres Cantos contra cada umbral (datos 2024-2025) con código de color: cumple / excede / al borde.
- Link al BOE del RD 1367/2007 (BOE-A-2007-18397).
- Breve explicación del **ICAO Balanced Approach** (Doc 9829): no fija umbrales numéricos, define 4 pilares de gestión (reducción en la fuente, planificación del suelo, procedimientos operacionales, restricciones).
- Qué mide AENA pero **no publica**: LAmax por evento, SEL, Lden/Lnight estandarizados, distribución por percentiles, número de eventos >65/70/80 dB (los publican Heathrow y Schiphol).

**Fuentes**: `doc/normativa_comparada.md` (se resume aquí y se referencia el detalle).

### 2.7 Trayectorias de salida configuración norte 🔍

**Objetivo**: mostrar por dónde salen los aviones cuando Barajas opera en configuración norte, qué poblaciones sobrevuelan, y proponer una discusión sobre alternativas.

**Contenido**:
- Mapa con los radiales de salida:
  - **36L**: radial 322 sobre Tres Cantos y Soto de Viñuelas (documentado).
  - **36R**: radial a confirmar (probablemente 317-321, por cartas AIP de ENAIRE).
- Tabla de poblaciones afectadas por cada radial.
- Comparativa de operaciones: despegues/año por 36L vs 36R — la usuaria observa en los informes que 36R tiene más despegues que 36L; hay que confirmarlo con la sección 2 "Usos de pista" de los informes anuales.
- Contexto histórico: antes de la ampliación de Barajas (2005) había una única salida norte; la duplicación a dos pistas paralelas obliga a separar las trayectorias inmediatamente tras el despegue, lo que impide que los aviones ganen altura suficiente antes de sobrevolar las poblaciones.
- Discusión: **¿tendría sentido centralizar los despegues norte en un solo radial con mayor altitud mínima?** — una propuesta técnica que sirva de partida para exigir estudios de viabilidad a AENA.

**Estado**: requiere (a) confirmar radial 36R en AIP, (b) extraer tablas de usos de pista de los informes anuales AENA.

**Fuentes**: [AIP ENAIRE](https://aip.enaire.es) (SID Madrid-Barajas), informes anuales de ruido AENA §2.

### 2.8 Altitud y percepción del ruido 🔍

**Objetivo**: explicar a partir de qué altitud el ruido aeronáutico deja de ser molesto y contrastar con la altitud real de paso sobre Tres Cantos.

**Contenido**:
- Resumen de la literatura: estudios de FAA, EASA e ICAO sobre relación altitud-percepción.
- Valores orientativos típicos: por debajo de **1.000-1.500 m** el ruido es claramente molesto; entre **1.500-3.000 m** es perceptible; por encima de **3.000 m** típicamente ambiental (depende del tipo de avión, potencia en el despegue, condiciones atmosféricas).
- Distribución real de altitudes sobre Tres Cantos (datos OpenSky, ya en `app.py`): mostrar qué porcentaje de vuelos pasa por debajo de cada umbral.
- Referencia a la norma aérea de altitud mínima sobre zonas pobladas.

**Estado**: requiere recopilar referencias bibliográficas (ICAO Doc 9829, estudios FAA sobre noise abatement procedures) y añadir el cruce con OpenSky.

### 2.9 Estudios epidemiológicos y salud 🔍

**Objetivo**: mostrar que el ruido por encima de los umbrales OMS tiene efectos documentados sobre la salud — no es una preocupación estética.

**Contenido**:
- OMS 2018 *Environmental Noise Guidelines for the European Region*: metodología y recomendaciones para ruido aeronáutico (<45 dB Lden, <40 dB Lnight).
- **HYENA** (Hypertension and Exposure to Noise near Airports, 2008): estudio europeo multinacional — asocia ruido aeronáutico nocturno con hipertensión.
- **DEBATS** (Francia, 2013-): efectos cardiovasculares cerca de aeropuertos franceses.
- **NORAH** (Alemania, Frankfurt, 2011-2015): sueño, cognición infantil, salud mental.
- Conclusión: la evidencia científica es sólida y los valores de Tres Cantos superan los umbrales OMS, especialmente de noche (ver §5 y `normativa_comparada.md`).

**Estado**: requiere recopilar bibliografía y DOIs.

### 2.10 Historia política y decisión Barajas-vs-Campo-Real 🔍

**Objetivo**: explicar públicamente por qué se amplió Barajas (Terminal 4 + segunda pareja de pistas 18L/36R y 18R/36L) en vez de construir el aeropuerto alternativo de Campo Real, y qué consecuencias tuvo para el norte de Madrid.

**Contenido**:
- Contexto 1995-2000: saturación prevista de Barajas, alternativas estudiadas (Campo Real, ampliación in situ).
- Decisión: quién la tomó, cuándo, con qué documentación oficial (Plan Director de Barajas, Declaración de Impacto Ambiental).
- Impacto: ruta 322 (2005), Terminal 4 (2006), multiplicación del tráfico sobre Tres Cantos.
- Fuentes primarias a consultar: Plan Director (Ministerio Fomento), DIA, Boletín Oficial de las Cortes Generales 1998-2001, hemerotecas de El País, ABC, El Mundo, El Economista.
- Recursos judiciales interpuestos por ayuntamientos afectados (Tres Cantos presentó alegaciones en 2007 — ver `historia_tmr.md` §3).

**Estado**: requiere investigación hemerográfica y documental sustancial.

### 2.11 Metodología y reproducibilidad 🔨

**Objetivo**: que cualquiera pueda verificar, replicar o extender el análisis.

**Contenido**:
- Cómo se obtienen los datos de OpenSky (Trino SQL).
- Cómo se parsean los informes AENA (`src/noise_report_parser.py`, `scripts/ocr_tmr16_monthly.py`).
- Cómo se calculan Lden y Lnight (`src/noise_metrics.py`).
- Enlace al repo en GitHub.
- Licencia del código y condiciones de uso de los datos AENA (cláusula Envirosuite — ver §4).

### 2.12 Contacto y extensión 🔨

**Objetivo**: recibir mensajes de otros afectados y sumar poblaciones a la investigación.

**Contenido**:
- Formulario de contacto (Formspree gratuito hasta 50 envíos/mes, o mailto directo como fallback).
- Sección "¿Eres de Sanse, Algete, Paracuellos, Soto del Real, Colmenar Viejo?" con invitación a compartir experiencias.
- Cómo sumarse a una queja conjunta.
- Enlaces a PA3CA y a asociaciones vecinales locales.
- Disclaimer legal: los mensajes no se hacen públicos sin consentimiento.

---

## 3. Ejes de la investigación

Traducción de los objetivos del proyecto en preguntas concretas que la app responde. Cada eje enlaza a la(s) página(s) donde vive la respuesta.

1. **¿Dónde están y dónde han estado los TMR de Tres Cantos?** → §2.5. **Respuesta rápida**: TMR-16 estuvo en el **Vivero municipal hasta jun 2023**, se trasladó al **King's College (Soto de Viñuelas)** en jul 2023, fue retirado por el incendio de ago 2025 y reinstalado en King's College en nov 2025. TMR-61 "Tres Cantos Norte" fue instalado en 2022, sin acreditación ENAC desde entonces.

2. **¿Cómo evoluciona el ruido año a año y mes a mes?** → §2.3 + §2.4.

3. **¿Qué son los "sucesos" que aparecen en los informes AENA?** → §2.4 (nota metodológica). **Respuesta rápida**: son **eventos acústicos que el sistema SIRMA correlaciona con el paso de un avión** (vía cruce con las trayectorias de Webtrak). **No implican superación de umbral**; son conteos de intrusiones sonoras atribuibles a aviación. Los informes anuales AENA publican el total anual de sucesos por TMR, pero **no cuántos superan 65, 70 u 80 dB** — métricas que sí publican Heathrow y Schiphol (ver `normativa_comparada.md` §4).

4. **¿Está el RD 1367/2007 publicado en el BOE? ¿Qué dicen OMS, ICAO y otros países europeos?** → §2.6. **Respuesta rápida**: sí, BOE núm. 254 de 23/10/2007 (BOE-A-2007-18397). OMS 2018 recomienda <45 dB Lden y <40 dB Lnight para ruido aeronáutico. ICAO Balanced Approach no fija números. Francia, Alemania, UK y Países Bajos usan Lden/Lnight con umbrales intermedios entre OMS y España.

5. **¿Hay estudios sobre el impacto del ruido por encima de los umbrales?** → §2.9. **Respuesta rápida**: sí, abundantes. La OMS 2018 sintetiza la evidencia: hipertensión, enfermedad cardiovascular, alteraciones del sueño, deterioro cognitivo en niños. Estudios clave: HYENA (Europa), DEBATS (Francia), NORAH (Alemania).

6. **¿Por dónde despegan los aviones en configuración norte? ¿Más por 36L o por 36R?** → §2.7. Hipótesis a confirmar contra informes AENA: **36R tiene más despegues que 36L** (observación de la usuaria); radial 36L = 322, radial 36R pendiente de confirmar en AIP.

7. **¿A partir de qué altitud el ruido aeronáutico deja de molestar?** → §2.8.

8. **¿Por qué se amplió Barajas en vez de construir Campo Real?** → §2.10.

9. **¿Cómo se pueden sumar otras poblaciones afectadas?** → §2.12.

---

## 4. Datos: fuentes, cobertura y limitaciones

### 4.1 Fuentes oficiales AENA

| Fuente | URL | Tipo |
|--------|-----|------|
| Informes mensuales/anuales de ruido AENA | https://www.aena.es/en/corporative/environment-sustainability/noise/noise-monitoring-systems/as-madrid-barajas.html | PDFs descargables |
| Datos diarios TMR (Madrid Insightfull) | https://insightfull-mad.anoms.aero/niveles-de-ruido-diarios/ | Web interactiva (no exportable) |
| Webtrak Madrid-Barajas | https://webtrak.emsbk.com/mad3 | Web interactiva, histórico 45-60 días |
| Estadísticas tráfico AENA | https://www.aena.es/es/estadisticas/informes-mensuales.html | PDFs/web |
| Informes seguimiento ruido (Ministerio Transportes) | https://www.transportes.gob.es | PDFs |

### 4.2 Fuentes independientes

| Fuente | URL | Tipo |
|--------|-----|------|
| OpenSky Network REST API | https://openskynetwork.github.io/opensky-api/rest.html | REST API, ~100 llamadas/día sin registro |
| OpenSky datos históricos Trino | https://opensky-network.org/data/trino | SQL, requiere registro |
| Cartas AIP ENAIRE | https://aip.enaire.es | Procedimientos de salida, radiales, altitudes mínimas |

### 4.3 Estado de extracción de datos

La tabla siguiente es la **fuente de verdad** sobre qué datos están disponibles en `data/flights.db` para alimentar las páginas §2.3 y §2.4.

| Año | Anual TMR-16 | Anual TMR-61 | Mensual TMR-16 | Mensual TMR-61 |
|---|---|---|---|---|
| 2015 | 🔴 (solo % cumplimiento) | — (no existe) | 🔴 (formato B&K) | — |
| 2016 | 🔴 (solo % cumplimiento) | — | 🔴 (B&K) | — |
| 2017 | 🟡 (OCR pendiente) | — | 🟡 (B&K, parser específico) | — |
| 2018 | 🟡 (OCR pendiente) | — | 🟡 (OCR pendiente) | — |
| 2019 | 🟢 | — | 🟡 (OCR pendiente) | — |
| 2020 | 🟢 | — | 🟡 | — |
| 2021 | 🟢 | — | 🟡 | — |
| 2022 | 🟢 | 🟢 | 🟡 | 🟡 |
| 2023 | 🟢 (partida Vivero/King's) | 🟢 | 🟡 pre-jul; 🟢 post-jul | 🟢 parcial |
| 2024 | 🟢 | 🟢 | 🟢 | 🟢 |
| 2025 | 🟢 | 🟢 | 🟢 | 🟢 |
| 2026 (en curso) | — | — | 🟢 parcial | 🟢 parcial |

Leyenda: 🟢 extraído y persistido · 🟡 en imágenes, OCR en curso · 🔴 solo % cumplimiento (formato B&K antiguo).

### 4.4 Qué contiene cada informe

**Mensuales** (`doc/aena/informes_mensuales_ruido/{YYYY}/{YYYY}-{MM}_informe_ruido.pdf`):
1. "Informe ejecutivo" (págs. 3-5): texto extraíble con `horas_sur`, `% horas Sur`, `% operaciones Sur`, `% acumulado anual`. Parser: `scripts/extract_config_sur.py`.
2. Gráficos por TMR (págs. ~40-43): **embebidos como imagen**. Requieren OCR. Cada gráfico contiene una serie **rolling de 13 meses**, por lo que un mismo (año, mes) aparece en hasta 13 informes distintos — redundancia explotable para validación cruzada.

**Anuales** (`doc/aena/informes_anuales_ruido/{YYYY}_informe_anual.pdf`):
- Resumen anual por TMR (~pág. 35): texto extraíble.
- Valores mensuales por TMR: solo en informes 2024+ (anteriores son imágenes).
- Parser: `src/noise_report_parser.py`.

### 4.5 Limitaciones y caveats

- **No existe API pública de AENA**. PDFs o nada.
- **Cláusula de reproducción** en todos los PDFs: *"La reproducción total o parcial de este documento no está permitida sin la autorización previa y por escrito del Laboratorio de Monitorado de Envirosuite Ibérica S.A."* No reproducimos PDFs enteros; analizamos datos bajo amparo de la **Ley 27/2006 de acceso a la información ambiental** y del **art. 32 LPI** (cita con fines de investigación y crítica).
- **Banderas en tablas**:
  - `*` o `*¹`: datos no amparados por acreditación ENAC. TMR-61 Tres Cantos Norte va siempre con `*`.
  - `¹`: disponibilidad <70%, típicamente justificada por "ruido de fondo".
- **Webtrak** solo guarda 45-60 días. Los datos de ruido salen con 24h de retraso.
- **Conflicto de interés estructural**: todo el sistema SIRMA (sensores, software de correlación, informes) es propiedad de AENA y operado por Envirosuite Ibérica bajo contrato con AENA. *El que genera el ruido es el que lo mide y lo publica*. La acreditación ENAC certifica que la metodología es correcta, no que los datos publicados sean representativos o completos.

---

## 5. Normativa comparada (resumen)

Detalle completo en [`normativa_comparada.md`](normativa_comparada.md). Tabla de umbrales (zona residencial, ruido aeronáutico):

| Norma | Indicador | Umbral | Estatus |
|---|---|---|---|
| **RD 1367/2007** (España, BOE-A-2007-18397) | LAeq Ld (07-19h) | 65 dB | Obligatorio |
| | LAeq Le (19-23h) | 65 dB | Obligatorio |
| | LAeq Ln (23-07h) | 55 dB | Obligatorio |
| **OMS 2018** (aircraft) | Lden | 45 dB | Strong recommendation |
| | Lnight | 40 dB | Strong recommendation |
| **Directiva 2002/49/CE** | Lden | 55 dB | Umbral de reporte obligatorio |
| | Lnight | 50 dB | Umbral de reporte obligatorio |

Con datos oficiales AENA 2025 para TMR-16:
- **Cumple** RD 1367/2007 (55,1 / 49,9 / 43,6 dB vs 65/65/55).
- **Excede** la recomendación OMS 2018 Lnight **en los 7 años analizados** (margen 2,1-10,1 dB).
- **Al borde** del umbral de reporte de la Directiva 2002/49/CE en varios años.

El RD español es **~20 dB más laxo que la OMS**. Cumplir el RD no equivale a proteger la salud. AENA afirma cumplimiento citando solo el RD, sin mencionar OMS ni Directiva EU.

**Lo que AENA mide pero no publica**: LAmax por evento, SEL, Lden/Lnight estandarizados, percentiles, número de eventos >65/70/80 dB por día. Heathrow y Schiphol sí los publican.

**ICAO Balanced Approach** (Doc 9829): no fija umbrales numéricos; define cuatro pilares de gestión del ruido (reducción en la fuente, planificación del suelo, procedimientos operacionales, restricciones). Aplicable a Tres Cantos como argumento para exigir **procedimientos operacionales** (altitud mínima, centralización de radiales) y **planificación del suelo** (ubicación de nuevos TMR en casco urbano).

---

## 6. Historia del TMR y del conflicto (resumen)

Detalle completo en [`historia_tmr.md`](historia_tmr.md). Hitos principales:

- **2005**: entra en funcionamiento el radial 322 (pista 36L), ruta que sobrevuela Tres Cantos y el ZEPA.
- **2006**: apertura Terminal 4 de Barajas; los movimientos sobre Tres Cantos se multiplican.
- **2007**: Tres Cantos presenta alegaciones al mapa estratégico de ruido (Directiva 2002/49/CE).
- **sep 2018**: Envirosuite Ibérica obtiene acreditación ENAC (ISO 20906). Datos previos quedan expresamente "no amparados por ENAC".
- **ene 2020**: AENA se compromete a un "sonómetro temporal" en zona norte de Tres Cantos tras quejas vecinales.
- **2022**: aparece el TMR-61 "Tres Cantos Norte", sin acreditación ENAC (sigue así en 2026, 4 años después).
- **jun/jul 2023**: TMR-16 se traslada del Vivero municipal al King's College. AENA no publica motivo. Salto de +10 dB en LAeq Avión día.
- **01-dic-2023**: Pleno de Tres Cantos aprueba **por unanimidad** la moción del PSOE para un estudio independiente de ruido con plazo de 6 meses y cláusula de expediente sancionador si las mediciones no concuerdan con las de AENA.
- **sep 2024, jul 2025**: PSOE denuncia que el estudio sigue sin ejecutarse.
- **ago 2025**: incendio forestal de Tres Cantos (1.968 ha); TMR-16 retirado.
- **nov 2025**: TMR-16 reinstalado en King's College, con disponibilidad <70%.
- **abr 2026**: queja formal 2026/MA000106 de la autora. AENA responde citando solo RD 1367/2007 y solo TMR-16 (omite TMR-61 pese a tener valores ~7 dB mayores).
- **abr 2026**: el estudio municipal sigue sin ejecutarse (2 años y 4 meses tras aprobación unánime).

### 6.1 Decisión Barajas-vs-Campo-Real (pendiente de investigar)

Esta sección del documento se ampliará con la investigación de §2.10. Pistas:
- Plan Director de Barajas (~2000, Ministerio Fomento).
- Declaración de Impacto Ambiental de la ampliación.
- Debates parlamentarios 1997-2001 (BOCG).
- Hemerotecas: El País, ABC, El Mundo.
- Posibles solicitudes vía Ley 19/2013 (transparencia) y Ley 27/2006 (medio ambiente).

---

## 7. Stack técnico y despliegue

### 7.1 Decisión actual (V1)

- **Frontend**: Streamlit multipágina (`st.navigation` / `pages/`).
- **Visualización**: Plotly (interactividad), Folium (mapas), `streamlit-folium`.
- **Datos**: SQLite (`data/flights.db`).
- **Backend de datos**: scripts Python en `src/` y `scripts/`.
- **Extracción AENA**: `src/noise_report_parser.py` + `scripts/ocr_tmr16_monthly.py` (OCR de gráficos en imagen).
- **Formulario contacto**: Formspree (gratuito hasta 50 envíos/mes) o mailto como fallback.
- **Despliegue**: Streamlit Community Cloud (gratuito). Secrets en la UI de Streamlit Cloud, no en el repo.

### 7.2 Migración futura (V2)

Se migrará a **Next.js (frontend) + FastAPI (API Python)** cuando se cumpla al menos una de estas condiciones:
- El contenido está estable y se quiere mejorar SEO + URLs limpias (ej. `/tmr16/2024`, `/normativa/oms`).
- Se quieren previews ricos de Twitter/X y Open Graph para compartir en redes.
- El formulario de contacto necesita lógica más compleja (autenticación, moderación).
- La app escala a varias poblaciones y se necesita routing más serio.

**Principio rector**: el contenido manda, no la infraestructura. No se migra hasta que el contenido justifique el coste de reescribir el frontend.

### 7.3 Dependencias clave

Ver `pyproject.toml`. Núcleo: `streamlit`, `plotly`, `folium`, `streamlit-folium`, `pandas`, `traffic` (OpenSky), `pdfplumber` + `pymupdf` (PDFs AENA), `pytesseract` (OCR), `pytest`.

---

## 8. Hallazgos contundentes a día de hoy

Base: 10 informes anuales AENA (2016-2025) + informes mensuales 2024-2026, parseados y persistidos en `data/flights.db` (tablas `noise_annual` y `noise_monthly`). Parser: `src/noise_report_parser.py`. Tests: `tests/test_noise_report_parser.py` (22 pasando).

### 8.1 Los 3 hallazgos más fuertes (para el Home)

1. **Salto de +10 dB en LAeq Avión día entre 2022 y 2024** (40,0 → 50,1 dB en TMR-16). No es aumento de tráfico: es el cambio silencioso de ubicación del sensor en jul 2023 (Vivero → King's College). AENA no lo explica en sus informes.
2. **El LAeq Total nocturno supera la recomendación OMS 2018 en los 7 años analizados** (2019-2025), con margen de 2,1 a 10,1 dB. El RD español (55 dB Ln) se cumple, pero es ~15 dB más laxo que la OMS (40 dB Lnight). Cumplir el RD no significa proteger la salud.
3. **El estudio independiente de ruido, aprobado por unanimidad en pleno de Tres Cantos el 01-dic-2023, sigue sin ejecutarse 2 años y 4 meses después**. El pleno incluía cláusula explícita de expediente sancionador si las mediciones discrepasen con AENA. Gobierno PP-Unión Santo Domingo ha dado solo *"respuestas evasivas"* según denuncia del PSOE local.

### 8.2 Serie histórica TMR-16 — LAeq Avión (dB)

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

### 8.3 Hallazgos adicionales

- **6 de los 7 años previos a 2025 están bajo bandera `*` o `*¹`**: sin ENAC, o <70% de datos válidos, o ambas. El dato "oficial" de 2025 que AENA cita es la excepción, no la regla.
- **2020 LAeq Avión noche = 12,8 dB**: por debajo del umbral de audición humana (~10 dB). Dato físicamente sospechoso publicado oficialmente sin bandera.
- **TMR-61 sin ENAC todos los años desde 2022**. En 2025, los dos TMRs del mismo municipio difieren **+7,6 dB en LAeq Avión noche** (TMR-16: 25,0 vs TMR-61: 32,6). AENA cita solo el menor.
- **TMR-16 entre los peores de la red en calidad de dato**: 5 de 7 años con banderas (71%). Solo TMR-1 La Moraleja está peor. La mayoría de los TMRs no tienen ninguna bandera en ese periodo.

### 8.4 Cambio silencioso de metodología 2016 → 2019

- **2016** (formato B&K antiguo): LAeq en dos periodos — día (16h) y noche (8h).
- **2019+** (Envirosuite, conforme RD 1367/2007): tres periodos — día (12h, 07-19h), tarde (4h, 19-23h), noche (8h, 23-07h).

El cambio no se anuncia en los informes y rompe la comparabilidad temporal. Los informes 2017-2018 (B&K antiguo) tienen los datos en imágenes y solo publican porcentajes de cumplimiento, no valores absolutos — pendiente de OCR o extracción desde informes mensuales.

### 8.5 Operaciones sobre la 36L en 2025 (contexto de tráfico)

Del informe anual 2025 §2 (usos de pista):
- Despegues 36L día (07-19h): **57.049** (~156/día).
- Despegues 36L tarde (19-23h): **12.717** (~35/día).
- Despegues 36L noche (23-07h): **15.990** (~44/día).
- Configuración norte >80% todo el año (salvo feb-25 y nov-25).

Esta intensidad sostenida todos los días del año es el contexto real que AENA no contextualiza al afirmar *"se cumplen los objetivos de calidad acústica"*.

### 8.6 Validez de OpenSky frente a AENA

- OpenSky usa **ADS-B**, la misma fuente que usan los controladores aéreos y el sistema SIRMA de AENA.
- AENA solo reconoce como oficiales sus propios datos; OpenSky **no tiene peso legal directo** en una queja administrativa formal.
- Sin embargo sirve como **evidencia complementaria e independiente** con peso periodístico, político y en redes: "X aviones/día bajo 1.500 m durante Z meses".
- Si se cruza con datos oficiales AENA y se detectan discrepancias, el valor probatorio aumenta.

---

## 9. Preguntas abiertas

Cada pregunta es un trabajo pendiente de investigación; va a alimentar una subsección del documento o una página de la app a medida que se resuelva.

| # | Pregunta | Fuente candidata | Destino |
|---|---|---|---|
| 1 | Radial exacto de salida 36R en config. norte | [AIP ENAIRE](https://aip.enaire.es) — SID Madrid-Barajas | §2.7 |
| 2 | ¿36R > 36L en despegues/año? | Informes anuales AENA §2 "Usos de pista" | §2.7 |
| 3 | Altitud umbral de no-molestia para aeronaves comerciales | ICAO Doc 9829, estudios FAA/EASA sobre noise abatement | §2.8 |
| 4 | URL BOE directa del RD 1367/2007 | BOE.es — BOE-A-2007-18397 | §5 |
| 5 | Umbrales en Francia, Alemania, UK, Países Bajos | DGAC (Arrêté PEB), UBA (FluLärmG), CAA UK, ILT Países Bajos | §2.6 |
| 6 | Estudios epidemiológicos (HYENA, DEBATS, NORAH) | PubMed / DOI | §2.9 |
| 7 | Fuente primaria decisión Barajas-vs-Campo-Real | Plan Director Barajas (Fomento), DIA, BOCG 1998-2001 | §2.10 |
| 8 | Hemerografía del debate 1998-2006 | Hemerotecas El País, ABC, El Mundo, El Economista | §2.10 |
| 9 | Coordenadas GPS exactas TMR-16 y TMR-61 | Webtrak + FOI a AENA (Ley 27/2006) | §2.5 |
| 10 | Motivo del traslado TMR-16 jun/jul 2023 | FOI a AENA, prensa local, actas ayuntamiento | §6 |
| 11 | Naturaleza del "incendio en la localización" ago 2025 (impacto operativo en el TMR) | Prensa local, bomberos, comunidad King's College | §6 |
| 12 | Por qué TMR-61 nunca ha recibido acreditación ENAC en 4 años | Solicitud formal a Envirosuite / AENA | §6 |
| 13 | Comparativa completa RD vs Directiva 2002/49/CE sobre umbrales de **mapeo** | Transposición al ordenamiento español | §5 |
| 14 | ¿Existe un tercer sonómetro planificado para el casco urbano de Tres Cantos? | Acta concejalía Medio Ambiente 2020+ | §2.5 |

---

## 10. Referencias y convención de citas

### 10.1 Convención

- **Toda cifra, afirmación o cita tiene footnote con URL a fuente original.**
- Fuente PDF local del repo → link al PDF en GitHub (`doc/aena/informes_anuales_ruido/...`).
- Fuente legal → enlace a BOE.
- Fuente periodística → enlace al medio.
- Fuente académica → enlace a DOI.
- Fuente oficial sin URL estable (ej. informe interno, FOI respondida) → PDF en el repo con nombre de fichero descriptivo y fecha.

### 10.2 Referencias clave

- **Real Decreto 1367/2007**, de 19 de octubre, por el que se desarrolla la Ley 37/2003 del Ruido — BOE núm. 254 de 23/10/2007, [BOE-A-2007-18397](https://www.boe.es/eli/es/rd/2007/10/19/1367).
- **Directiva 2002/49/CE** del Parlamento Europeo y del Consejo, de 25 de junio de 2002, sobre evaluación y gestión del ruido ambiental.
- **OMS (2018)**, *Environmental Noise Guidelines for the European Region*, ISBN 978 92 890 5356 3.
- **Ley 37/2003**, de 17 de noviembre, del Ruido.
- **Ley 27/2006**, de 18 de julio, de acceso a la información ambiental.
- **Ley 19/2013**, de 9 de diciembre, de transparencia, acceso a la información pública y buen gobierno.
- **ICAO Doc 9829** — *Guidance on the Balanced Approach to Aircraft Noise Management*.
- Informes anuales de ruido de Madrid-Barajas, años 2016-2025 (Envirosuite Ibérica S.A., antes EMS Brüel & Kjær), en `doc/aena/informes_anuales_ruido/`.
- Informes mensuales de ruido de Madrid-Barajas, en `doc/aena/informes_mensuales_ruido/`.
- Respuesta de AENA de 16-04-2026 (expediente SO/MA/SBP 2026001488) a la queja 2026/MA000106, en `doc/queja_aena/`.

### 10.3 Cronología periodística

- [Telemadrid, 28-01-2020 — "Aena medirá el ruido que causan los aviones en la zona norte de Tres Cantos"](https://www.telemadrid.es/noticias/madrid/Aena-medira-causan-aviones-Cantos-0-2199380052--20200128113410.html).
- [Revista 360y5, dic-2023 — aprobación moción pleno Tres Cantos](https://360y5.es/el-pleno-del-ayuntamiento-aprueba-realizar-un-estudio-de-medicion-de-ruido-producido-por-los-aviones-que-sobrevuelan-tres-cantos/).
- [Madrid Norte 24 horas, 03-09-2024 — PSOE lleva al pleno el problema del ruido](https://www.madridnorte24horas.com/articulo/tres-cantos/el-psoe-de-tres-cantos-llevara-de-nuevo-al-pleno-el-problema-del-ruido-de-los-aviones/20240903115531112159.html).
- [Madrid Norte 24 horas, 15-07-2025 — PSOE exige estudio independiente](https://www.madridnorte24horas.com/articulo/tres-cantos/psoe-tres-cantos-exige-ayuntamiento-estudio-independiente-ruido-aviones/20250715111322120513.html).
- [El Economista, 2007 — Tres Cantos presenta alegaciones](https://www.eleconomista.es/empresas-finanzas/noticias/246196/07/07/Tres-Cantos-presentara-alegaciones-al-mapa-del-ruido-elaborado-por-AENA.html).
- [Pressnorte, 12-08-2025 — King's College Soto de Viñuelas tras el incendio](https://www.pressnorte.com/kings-college-soto-vinuelas-inicio-curso-incendio-20250812/).
- [Comunidad de Madrid, 28-11-2025 — Agencia 112 reconocida por King's College tras el incendio](https://www.comunidad.madrid/noticias/2025/11/28/agencia-seguridad-emergencias-madrid-112-reconocida-kings-college-school-su-actuacion-incendio-tres-cantos).
- [Blog PA3CA — Ruido de aviones en Tres Cantos](https://ruidotrescantos.blogspot.com/).

### 10.4 Documentos internos del proyecto

- [`normativa_comparada.md`](normativa_comparada.md) — detalle de la comparativa RD 1367 / OMS / Directiva EU.
- [`historia_tmr.md`](historia_tmr.md) — cronología completa del TMR y del conflicto político.
- [`analisis_config_sur_vs_tmr16.md`](analisis_config_sur_vs_tmr16.md) — correlación configuración sur vs niveles TMR-16.

Datos y cálculos reproducibles: `src/noise_metrics.py` + `data/flights.db` (tablas `noise_annual`, `noise_monthly`, `overflights`).
