# Comparativa normativa del ruido aeronáutico: RD 1367/2007 vs OMS 2018 vs Directiva 2002/49/CE

Este documento confronta los umbrales usados por AENA para dictaminar el cumplimiento del ruido en Tres Cantos con las dos referencias internacionales más extendidas: las guías OMS 2018 y la Directiva europea 2002/49/CE. Los cálculos se apoyan en la extracción de datos del TMR-16 y TMR-61 persistidos en `data/flights.db` (ver `src/noise_metrics.py` para la reproducibilidad).

Fecha: 2026-04-23.

---

## 1. Resumen ejecutivo

La respuesta de AENA a la queja 2026/MA000106 afirma que "se cumplen los Objetivos de Calidad Acústica" basándose únicamente en el **Real Decreto 1367/2007** (umbrales: 65/65/55 dB A ponderado, día/tarde/noche, zona residencial). Con los mismos datos que AENA publica:

- ❌ **El LAeq Total nocturno del TMR-16 excede la recomendación OMS 2018** (< 40 dB Lnight para ruido aeronáutico) **en los 7 años analizados** (2019-2025). Margen: −2.1 a −10.1 dB.
- ❌ **El Lden calculado para el TMR-16 Avión 2024-2025 excede la recomendación OMS 2018** (< 45 dB Lden) por unos **4 dB**.
- ❌ **El Lden Total del TMR-16 y TMR-61 supera el umbral de reporte obligatorio de la Directiva 2002/49/CE** (55 dB) en varios años.
- ⚠️ **AENA no publica las métricas internacionales estándar** (Lden, Lnight como tales, LAmax por evento, SEL, nº sucesos/día) — publica solo LAeq por periodo agregado anual.
- ✅ El RD 1367/2007 se cumple para LAeq Total (55,1 / 49,9 / 43,6 dB en 2025, contra umbrales 65/65/55), pero el RD español es **~20 dB más laxo que la OMS**. Cumplir el RD no significa proteger la salud.

Conclusión: la frase "se cumplen los objetivos de calidad acústica" es técnicamente correcta **solo bajo el RD español**. Bajo estándares de salud pública internacionales (OMS) y bajo los umbrales de reporte europeos (Directiva 2002/49/CE), el ruido medido por AENA en Tres Cantos **ya excede** los límites de lo que se considera aceptable.

---

## 2. Umbrales comparados (zona residencial, ruido aeronáutico)

| Norma | Aplicación | Indicador | Umbral | Estatus |
|---|---|---|---|---|
| **RD 1367/2007** (España, Anexo II Tabla A) | Objetivo de calidad acústica en exterior — zona residencial | LAeq Ld (07-19h) | 65 dB | Obligatorio |
| | | LAeq Le (19-23h) | 65 dB | Obligatorio |
| | | LAeq Ln (23-07h) | 55 dB | Obligatorio |
| **OMS 2018** (Environmental Noise Guidelines, aircraft) | Recomendación de salud pública europea | Lden | 45 dB | *"Strong recommendation"* — efectos en salud por encima |
| | | Lnight | 40 dB | *"Strong recommendation"* — alteración del sueño por encima |
| **Directiva 2002/49/CE** (mapeo estratégico UE) | Obliga a mapear superficies expuestas en aeropuertos con >50.000 mov./año (Barajas: 430.353 en 2025) | Lden | 55 dB | Umbral de reporte obligatorio |
| | | Lnight | 50 dB | Umbral de reporte obligatorio |

**Nota clave sobre el RD 1367/2007**: su Tabla A deriva de la Directiva 1999/30/CE (previa a la 2002/49/CE) y nunca se ha alineado con las guías OMS 2018. España es uno de los países europeos con umbrales más laxos para ruido aeronáutico. La Directiva europea deja los **valores límite** a cada Estado, pero fija umbrales de **mapeo obligatorio** (55/50 dB) que son muy inferiores a los del RD español (65/55 dB) — AENA los superaría en algunos años si los reportara.

---

## 3. Lden y Lnight calculados a partir de los datos oficiales de AENA

Fórmula Lden (Directiva 2002/49/CE, Anexo I; ver `src/noise_metrics.py`):

$$
L_{den} = 10 \cdot \log_{10}\left(\frac{1}{24} \cdot \left[12 \cdot 10^{L_d/10} + 4 \cdot 10^{(L_e+5)/10} + 8 \cdot 10^{(L_n+10)/10}\right]\right)
$$

### TMR-16 Tres Cantos (ubicación King's College / Vivero)

| Año | Lden Total | Lden Avión | Lnight Total | Lnight Avión |
|---|---|---|---|---|
| 2019 | 58,2 | 39,0 | 49,2 | 17,9 |
| 2020 | 57,8 | 35,9 | 50,1 | 12,8 |
| 2021 | 57,6 | 36,9 | 50,0 | 18,4 |
| 2022 | 57,7 | 38,0 | 49,9 | 16,3 |
| 2024 | 52,8 | 48,9 | 42,1 | 24,2 |
| 2025 | **54,6** | **49,2** | **43,6** | **25,0** |

### TMR-61 Tres Cantos Norte (sin acreditación ENAC)

| Año | Lden Total | Lden Avión | Lnight Total | Lnight Avión |
|---|---|---|---|---|
| 2022 | 54,8 | 44,7 | 44,8 | 32,2 |
| 2023 | 59,1 | 45,0 | 46,3 | 32,5 |
| 2024 | 56,9 | 45,6 | 46,6 | 32,5 |
| 2025 | **58,2** | **46,7** | **49,9** | **32,6** |

### Evaluación de cumplimiento (datos 2025, ambos TMRs)

| Indicador | Valor 2025 | RD 1367/2007 | OMS 2018 aircraft | Directiva 2002/49/CE |
|---|---|---|---|---|
| **TMR-16 Lden Total** | 54,6 dB | ✅ (65) | ❌ excede por 9,6 dB (45) | ✅ bajo umbral reporte (55) |
| **TMR-16 Lden Avión** | 49,2 dB | ✅ (65) | ❌ excede por **4,2 dB** (45) | ✅ bajo umbral reporte (55) |
| **TMR-16 Lnight Total** | 43,6 dB | ✅ (55) | ❌ excede por **3,6 dB** (40) | ✅ bajo umbral reporte (50) |
| **TMR-16 Lnight Avión** | 25,0 dB | ✅ (55) | ✅ cumple (40) | ✅ |
| **TMR-61 Lden Total** | 58,2 dB | ✅ (65) | ❌ excede por 13,2 dB | ❌ **supera reporte (55)** |
| **TMR-61 Lden Avión** | 46,7 dB | ✅ (65) | ❌ excede por **1,7 dB** | ✅ |
| **TMR-61 Lnight Total** | 49,9 dB | ✅ (55) | ❌ excede por **9,9 dB** | al borde reporte (50) |
| **TMR-61 Lnight Avión** | 32,6 dB | ✅ (55) | ✅ cumple (40) | ✅ |

### Años anteriores que también superan OMS / Directiva EU

- **2020 TMR-16 Lnight Total = 50,1 dB**. Supera umbral de reporte obligatorio de la Directiva 2002/49/CE (50). AENA no lo reporta.
- **2019-2022 TMR-16 Lnight Total ≥ 49 dB**. Todos al borde del umbral europeo.
- **2023 TMR-61 Lden Total = 59,1 dB**. 4 dB por encima del umbral europeo de reporte.

---

## 4. Lo que AENA mide pero no publica

Los TMRs de SIRMA (Sistema de Monitorado de Ruido y Sendas de Vuelo de Barajas) son sonómetros de clase 1 acreditados para registrar **eventos individuales** además del LAeq agregado. La tecnología es idéntica a la de otros aeropuertos europeos (Schiphol, Heathrow, CDG) que sí publican métricas por evento. AENA publica solo:

- LAeq Total y LAeq Avión por periodo (día/tarde/noche), agregado mensual y anual.
- Número de eventos correlacionados por año (en la tabla 3.1 del informe anual).

AENA **no publica**, aunque los mide:

| Métrica | Qué es | Por qué importa |
|---|---|---|
| **Lden / Lnight** (Directiva 2002/49/CE) | Indicadores estándar europeos con penalizaciones horarias | Son la métrica con la que se evalúan los demás aeropuertos europeos. Cumplir RD 1367 sin Lden oculta el impacto nocturno real |
| **LAmax por evento** | Pico máximo de ruido de cada avión individual | Un LAeq de 50 dB puede contener 80 picos diarios de 75 dB. El LAmax mide el evento molesto |
| **SEL (Sound Exposure Level) por evento** | Energía total de cada paso en 1 segundo equivalente | Métrica estándar internacional para dosis acústica por evento |
| **Distribución L10 / L50 / L90** | Percentiles del nivel sonoro | Dan la variabilidad que el promedio esconde |
| **Número de eventos >65 dB / >70 dB / >80 dB por día** | Conteo de picos molestos | En Heathrow y Schiphol se publican estos conteos |
| **Duración media del paso de avión en la zona** | Cuánto dura cada intrusión acústica | Correlaciona con alteración del sueño |
| **Disponibilidad de datos válidos por hora** | % de horas con dato fiable | Revelaría los largos periodos con TMR-16 <70% (hay años con el dato oficial entero bajo bandera) |

La OMS y numerosos estudios epidemiológicos usan estas métricas para derivar relaciones dosis-respuesta con trastornos del sueño, enfermedad cardiovascular y deterioro cognitivo en niños. El informe anual de AENA no permite a un ciudadano saber cuántas veces al día un avión supera los 70 u 80 dB sobre su casa.

---

## 5. Recomendación técnica para réplica formal

Elementos que se pueden incorporar a una segunda queja formal ante AENA, o al recurso administrativo posterior:

1. **Solicitar explícitamente la publicación de Lden y Lnight** del TMR-16 y TMR-61 según la metodología de la Directiva 2002/49/CE. AENA está obligada a calcularlos como "gran aeropuerto" (> 50.000 mov./año) en los mapas estratégicos quinquenales; el dato existe.

2. **Solicitar el cumplimiento contra umbrales OMS 2018** como referencia de salud, no solo contra el RD 1367/2007. Las guías OMS son evidencia médica europea; aunque no son vinculantes, AENA no puede afirmar "se protege la salud" mientras los valores exceden la OMS.

3. **Solicitar datos por evento** (LAmax, SEL, nº eventos >65/70/80 dB por día) para el TMR-16 y TMR-61, con granularidad diaria al menos durante los últimos 12 meses. Invocar la Ley 27/2006 de acceso a la información ambiental si AENA se niega.

4. **Cuestionar la representatividad de los TMRs de Tres Cantos**: los dos medidores (TMR-16 en King's College, TMR-61 al norte) están **en los bordes del municipio**, no en el núcleo residencial. El TMR-61 lleva 4 años sin ENAC y registra **~7 dB más de Lnight Total** que el TMR-16 — eso sugiere que en el centro urbano el ruido real está entre ambos valores, no en el menor. Solicitar la instalación de un TMR acreditado en el casco urbano denso (Av. Juan Pablo II, Sector Foresta).

5. **Pedir el historial oficial de disponibilidad del TMR-16**: en los informes 2019-2023 aparece marcado con `*` o `*¹` (sin ENAC, <70% disponibilidad). AENA no puede usar como "datos oficiales" valores que sus propios informes declaran no acreditados. Solicitar tabla año a año con disponibilidad expresada en %.

6. **Incluir la referencia al cambio silencioso de ubicación de jul 2023**: el salto de +10 dB en LAeq Avión día entre 2022 y 2024 no es un aumento del tráfico, es consecuencia de mover el sensor. AENA lo debe explicar en sus informes y no lo hace.

---

## 6. Referencias

- Real Decreto 1367/2007, de 19 de octubre, por el que se desarrolla la Ley 37/2003 del Ruido. BOE núm. 254 de 23/10/2007.
- Directiva 2002/49/CE del Parlamento Europeo y del Consejo, de 25 de junio de 2002, sobre evaluación y gestión del ruido ambiental.
- World Health Organization (2018). *Environmental Noise Guidelines for the European Region*. ISBN 978 92 890 5356 3.
- Ley 37/2003, de 17 de noviembre, del Ruido.
- Ley 27/2006, de 18 de julio, de acceso a la información ambiental.
- Informes anuales de ruido del Aeropuerto Adolfo Suárez Madrid-Barajas, años 2016-2025 (Envirosuite Ibérica S.A., antes EMS Brüel & Kjær).

Datos y cálculos reproducibles: `src/noise_metrics.py` + `data/flights.db` (tablas `noise_annual` y `noise_monthly`).
