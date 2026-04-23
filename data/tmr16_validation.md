# Validación manual de valores OCR del TMR16

Rango analizado: 2017-2026. **Total celdas sospechosas: 213**

Desglose por tipo:
- `no_valid_readings` (ninguna lectura OCR — revisar manualmente): **29**
- `high_spread` (rango >5 dB entre lecturas — posible confusión Total/Avión o mezcla de meses): **123**
- `std_X` (desviación típica >2 dB): **6**
- `only_N_readings` (pocas lecturas <3): **55**

## Cómo validar

Para cada celda dudosa:
1. Mira la **mediana** propuesta (columna `median` en el CSV) y las lecturas individuales.
2. Si la mediana parece razonable (Total 40-70 dB; Avión 15-55 dB; noche Avión puede ser 0), suele estar OK.
3. Si no, abre el PDF del informe origen más cercano (p.ej. si buscas jun 2020, abre `2020-06` o `2020-07`) y busca la página del TMR16 (mirar marker `TMR[\s\-]?16`). Anota el valor correcto.
4. Edita `data/tmr16_aggregated.csv` para corregir la mediana (opcionalmente añade una columna `manual_value`).

## 2017-01

### day / total — mediana: **45.4**  (razón: `high_spread_10.7|std_6.2`, 3 lecturas, rango 45.4–56.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-01 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-02 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 5 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2017-10 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2017-11 | 2 | 45.4 |  | 74 | `454` | no_decimal_dot |
| 2017-12 | 1 | 45.4 |  | 54 | `454` | no_decimal_dot |
| 2018-01 | 0 | 56.1 |  | 50 | `561` | no_decimal_dot |

### day / avion — mediana: **45.4**  (razón: `only_1_readings`, 1 lecturas, rango 45.4–45.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-01 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-02 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 5 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 4 | None |  | 51 | `4` | parse_error |
| 2017-10 | 3 | None |  | 61 | `4` | parse_error |
| 2017-11 | 2 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 1 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 0 | 45.4 |  | 61 | `454` | no_decimal_dot |

### evening / total — mediana: **44.8**  (razón: `high_spread_14.4|only_2_readings`, 2 lecturas, rango 37.6–52.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-01 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-02 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 5 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 4 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 3 | 37.6 |  | 76 | `376` | no_decimal_dot |
| 2017-11 | 2 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 1 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 0 | 52.0 |  | 81 | `520` | no_decimal_dot |

### evening / avion — mediana: **37.6**  (razón: `only_1_readings`, 1 lecturas, rango 37.6–37.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-01 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-02 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 5 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 4 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 3 | None |  | -1 | `` | row_not_detected |
| 2017-11 | 2 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 1 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 0 | 37.6 |  | 89 | `376` | no_decimal_dot |

## 2017-02

### day / total — mediana: **52.35**  (razón: `high_spread_11.7|std_5.8`, 4 lecturas, rango 44.5–56.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-02 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2017-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2017-11 | 3 | 48.5 |  | 32 | `485` | no_decimal_dot |
| 2017-12 | 2 | 44.5 |  | 29 | `445` | no_decimal_dot |
| 2018-01 | 1 | 56.2 |  | 67 | `562` | no_decimal_dot |
| 2018-02 | 0 | 56.2 |  | 56 | `562` | no_decimal_dot |

### day / avion — mediana: **44.5**  (razón: `only_2_readings`, 2 lecturas, rango 44.5–44.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-02 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 5 | None |  | 36 | `5` | parse_error |
| 2017-10 | 4 | None |  | 58 | `5` | parse_error |
| 2017-11 | 3 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 2 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 1 | 44.5 |  | 32 | `445` | no_decimal_dot |
| 2018-02 | 0 | 44.5 |  | 82 | `44.5` |  |

### evening / total — mediana: **51.7**  (razón: `high_spread_13.9|std_8.0`, 3 lecturas, rango 37.8–51.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-02 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 5 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 4 | 37.8 |  | 79 | `378` | no_decimal_dot |
| 2017-11 | 3 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 2 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 1 | 51.7 |  | 84 | `517` | no_decimal_dot |
| 2018-02 | 0 | 51.7 |  | 68 | `517` | no_decimal_dot |

### evening / avion — mediana: **37.8**  (razón: `only_2_readings`, 2 lecturas, rango 37.8–37.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-02 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-03 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 6 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 5 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 4 | None |  | -1 | `` | row_not_detected |
| 2017-11 | 3 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 2 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 1 | 37.8 |  | 90 | `378` | no_decimal_dot |
| 2018-02 | 0 | 37.8 |  | 86 | `37.8` |  |

## 2017-03

### day / total — mediana: **49.25**  (razón: `high_spread_20.0|std_9.8`, 4 lecturas, rango 35.3–55.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-03 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 6 | None |  | 42 | `2)` | parse_error |
| 2017-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2017-11 | 4 | None |  | 39 | `32` | parse_error |
| 2017-12 | 3 | 43.2 |  | 75 | `432` | no_decimal_dot |
| 2018-01 | 2 | 55.3 |  | 76 | `553` | no_decimal_dot |
| 2018-02 | 1 | 55.3 |  | 72 | `553` | no_decimal_dot |
| 2018-03 | 0 | 35.3 |  | 60 | `353` | no_decimal_dot |

### evening / total — mediana: **50.9**  (razón: `high_spread_15.3|std_7.6`, 4 lecturas, rango 35.6–50.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-03 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-04 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 7 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 6 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 5 | 35.6 |  | 84 | `356` | no_decimal_dot |
| 2017-11 | 4 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 3 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 2 | 50.9 |  | 72 | `509` | no_decimal_dot |
| 2018-02 | 1 | 50.9 |  | 74 | `509` | no_decimal_dot |
| 2018-03 | 0 | 50.9 |  | 72 | `509` | no_decimal_dot |

## 2017-04

### day / total — mediana: **54.9**  (razón: `high_spread_11.7|std_5.8`, 4 lecturas, rango 43.2–54.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-04 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2017-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2017-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2017-12 | 4 | 43.2 |  | 72 | `432` | no_decimal_dot |
| 2018-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2018-02 | 2 | 54.9 |  | 81 | `549` | no_decimal_dot |
| 2018-03 | 1 | 54.9 |  | 76 | `549` | no_decimal_dot |
| 2018-04 | 0 | 54.9 |  | 32 | `549` | no_decimal_dot |

### evening / total — mediana: **51.6**  (razón: `high_spread_16.4|std_9.0`, 5 lecturas, rango 35.2–51.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-04 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-05 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 8 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 7 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 6 | 35.2 |  | 51 | `352` | no_decimal_dot |
| 2017-11 | 5 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 4 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 3 | 51.6 |  | 44 | `516` | no_decimal_dot |
| 2018-02 | 2 | 51.6 |  | 52 | `516` | no_decimal_dot |
| 2018-03 | 1 | 51.6 |  | 59 | `516` | no_decimal_dot |
| 2018-04 | 0 | 35.2 |  | 92 | `352` | no_decimal_dot |

## 2017-05

### day / total — mediana: **55.2**  (razón: `high_spread_12.6|std_6.3`, 4 lecturas, rango 42.6–55.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-05 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2017-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2017-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2017-12 | 5 | 42.6 |  | 41 | `426` | no_decimal_dot |
| 2018-01 | 4 | 95.2 |  | 74 | `952` | out_of_range |
| 2018-02 | 3 | 55.2 |  | 0 | `552` | no_decimal_dot |
| 2018-03 | 2 | 55.2 |  | 43 | `552` | no_decimal_dot |
| 2018-04 | 1 | 55.2 |  | 71 | `552` | no_decimal_dot |
| 2018-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **51.0**  (razón: `high_spread_17.7|std_10.2`, 3 lecturas, rango 33.3–51.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-05 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-06 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 9 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 8 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 7 | 33.3 |  | 80 | `333` | no_decimal_dot |
| 2017-11 | 6 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 5 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 4 | 51.0 |  | 48 | `510` | no_decimal_dot |
| 2018-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 2 | None |  | 55 | `10` | parse_error |
| 2018-04 | 1 | None |  | 77 | `33` | parse_error |
| 2018-05 | 0 | 51.0 |  | 37 | `510` | no_decimal_dot |

## 2017-06

### day / total — mediana: **55.2**  (razón: `high_spread_12.0|std_4.5`, 7 lecturas, rango 43.2–55.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-06 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2017-10 | 8 | None |  | 34 | `2]` | parse_error |
| 2017-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2017-12 | 6 | 43.2 |  | 76 | `432` | no_decimal_dot |
| 2018-01 | 5 | 55.2 |  | 56 | `552` | no_decimal_dot |
| 2018-02 | 4 | 55.2 |  | 23 | `552` | no_decimal_dot |
| 2018-03 | 3 | 55.2 |  | 27 | `552` | no_decimal_dot |
| 2018-04 | 2 | 55.2 |  | 56 | `552` | no_decimal_dot |
| 2018-05 | 1 | 55.2 |  | 65 | `552` | no_decimal_dot |
| 2018-06 | 0 | 55.2 |  | 70 | `55.2` |  |

### evening / total — mediana: **53.0**  (razón: `high_spread_19.0|std_9.8`, 6 lecturas, rango 34.0–53.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-06 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-07 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 10 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 9 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 8 | 34.0 |  | 69 | `340` | no_decimal_dot |
| 2017-11 | 7 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 6 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 5 | 53.0 |  | 71 | `530` | no_decimal_dot |
| 2018-02 | 4 | 53.0 |  | 25 | `530` | no_decimal_dot |
| 2018-03 | 3 | 53.0 |  | 46 | `530` | no_decimal_dot |
| 2018-04 | 2 | None |  | 71 | `40)` | parse_error |
| 2018-05 | 1 | 53.0 |  | 64 | `530` | no_decimal_dot |
| 2018-06 | 0 | 34.0 |  | 78 | `34.0` |  |

## 2017-07

### evening / total — mediana: **31.9**  (razón: `only_2_readings`, 2 lecturas, rango 31.9–31.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-07 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-08 | 11 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 10 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 9 | 31.9 |  | 44 | `319` | no_decimal_dot |
| 2017-11 | 8 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 7 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 4 | None |  | 42 | `10` | parse_error |
| 2018-04 | 3 | None |  | 55 | `19` | parse_error |
| 2018-05 | 2 | None |  | 51 | `10` | parse_error |
| 2018-06 | 1 | 31.9 |  | 95 | `31.9` |  |
| 2018-07 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2017-08

### day / total — mediana: **53.1**  (razón: `high_spread_12.9|std_6.2`, 10 lecturas, rango 40.2–53.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-08 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 11 | 40.2 |  | 36 | `402` | no_decimal_dot |
| 2017-10 | 10 | None |  | 36 | `42` | parse_error |
| 2017-11 | 9 | 40.2 |  | 45 | `402` | no_decimal_dot |
| 2017-12 | 8 | 40.2 |  | 23 | `402` | no_decimal_dot |
| 2018-01 | 7 | 53.1 |  | 60 | `531` | no_decimal_dot |
| 2018-02 | 6 | 53.1 |  | 36 | `531` | no_decimal_dot |
| 2018-03 | 5 | 53.1 |  | 19 | `531]` | no_decimal_dot |
| 2018-04 | 4 | 53.1 |  | 57 | `531` | no_decimal_dot |
| 2018-05 | 3 | 53.1 |  | 59 | `531` | no_decimal_dot |
| 2018-06 | 2 | 53.1 |  | 81 | `531` | no_decimal_dot |
| 2018-07 | 1 | 53.1 |  | 82 | `53.1` |  |
| 2018-08 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **48.6**  (razón: `high_spread_19.8|std_10.8`, 5 lecturas, rango 28.8–48.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-08 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 11 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 10 | 28.8 |  | 76 | `288` | no_decimal_dot |
| 2017-11 | 9 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 8 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 7 | 48.6 |  | 44 | `486` | no_decimal_dot |
| 2018-02 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 2 | 28.8 |  | 82 | `28.8` |  |
| 2018-07 | 1 | 48.6 |  | 73 | `48.6` |  |
| 2018-08 | 0 | 48.6 |  | 82 | `48.6` |  |

### evening / avion — mediana: **28.8**  (razón: `high_spread_6.0|std_3.0`, 5 lecturas, rango 22.8–28.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-08 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 11 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 10 | None |  | -1 | `` | row_not_detected |
| 2017-11 | 9 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 8 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 7 | 28.8 |  | 85 | `288` | no_decimal_dot |
| 2018-02 | 6 | 23.8 |  | 44 | `238` | no_decimal_dot |
| 2018-03 | 5 | None |  | 77 | `28` | parse_error |
| 2018-04 | 4 | None |  | -1 | `` | row_not_detected |
| 2018-05 | 3 | 28.8 |  | 87 | `28.8` |  |
| 2018-06 | 2 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 1 | 28.8 |  | 69 | `28.8` |  |
| 2018-08 | 0 | 22.8 |  | 68 | `22.8` |  |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-08 | 12 | None |  | -1 | `` | chart_not_detected |
| 2017-09 | 11 | None |  | 76 | `69` | parse_error |
| 2017-10 | 10 | None |  | 90 | `69` | parse_error |
| 2017-11 | 9 | None |  | 93 | `69` | parse_error |
| 2017-12 | 8 | None |  | 86 | `69` | parse_error |
| 2018-01 | 7 | None |  | 83 | `69` | parse_error |
| 2018-02 | 6 | None |  | 92 | `69` | parse_error |
| 2018-03 | 5 | None |  | 91 | `69` | parse_error |
| 2018-04 | 4 | None |  | 94 | `69` | parse_error |
| 2018-05 | 3 | None |  | 96 | `69` | parse_error |
| 2018-06 | 2 | None |  | 96 | `69` | parse_error |
| 2018-07 | 1 | None |  | 93 | `69` | parse_error |
| 2018-08 | 0 | None |  | 93 | `69` | parse_error |

## 2017-09

### day / total — mediana: **54.6**  (razón: `high_spread_10.4|std_5.2`, 9 lecturas, rango 44.2–54.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-09 | 12 | 44.2 |  | 50 | `442` | no_decimal_dot |
| 2017-10 | 11 | 44.2 |  | 38 | `442` | no_decimal_dot |
| 2017-11 | 10 | 44.2 |  | 42 | `442` | no_decimal_dot |
| 2017-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-01 | 8 | 54.6 |  | 60 | `546` | no_decimal_dot |
| 2018-02 | 7 | 54.6 |  | 29 | `546` | no_decimal_dot |
| 2018-03 | 6 | 54.6 |  | 42 | `546` | no_decimal_dot |
| 2018-04 | 5 | None |  | 0 | `46` | parse_error |
| 2018-05 | 4 | 54.6 |  | 37 | `546` | no_decimal_dot |
| 2018-06 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2018-07 | 2 | None |  | 81 | `46` | parse_error |
| 2018-08 | 1 | 54.6 |  | 29 | `546` | no_decimal_dot |
| 2018-09 | 0 | 54.6 | * | 73 | `*54.6` |  |

### evening / total — mediana: **50.7**  (razón: `high_spread_14.5|std_7.5`, 8 lecturas, rango 36.2–50.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-09 | 12 | None |  | -1 | `` | row_not_detected |
| 2017-10 | 11 | 36.2 |  | 75 | `362` | no_decimal_dot |
| 2017-11 | 10 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 9 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 8 | 50.7 |  | 72 | `507` | no_decimal_dot |
| 2018-02 | 7 | 90.7 |  | 9 | `907` | out_of_range |
| 2018-03 | 6 | 50.7 |  | 45 | `507` | no_decimal_dot |
| 2018-04 | 5 | 36.2 |  | 51 | `362` | no_decimal_dot |
| 2018-05 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 3 | 36.2 |  | 60 | `36.2` |  |
| 2018-07 | 2 | 50.7 |  | 87 | `507` | no_decimal_dot |
| 2018-08 | 1 | 50.7 |  | 89 | `507` | no_decimal_dot |
| 2018-09 | 0 | 50.7 |  | 52 | `50.7` |  |

### night / total — mediana: **49.4**  (razón: `high_spread_9.0|std_2.6`, 12 lecturas, rango 40.4–49.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-09 | 12 | 40.4 |  | 60 | `404` | no_decimal_dot |
| 2017-10 | 11 | 49.4 |  | 52 | `494` | no_decimal_dot |
| 2017-11 | 10 | 49.4 |  | 67 | `494` | no_decimal_dot |
| 2017-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-01 | 8 | 49.4 |  | 69 | `494` | no_decimal_dot |
| 2018-02 | 7 | 49.4 |  | 84 | `494` | no_decimal_dot |
| 2018-03 | 6 | 49.4 |  | 86 | `494` | no_decimal_dot |
| 2018-04 | 5 | 49.4 |  | 58 | `494` | no_decimal_dot |
| 2018-05 | 4 | 49.4 |  | 88 | `494` | no_decimal_dot |
| 2018-06 | 3 | 49.4 |  | 81 | `494` | no_decimal_dot |
| 2018-07 | 2 | 49.4 |  | 87 | `494` | no_decimal_dot |
| 2018-08 | 1 | 49.4 |  | 82 | `49.4` |  |
| 2018-09 | 0 | 49.4 | * | 37 | `*49.4|` |  |

## 2017-10

### evening / total — mediana: **51.8**  (razón: `high_spread_15.7|std_8.4`, 7 lecturas, rango 36.1–51.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-10 | 12 | 36.1 |  | 80 | `361` | no_decimal_dot |
| 2017-11 | 11 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 10 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-02 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 6 | 36.1 |  | 68 | `361` | no_decimal_dot |
| 2018-05 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 4 | 36.1 |  | 94 | `36.1` |  |
| 2018-07 | 3 | 51.8 |  | 27 | `518` | no_decimal_dot |
| 2018-08 | 2 | 51.8 |  | 87 | `518` | no_decimal_dot |
| 2018-09 | 1 | 51.8 | * | 81 | `*51.8` |  |
| 2018-10 | 0 | 51.8 | * | 70 | `*51.8` |  |

## 2017-11

### day / total — mediana: **55.5**  (razón: `high_spread_20.0|std_6.8`, 10 lecturas, rango 35.5–55.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-11 | 12 | 45.3 |  | 78 | `453` | no_decimal_dot |
| 2017-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-01 | 10 | 55.5 |  | 81 | `555` | no_decimal_dot |
| 2018-02 | 9 | 55.5 |  | 76 | `555` | no_decimal_dot |
| 2018-03 | 8 | None |  | 47 | `55` | parse_error |
| 2018-04 | 7 | 55.5 |  | 46 | `555` | no_decimal_dot |
| 2018-05 | 6 | None |  | 54 | `55` | parse_error |
| 2018-06 | 5 | 55.5 |  | 79 | `555` | no_decimal_dot |
| 2018-07 | 4 | 55.5 |  | 90 | `555` | no_decimal_dot |
| 2018-08 | 3 | 35.5 |  | 21 | `355` | no_decimal_dot |
| 2018-09 | 2 | 55.5 | * | 61 | `*55.5` |  |
| 2018-10 | 1 | 55.5 | * | 80 | `*55.5` |  |
| 2018-11 | 0 | 55.5 | * | 81 | `*55.5` |  |

### evening / total — mediana: **51.7**  (razón: `high_spread_12.0|std_5.9`, 7 lecturas, rango 39.7–51.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-11 | 12 | None |  | -1 | `` | row_not_detected |
| 2017-12 | 11 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 10 | 51.7 |  | 56 | `517` | no_decimal_dot |
| 2018-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 7 | 39.7 |  | 75 | `397` | no_decimal_dot |
| 2018-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 5 | 39.7 |  | 82 | `39.7` |  |
| 2018-07 | 4 | None |  | 17 | `57` | parse_error |
| 2018-08 | 3 | 51.7 |  | 68 | `517` | no_decimal_dot |
| 2018-09 | 2 | 51.7 | * | 67 | `*51.7` |  |
| 2018-10 | 1 | 51.7 | * | 37 | `*51.7` |  |
| 2018-11 | 0 | 51.7 | * | 77 | `*51.7` |  |

### night / avion — mediana: **0.0**  (razón: `only_1_readings`, 1 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-11 | 12 | None |  | 8 | `00` | parse_error |
| 2017-12 | 11 | None |  | 81 | `00` | parse_error |
| 2018-01 | 10 | None |  | 89 | `00` | parse_error |
| 2018-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-07 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 3 | 0.0 |  | 43 | `0.0` |  |
| 2018-09 | 2 | None |  | 82 | `*0.0` | parse_error |
| 2018-10 | 1 | None |  | 86 | `*0.0` | parse_error |
| 2018-11 | 0 | None |  | 75 | `*0.0` | parse_error |

## 2017-12

### evening / total — mediana: **52.0**  (razón: `high_spread_13.7|std_5.8`, 10 lecturas, rango 38.3–52.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-12 | 12 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 11 | 52.0 |  | 61 | `520` | no_decimal_dot |
| 2018-02 | 10 | 52.0 |  | 58 | `520` | no_decimal_dot |
| 2018-03 | 9 | None |  | 61 | `20` | parse_error |
| 2018-04 | 8 | 38.3 |  | 87 | `383` | no_decimal_dot |
| 2018-05 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 6 | 38.3 |  | 87 | `38.3` |  |
| 2018-07 | 5 | 52.0 |  | 76 | `520` | no_decimal_dot |
| 2018-08 | 4 | 52.0 |  | 79 | `520` | no_decimal_dot |
| 2018-09 | 3 | 52.0 | * | 62 | `*52.0` |  |
| 2018-10 | 2 | 52.0 | * | 81 | `*52.0` |  |
| 2018-11 | 1 | 52.0 | * | 83 | `*52.0` |  |
| 2018-12 | 0 | 52.0 |  | 26 | `52.0` |  |

### evening / avion — mediana: **38.3**  (razón: `high_spread_10.0|std_3.5`, 8 lecturas, rango 38.3–48.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2017-12 | 12 | None |  | -1 | `` | row_not_detected |
| 2018-01 | 11 | 38.3 |  | 57 | `383` | no_decimal_dot |
| 2018-02 | 10 | 38.3 |  | 77 | `38.3` |  |
| 2018-03 | 9 | 38.3 |  | 75 | `383` | no_decimal_dot |
| 2018-04 | 8 | None |  | -1 | `` | row_not_detected |
| 2018-05 | 7 | 38.3 |  | 65 | `38.3.` |  |
| 2018-06 | 6 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 5 | 38.3 |  | 91 | `38.3` |  |
| 2018-08 | 4 | 38.3 |  | 90 | `38.3` |  |
| 2018-09 | 3 | 48.3 | * | 61 | `*48.3` |  |
| 2018-10 | 2 | 438.3 | ¹ | 71 | `438.3)` | out_of_range |
| 2018-11 | 1 | 38.3 | * | 83 | `*38.3` |  |
| 2018-12 | 0 | 498.3 | * | 45 | `*498.3` | out_of_range |

## 2018-01

### evening / total — mediana: **52.1**  (razón: `high_spread_14.3|std_6.3`, 9 lecturas, rango 37.8–52.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-01 | 12 | 52.1 |  | 50 | `521` | no_decimal_dot |
| 2018-02 | 11 | 52.1 |  | 39 | `521` | no_decimal_dot |
| 2018-03 | 10 | None |  | 31 | `21` | parse_error |
| 2018-04 | 9 | 37.8 |  | 72 | `378` | no_decimal_dot |
| 2018-05 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 7 | 37.8 |  | 88 | `37.8` |  |
| 2018-07 | 6 | 52.1 |  | 50 | `521` | no_decimal_dot |
| 2018-08 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 3 | 52.1 | * | 63 | `*52.1|` |  |
| 2018-11 | 2 | 52.1 | * | 49 | `*52.1` |  |
| 2018-12 | 1 | 52.1 | * | 75 | `*52.1` |  |
| 2019-01 | 0 | 52.1 | * | 82 | `*52.1|` |  |

### evening / avion — mediana: **37.8**  (razón: `high_spread_10.0|std_4.2`, 10 lecturas, rango 37.8–47.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-01 | 12 | 37.8 |  | 47 | `378` | no_decimal_dot |
| 2018-02 | 11 | 37.8 |  | 83 | `37.8` |  |
| 2018-03 | 10 | 37.8 |  | 66 | `378` | no_decimal_dot |
| 2018-04 | 9 | None |  | -1 | `` | row_not_detected |
| 2018-05 | 8 | 37.8 |  | 77 | `37.8` |  |
| 2018-06 | 7 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 6 | 37.8 |  | 74 | `37.8` |  |
| 2018-08 | 5 | 37.8 |  | 70 | `37.8` |  |
| 2018-09 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 3 | 47.8 | * | 56 | `*47.8` |  |
| 2018-11 | 2 | 47.8 | * | 41 | `*47.8` |  |
| 2018-12 | 1 | 37.8 | * | 81 | `*37.8` |  |
| 2019-01 | 0 | 37.8 | ¹ | 88 | `37.8)` |  |

## 2018-02

### day / avion — mediana: **44.5**  (razón: `high_spread_29.9|std_8.3`, 13 lecturas, rango 44.5–74.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-02 | 12 | 44.5 |  | 31 | `445` | no_decimal_dot |
| 2018-03 | 11 | 44.5 |  | 81 | `445` | no_decimal_dot |
| 2018-04 | 10 | 44.5 |  | 74 | `445` | no_decimal_dot |
| 2018-05 | 9 | 44.5 |  | 78 | `445` | no_decimal_dot |
| 2018-06 | 8 | 44.5 |  | 81 | `445` | no_decimal_dot |
| 2018-07 | 7 | 44.5 |  | 76 | `445` | no_decimal_dot |
| 2018-08 | 6 | 44.5 |  | 61 | `445` | no_decimal_dot |
| 2018-09 | 5 | 44.5 |  | 28 | `445` | no_decimal_dot |
| 2018-10 | 4 | 44.5 |  | 28 | `*445` | no_decimal_dot |
| 2018-11 | 3 | 44.5 |  | 62 | `*445` | no_decimal_dot |
| 2018-12 | 2 | 74.4 | ¹ | 50 | `7445)` | no_decimal_dot |
| 2019-01 | 1 | 44.5 |  | 65 | `*445` | no_decimal_dot |
| 2019-02 | 0 | 44.5 |  | 0 | `445)` | no_decimal_dot |

### evening / total — mediana: **51.8**  (razón: `high_spread_14.6|std_6.5`, 5 lecturas, rango 37.2–51.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-03 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 10 | 37.2 |  | 80 | `372` | no_decimal_dot |
| 2018-05 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 8 | None |  | 1 | `3F2` | parse_error |
| 2018-07 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 5 | 51.8 | * | 62 | `*51.8` |  |
| 2018-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 2 | 51.8 | * | 60 | `*51.8|` |  |
| 2019-01 | 1 | 51.8 | * | 48 | `*51.8` |  |
| 2019-02 | 0 | 51.8 | * | 64 | `*51.8|` |  |

### evening / avion — mediana: **37.2**  (razón: `high_spread_10.6|std_4.8`, 8 lecturas, rango 37.2–47.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-02 | 12 | 37.2 |  | 76 | `37.2` |  |
| 2018-03 | 11 | 37.2 |  | 79 | `37.2` |  |
| 2018-04 | 10 | None |  | -1 | `` | row_not_detected |
| 2018-05 | 9 | None |  | 29 | `3F.2` | parse_error |
| 2018-06 | 8 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 7 | 37.2 |  | 38 | `37.2` |  |
| 2018-08 | 6 | 37.2 |  | 46 | `37.2` |  |
| 2018-09 | 5 | 47.8 | *¹ | 41 | `*47.8)*437.2` |  |
| 2018-10 | 4 | 437.2 | * | 36 | `*437.2` | out_of_range |
| 2018-11 | 3 | 47.2 | * | 72 | `*47.2` |  |
| 2018-12 | 2 | 737.2 | ¹ | 15 | `737.2)` | out_of_range |
| 2019-01 | 1 | 37.2 |  | 79 | `37.2` |  |
| 2019-02 | 0 | 37.2 | * | 0 | `*37.2` |  |

## 2018-03

### evening / total — mediana: **52.1**  (razón: `high_spread_18.7|std_9.1`, 7 lecturas, rango 33.4–52.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 11 | 33.4 |  | 56 | `334` | no_decimal_dot |
| 2018-05 | 10 | None |  | 62 | `21` | parse_error |
| 2018-06 | 9 | 33.4 |  | 86 | `33.4` |  |
| 2018-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 5 | 52.1 |  | 49 | `*521|` | no_decimal_dot |
| 2018-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 3 | 52.1 | * | 57 | `*52.1|` |  |
| 2019-01 | 2 | 52.1 | * | 40 | `*52.1` |  |
| 2019-02 | 1 | 52.1 | * | 21 | `*52.1` |  |
| 2019-03 | 0 | 52.1 | * | 58 | `*52.1|` |  |

### night / total — mediana: **49.8**  (razón: `high_spread_35.7|std_12.6`, 8 lecturas, rango 14.1–49.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-04 | 11 | 49.8 |  | 86 | `498` | no_decimal_dot |
| 2018-05 | 10 | 49.8 |  | 72 | `498` | no_decimal_dot |
| 2018-06 | 9 | 49.8 |  | 61 | `498` | no_decimal_dot |
| 2018-07 | 8 | 49.8 |  | 37 | `498` | no_decimal_dot |
| 2018-08 | 7 | 49.8 |  | 26 | `498` | no_decimal_dot |
| 2018-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 2 | 49.8 |  | 46 | `*498` | no_decimal_dot |
| 2019-02 | 1 | 49.8 |  | 0 | `*498` | no_decimal_dot |
| 2019-03 | 0 | 14.1 | *¹ | 40 | `*14.1)` |  |

## 2018-04

### evening / total — mediana: **51.5**  (razón: `high_spread_16.6|std_8.3`, 6 lecturas, rango 35.9–52.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-04 | 12 | 35.9 |  | 75 | `359` | no_decimal_dot |
| 2018-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 10 | 35.9 |  | 94 | `35.9` |  |
| 2018-07 | 9 | 52.5 |  | 43 | `525` | no_decimal_dot |
| 2018-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 6 | 51.5 |  | 41 | `*515|` | no_decimal_dot |
| 2018-11 | 5 | 52.1 | *¹ | 57 | `*52.1|*515` |  |
| 2018-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 0 | 51.5 | * | 61 | `*51.5|` |  |

### evening / avion — mediana: **35.9**  (razón: `high_spread_6.1`, 7 lecturas, rango 33.4–39.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-04 | 12 | None |  | -1 | `` | row_not_detected |
| 2018-05 | 11 | 35.9 |  | 77 | `35.9` |  |
| 2018-06 | 10 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 9 | 35.9 |  | 94 | `35.9` |  |
| 2018-08 | 8 | 35.9 |  | 95 | `35.9` |  |
| 2018-09 | 7 | 435.9 | *¹ | 14 | `*435.9)` | out_of_range |
| 2018-10 | 6 | 393.4 | *¹ | 8 | `*4393.4/)*3959)` | out_of_range |
| 2018-11 | 5 | 393.4 | *¹ | 0 | `*393.4/)*4395.9` | out_of_range |
| 2018-12 | 4 | 39.5 |  | 33 | `*3959` | no_decimal_dot |
| 2019-01 | 3 | 433.4 | *¹ | 39 | `*433.4)*45.9` | out_of_range |
| 2019-02 | 2 | 33.4 | *¹ | 52 | `*33.4)735.9` |  |
| 2019-03 | 1 | 35.9 | * | 25 | `*35.9` |  |
| 2019-04 | 0 | 35.9 | * | 82 | `*35.9` |  |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2018-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 7 | None |  | 48 | `*00` | parse_error |
| 2018-10 | 6 | None |  | 54 | `*00` | parse_error |
| 2018-11 | 5 | None |  | 50 | `*0.0` | parse_error |
| 2018-12 | 4 | None |  | 77 | `*0.0` | parse_error |
| 2019-01 | 3 | None |  | 79 | `*00` | parse_error |
| 2019-02 | 2 | None |  | 84 | `*0.0` | parse_error |
| 2019-03 | 1 | None |  | -1 | `` | row_not_detected |
| 2019-04 | 0 | None |  | 69 | `*0.0` | parse_error |

## 2018-05

### day / total — mediana: **63.6**  (razón: `high_spread_6.5|std_2.1`, 10 lecturas, rango 57.1–63.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 11 | None |  | 52 | `66` | parse_error |
| 2018-07 | 10 | 63.6 |  | 71 | `636` | no_decimal_dot |
| 2018-08 | 9 | 63.6 |  | 59 | `636` | no_decimal_dot |
| 2018-09 | 8 | 63.6 | * | 68 | `*63.6|` |  |
| 2018-10 | 7 | 63.6 | * | 36 | `*63.6|` |  |
| 2018-11 | 6 | 63.6 | * | 67 | `*63.6|` |  |
| 2018-12 | 5 | 57.1 | *¹ | 34 | `*57.1|*63.6|` |  |
| 2019-01 | 4 | 63.6 |  | 0 | `63.6` |  |
| 2019-02 | 3 | 63.6 |  | 63 | `*636|` | no_decimal_dot |
| 2019-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 1 | 63.6 |  | 34 | `63.6` |  |
| 2019-05 | 0 | 63.6 | * | 58 | `*63.6|` |  |

### evening / total — mediana: **52.5**  (razón: `high_spread_15.2|std_6.2`, 6 lecturas, rango 37.3–52.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-06 | 11 | 37.3 |  | 81 | `37.3` |  |
| 2018-07 | 10 | 52.5 |  | 89 | `525` | no_decimal_dot |
| 2018-08 | 9 | 52.5 |  | 21 | `525` | no_decimal_dot |
| 2018-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 7 | 52.5 |  | 34 | `*525|` | no_decimal_dot |
| 2018-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 4 | None |  | 42 | `*515|*525` | parse_error |
| 2019-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 1 | 52.5 |  | 42 | `*525` | no_decimal_dot |
| 2019-05 | 0 | 52.5 | * | 43 | `*52.5` |  |

### evening / avion — mediana: **37.3**  (razón: `high_spread_10.0|std_3.5`, 8 lecturas, rango 37.3–47.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-05 | 12 | 37.3 |  | 49 | `37.3` |  |
| 2018-06 | 11 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 10 | 37.3 |  | 82 | `37.3` |  |
| 2018-08 | 9 | 37.3 |  | 78 | `37.3` |  |
| 2018-09 | 8 | 497.3 | *¹ | 42 | `*497.3)` | out_of_range |
| 2018-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 6 | 37.3 |  | 44 | `*3739)` | no_decimal_dot |
| 2018-12 | 5 | 397.3 | * | 19 | `*397.3` | out_of_range |
| 2019-01 | 4 | 47.3 | * | 33 | `*47.3` |  |
| 2019-02 | 3 | 37.3 | * | 28 | `*37.3` |  |
| 2019-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 1 | 37.3 | *¹ | 51 | `*37.3)` |  |
| 2019-05 | 0 | 37.3 | ¹ | 46 | `37.3)` |  |

## 2018-06

### day / avion — mediana: **39.6**  (razón: `high_spread_34.3|std_12.9`, 13 lecturas, rango 39.6–73.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-06 | 12 | 39.6 | * | 13 | `*39.6` |  |
| 2018-07 | 11 | 39.6 |  | 71 | `*396` | no_decimal_dot |
| 2018-08 | 10 | 39.6 |  | 82 | `396)` | no_decimal_dot |
| 2018-09 | 9 | 39.9 | ¹ | 8 | `*3996` | no_decimal_dot |
| 2018-10 | 8 | 39.6 |  | 82 | `396)` | no_decimal_dot |
| 2018-11 | 7 | 73.9 | ¹ | 0 | `7396)` | no_decimal_dot |
| 2018-12 | 6 | 73.9 | ¹ | 38 | `7396)` | no_decimal_dot |
| 2019-01 | 5 | 39.6 | * | 56 | `*39.6` |  |
| 2019-02 | 4 | 39.6 |  | 52 | `*396)` | no_decimal_dot |
| 2019-03 | 3 | 39.6 | * | 52 | `*39.6` |  |
| 2019-04 | 2 | 39.6 |  | 0 | `39.6` |  |
| 2019-05 | 1 | 39.6 | * | 85 | `*39.6` |  |
| 2019-06 | 0 | 39.6 | *¹ | 68 | `*39.6)` |  |

### evening / total — mediana: **52.2**  (razón: `high_spread_17.5|std_7.8`, 5 lecturas, rango 34.7–52.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-06 | 12 | 34.7 |  | 46 | `347` | no_decimal_dot |
| 2018-07 | 11 | 52.2 |  | 91 | `522` | no_decimal_dot |
| 2018-08 | 10 | 52.2 |  | 58 | `522` | no_decimal_dot |
| 2018-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 8 | 52.2 |  | 9 | `*522|` | no_decimal_dot |
| 2018-11 | 7 | None |  | 16 | `*525|*522|*514|` | parse_error |
| 2018-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 0 | 52.2 | * | 33 | `*52.2|` |  |

### evening / avion — mediana: **34.7**  (razón: `high_spread_10.0|std_4.1`, 6 lecturas, rango 34.7–44.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-06 | 12 | None |  | -1 | `` | row_not_detected |
| 2018-07 | 11 | 34.7 |  | 83 | `34.7` |  |
| 2018-08 | 10 | 34.7 |  | 87 | `347` | no_decimal_dot |
| 2018-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 5 | 39.4 | ¹ | 38 | `*3947` | no_decimal_dot |
| 2019-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 3 | 44.7 |  | 33 | `*447` | no_decimal_dot |
| 2019-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-05 | 1 | 34.7 | * | 50 | `*34.7` |  |
| 2019-06 | 0 | 34.7 |  | 53 | `34.7` |  |

### night / total — mediana: **51.4**  (razón: `high_spread_26.0|std_10.6`, 6 lecturas, rango 25.4–51.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-06 | 12 | 51.4 |  | 74 | `514` | no_decimal_dot |
| 2018-07 | 11 | 51.4 |  | 53 | `514` | no_decimal_dot |
| 2018-08 | 10 | 51.4 |  | 70 | `514` | no_decimal_dot |
| 2018-09 | 9 | 51.4 |  | 0 | `*514` | no_decimal_dot |
| 2018-10 | 8 | 51.4 |  | 48 | `*514)` | no_decimal_dot |
| 2018-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 3 | 25.4 | * | 7 | `*25.4` |  |
| 2019-04 | 2 | None |  | 14 | `*505/*514` | parse_error |
| 2019-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2018-07

### day / avion — mediana: **41.4**  (razón: `high_spread_32.7|std_9.1`, 13 lecturas, rango 41.4–74.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-07 | 12 | 41.4 |  | 60 | `*414` | no_decimal_dot |
| 2018-08 | 11 | 41.4 |  | 82 | `*414` | no_decimal_dot |
| 2018-09 | 10 | 74.1 | ¹ | 0 | `7414)` | no_decimal_dot |
| 2018-10 | 9 | 41.4 |  | 42 | `*414` | no_decimal_dot |
| 2018-11 | 8 | 41.4 |  | 64 | `*414)` | no_decimal_dot |
| 2018-12 | 7 | 41.4 |  | 51 | `*414)` | no_decimal_dot |
| 2019-01 | 6 | 41.4 |  | 79 | `*414` | no_decimal_dot |
| 2019-02 | 5 | 41.4 |  | 74 | `414` | no_decimal_dot |
| 2019-03 | 4 | 41.4 |  | 69 | `*414` | no_decimal_dot |
| 2019-04 | 3 | 41.4 |  | 68 | `414)` | no_decimal_dot |
| 2019-05 | 2 | 41.4 |  | 39 | `*414` | no_decimal_dot |
| 2019-06 | 1 | 41.4 |  | 7 | `414` | no_decimal_dot |
| 2019-07 | 0 | 41.4 |  | 78 | `414)` | no_decimal_dot |

### evening / total — mediana: **52.2**  (razón: `only_1_readings`, 1 lecturas, rango 52.2–52.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 10 | 52.2 | *¹ | 27 | `*52.2|*514|*50.6|` |  |
| 2018-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 6 | None |  | 35 | `*522|*514|*506|` | parse_error |
| 2019-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 3 | None |  | 45 | `*522|*514|*506|` | parse_error |
| 2019-05 | 2 | None |  | 35 | `*522|*514/*506|` | parse_error |
| 2019-06 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2019-07 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **32.9**  (razón: `high_spread_40.3|std_16.5`, 6 lecturas, rango 32.9–73.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-07 | 12 | 32.9 |  | 0 | `32.9` |  |
| 2018-08 | 11 | 32.9 |  | 90 | `32.9` |  |
| 2018-09 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 7 | 73.2 |  | 45 | `7329)` | no_decimal_dot |
| 2019-01 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 5 | None |  | 1 | `*347>*329)` | parse_error |
| 2019-03 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 3 | 49.2 |  | 33 | `*4929` | no_decimal_dot |
| 2019-05 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 1 | 32.9 | * | 9 | `*32.9` |  |
| 2019-07 | 0 | 32.9 | * | 3 | `*32.9` |  |

### night / total — mediana: **50.45**  (razón: `high_spread_24.2|std_11.9`, 4 lecturas, rango 26.9–51.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-08 | 11 | 51.1 |  | 51 | `511` | no_decimal_dot |
| 2018-09 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 7 | 49.8 | *¹ | 48 | `*49.8|*49.7|*505|*514|` |  |
| 2019-01 | 6 | 51.1 |  | 0 | `*511\` | no_decimal_dot |
| 2019-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 4 | 26.9 | * | 21 | `*26.9` |  |
| 2019-04 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-05 | 2 | None |  | 15 | `*514/*511/*487|` | parse_error |
| 2019-06 | 1 | None |  | 7 | `*514|*511/*487` | parse_error |
| 2019-07 | 0 | 276.9 | *¹ | 0 | `*276.9)` | out_of_range |

## 2018-08

### evening / total — mediana: **50.6**  (razón: `only_2_readings`, 2 lecturas, rango 50.6–50.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 10 | 50.6 | *¹ | 27 | `*514|*50.6|` |  |
| 2018-11 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 8 | None |  | 23 | `*525|*522|*514|*506|` | parse_error |
| 2019-01 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 2 | None |  | 33 | `*514/*506|` | parse_error |
| 2019-07 | 1 | None |  | 3 | `*514|*506/` | parse_error |
| 2019-08 | 0 | 50.6 |  | 65 | `*506|` | no_decimal_dot |

### evening / avion — mediana: **35.0**  (razón: `high_spread_41.2|std_19.9`, 4 lecturas, rango 32.5–73.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-08 | 12 | 32.5 |  | 20 | `32.5` |  |
| 2018-09 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 8 | 37.5 |  | 44 | `*375)` | no_decimal_dot |
| 2019-01 | 7 | None |  | 17 | `*3929/)*3925)` | parse_error |
| 2019-02 | 6 | 73.7 | ¹ | 61 | `7375)` | no_decimal_dot |
| 2019-03 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-04 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2019-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-07 | 1 | None |  | 22 | `*39275)` | parse_error |
| 2019-08 | 0 | 32.5 |  | 73 | `32.5` |  |

### night / total — mediana: **38.3**  (razón: `high_spread_25.8|std_13.6`, 4 lecturas, rango 22.9–48.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-09 | 11 | None |  | 6 | `*511|)*487)` | parse_error |
| 2018-10 | 10 | None |  | 6 | `*511/*4a7|` | parse_error |
| 2018-11 | 9 | 48.7 | * | 44 | `*48.7|` |  |
| 2018-12 | 8 | 48.7 |  | 36 | `*487)` | no_decimal_dot |
| 2019-01 | 7 | None |  | 37 | `*4a7|` | parse_error |
| 2019-02 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 5 | 22.9 | * | 55 | `*22.9` |  |
| 2019-04 | 4 | None |  | 14 | `*511)*487)` | parse_error |
| 2019-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-07 | 1 | 27.9 |  | 21 | `*279` | no_decimal_dot |
| 2019-08 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **22.9**  (razón: `high_spread_49.3|std_19.8`, 6 lecturas, rango 22.9–72.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-08 | 12 | None |  | 67 | `29` | parse_error |
| 2018-09 | 11 | 22.9 |  | 56 | `*229` | no_decimal_dot |
| 2018-10 | 10 | 72.2 |  | 6 | `7229)` | no_decimal_dot |
| 2018-11 | 9 | 22.9 |  | 18 | `*229)` | no_decimal_dot |
| 2018-12 | 8 | None |  | 54 | `72729)` | parse_error |
| 2019-01 | 7 | 27.9 |  | 41 | `*279)` | no_decimal_dot |
| 2019-02 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 5 | None |  | -1 | `` | row_not_detected |
| 2019-04 | 4 | 22.9 |  | 78 | `*229` | no_decimal_dot |
| 2019-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 2 | 22.9 | * | 54 | `*22.9` |  |
| 2019-07 | 1 | None |  | -1 | `` | row_not_detected |
| 2019-08 | 0 | None |  | -1 | `` | row_not_detected |

## 2018-09

### day / avion — mediana: **42.4**  (razón: `high_spread_7.0|std_2.5`, 11 lecturas, rango 42.4–49.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-10 | 11 | 42.4 |  | 50 | `424` | no_decimal_dot |
| 2018-11 | 10 | 47.4 | ¹ | 0 | `47.4)` |  |
| 2018-12 | 9 | 42.4 | ¹ | 10 | `42.4)` |  |
| 2019-01 | 8 | 42.4 | ¹ | 82 | `42.4)` |  |
| 2019-02 | 7 | 42.4 | ¹ | 63 | `42.4)` |  |
| 2019-03 | 6 | 49.4 | ¹ | 17 | `49.4)` |  |
| 2019-04 | 5 | 42.4 | ¹ | 2 | `42.4)` |  |
| 2019-05 | 4 | 42.4 | *¹ | 21 | `**42.4)**` |  |
| 2019-06 | 3 | 42.4 | ¹ | 7 | `42.4)` |  |
| 2019-07 | 2 | 42.4 | *¹ | 29 | `42.4)**` |  |
| 2019-08 | 1 | 42.4 | ¹ | 45 | `42.4)` |  |
| 2019-09 | 0 | None |  | 0 | `4)` | parse_error |

### night / total — mediana: **51.2**  (razón: `high_spread_27.0|std_12.2`, 12 lecturas, rango 24.2–51.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-09 | 12 | 51.2 |  | 82 | `512` | no_decimal_dot |
| 2018-10 | 11 | 51.2 |  | 81 | `512` | no_decimal_dot |
| 2018-11 | 10 | 51.2 |  | 74 | `512` | no_decimal_dot |
| 2018-12 | 9 | 51.2 |  | 66 | `512` | no_decimal_dot |
| 2019-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2019-02 | 7 | 51.2 |  | 83 | `512` | no_decimal_dot |
| 2019-03 | 6 | 24.2 |  | 91 | `24.2` |  |
| 2019-04 | 5 | 51.2 |  | 81 | `512` | no_decimal_dot |
| 2019-05 | 4 | 51.2 |  | 76 | `512` | no_decimal_dot |
| 2019-06 | 3 | 51.2 |  | 73 | `512` | no_decimal_dot |
| 2019-07 | 2 | 24.3 |  | 70 | `243` | no_decimal_dot |
| 2019-08 | 1 | 24.2 |  | 86 | `24.2` |  |
| 2019-09 | 0 | 51.2 |  | 84 | `51.2` |  |

## 2018-10

### night / total — mediana: **50.2**  (razón: `high_spread_32.7|std_13.2`, 11 lecturas, rango 17.5–50.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-11 | 11 | 50.2 |  | 85 | `502` | no_decimal_dot |
| 2018-12 | 10 | 50.2 |  | 81 | `502` | no_decimal_dot |
| 2019-01 | 9 | 50.2 |  | 74 | `502` | no_decimal_dot |
| 2019-02 | 8 | 50.2 |  | 72 | `502` | no_decimal_dot |
| 2019-03 | 7 | 17.5 |  | 92 | `17.5` |  |
| 2019-04 | 6 | 50.2 |  | 89 | `502` | no_decimal_dot |
| 2019-05 | 5 | 50.2 |  | 80 | `50.2` |  |
| 2019-06 | 4 | 50.2 |  | 76 | `502` | no_decimal_dot |
| 2019-07 | 3 | 17.5 |  | 83 | `17.5` |  |
| 2019-08 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 1 | 50.2 |  | 72 | `502` | no_decimal_dot |
| 2019-10 | 0 | 50.2 |  | 85 | `50.2` |  |

## 2018-11

### day / total — mediana: **60.0**  (razón: `high_spread_60.0|std_21.2`, 8 lecturas, rango 0.0–60.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2018-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2019-01 | 10 | 60.0 |  | 50 | `600` | no_decimal_dot |
| 2019-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2019-03 | 8 | 60.0 |  | 61 | `600` | no_decimal_dot |
| 2019-04 | 7 | 60.0 |  | 72 | `60.0` |  |
| 2019-05 | 6 | None |  | 64 | `60` | parse_error |
| 2019-06 | 5 | 60.0 |  | 90 | `60.0` |  |
| 2019-07 | 4 | 60.0 |  | 92 | `60.0` |  |
| 2019-08 | 3 | 60.0 |  | 81 | `60.0` |  |
| 2019-09 | 2 | None |  | 44 | `6.0` | parse_error |
| 2019-10 | 1 | 0.0 |  | 40 | `0.0` |  |
| 2019-11 | 0 | 60.0 |  | 90 | `60.0` |  |

### day / avion — mediana: **39.3**  (razón: `high_spread_20.2|std_7.1`, 8 lecturas, rango 39.3–59.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-11 | 12 | 39.3 |  | 56 | `39.3` |  |
| 2018-12 | 11 | 399.9 |  | 58 | `399.9` | out_of_range |
| 2019-01 | 10 | 39.3 | ¹ | 67 | `39.3)` |  |
| 2019-02 | 9 | 59.5 | ¹ | 23 | `59.5)` |  |
| 2019-03 | 8 | 99.5 | ¹ | 46 | `99.5)` | out_of_range |
| 2019-04 | 7 | 39.3 | ¹ | 77 | `39.3)` |  |
| 2019-05 | 6 | 39.3 | ¹ | 0 | `39.3)` |  |
| 2019-06 | 5 | 39.3 | ¹ | 12 | `39.3)` |  |
| 2019-07 | 4 | 39.3 | ¹ | 0 | `39.3)` |  |
| 2019-08 | 3 | 39.3 | ¹ | 81 | `39.3)` |  |
| 2019-09 | 2 | 399.3 | ¹ | 24 | `7399.3)` | out_of_range |
| 2019-10 | 1 | 739.3 | ¹ | 0 | `739.3)` | out_of_range |
| 2019-11 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **49.7**  (razón: `high_spread_36.1|std_15.8`, 13 lecturas, rango 13.6–49.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-11 | 12 | 49.7 |  | 84 | `497` | no_decimal_dot |
| 2018-12 | 11 | 49.7 |  | 89 | `497` | no_decimal_dot |
| 2019-01 | 10 | 49.7 |  | 87 | `497` | no_decimal_dot |
| 2019-02 | 9 | 49.7 |  | 89 | `497` | no_decimal_dot |
| 2019-03 | 8 | 13.6 |  | 85 | `13.6` |  |
| 2019-04 | 7 | 49.7 |  | 82 | `497` | no_decimal_dot |
| 2019-05 | 6 | 49.7 |  | 92 | `497` | no_decimal_dot |
| 2019-06 | 5 | 49.7 |  | 93 | `497` | no_decimal_dot |
| 2019-07 | 4 | 13.6 |  | 89 | `13.6` |  |
| 2019-08 | 3 | 13.6 |  | 93 | `13.6` |  |
| 2019-09 | 2 | 49.7 |  | 85 | `497` | no_decimal_dot |
| 2019-10 | 1 | 49.7 |  | 91 | `497` | no_decimal_dot |
| 2019-11 | 0 | 49.7 |  | 89 | `49.7` |  |

## 2018-12

### day / avion — mediana: **42.4**  (razón: `high_spread_7.0|std_2.3`, 12 lecturas, rango 42.3–49.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-12 | 12 | 42.3 |  | 43 | `423` | no_decimal_dot |
| 2019-01 | 11 | 42.3 |  | 78 | `423` | no_decimal_dot |
| 2019-02 | 10 | 42.5 |  | 4 | `425)` | no_decimal_dot |
| 2019-03 | 9 | 42.5 | ¹ | 3 | `42.5)` |  |
| 2019-04 | 8 | 42.3 | ¹ | 48 | `42.3)` |  |
| 2019-05 | 7 | 43.3 | ¹ | 67 | `43.3)` |  |
| 2019-06 | 6 | 42.3 | *¹ | 30 | `42.3|)**` |  |
| 2019-07 | 5 | 49.3 | ¹ | 0 | `49.3)` |  |
| 2019-08 | 4 | 42.3 | ¹ | 9 | `42.3)` |  |
| 2019-09 | 3 | 42.3 |  | 32 | `*4239)` | no_decimal_dot |
| 2019-10 | 2 | 742.5 | ¹ | 1 | `742.5)` | out_of_range |
| 2019-11 | 1 | 43.3 | *¹ | 45 | `*43.3)` |  |
| 2019-12 | 0 | 47.3 |  | 0 | `473)` | no_decimal_dot |

### night / total — mediana: **49.2**  (razón: `high_spread_50.0|std_11.9`, 13 lecturas, rango 21.2–71.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-12 | 12 | 49.2 |  | 89 | `492` | no_decimal_dot |
| 2019-01 | 11 | 49.2 |  | 71 | `49.2` |  |
| 2019-02 | 10 | 49.2 |  | 87 | `492` | no_decimal_dot |
| 2019-03 | 9 | 21.2 |  | 88 | `21.2` |  |
| 2019-04 | 8 | 49.2 |  | 85 | `492` | no_decimal_dot |
| 2019-05 | 7 | 49.2 |  | 90 | `492` | no_decimal_dot |
| 2019-06 | 6 | 49.2 |  | 93 | `492` | no_decimal_dot |
| 2019-07 | 5 | 71.2 |  | 59 | `71.2` |  |
| 2019-08 | 4 | 27.1 | ¹ | 66 | `2713` | no_decimal_dot |
| 2019-09 | 3 | 49.2 |  | 78 | `49.2` |  |
| 2019-10 | 2 | 49.2 |  | 89 | `492` | no_decimal_dot |
| 2019-11 | 1 | 49.2 |  | 92 | `49.2` |  |
| 2019-12 | 0 | 49.2 |  | 84 | `49.2` |  |

### night / avion — mediana: **21.2**  (razón: `high_spread_50.0|std_24.1`, 10 lecturas, rango 21.2–71.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2018-12 | 12 | 71.2 |  | 82 | `71.2` |  |
| 2019-01 | 11 | 21.2 |  | 68 | `212` | no_decimal_dot |
| 2019-02 | 10 | 71.2 |  | 71 | `71.2` |  |
| 2019-03 | 9 | None |  | -1 | `` | row_not_detected |
| 2019-04 | 8 | 21.3 |  | 63 | `213` | no_decimal_dot |
| 2019-05 | 7 | 71.2 |  | 67 | `712` | no_decimal_dot |
| 2019-06 | 6 | 21.2 |  | 71 | `212` | no_decimal_dot |
| 2019-07 | 5 | None |  | -1 | `` | row_not_detected |
| 2019-08 | 4 | None |  | -1 | `` | row_not_detected |
| 2019-09 | 3 | 21.2 |  | 91 | `21.2` |  |
| 2019-10 | 2 | 21.2 |  | 89 | `21.2` |  |
| 2019-11 | 1 | 21.2 |  | 91 | `21.2` |  |
| 2019-12 | 0 | 21.2 |  | 76 | `21.2` |  |

## 2019-01

### night / total — mediana: **50.2**  (razón: `high_spread_38.4|std_16.8`, 13 lecturas, rango 11.8–50.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-01 | 12 | 50.2 |  | 94 | `502` | no_decimal_dot |
| 2019-02 | 11 | 50.2 |  | 70 | `502` | no_decimal_dot |
| 2019-03 | 10 | 11.8 |  | 82 | `11.8` |  |
| 2019-04 | 9 | 50.2 |  | 59 | `502` | no_decimal_dot |
| 2019-05 | 8 | 50.2 |  | 93 | `502` | no_decimal_dot |
| 2019-06 | 7 | 50.2 |  | 90 | `502` | no_decimal_dot |
| 2019-07 | 6 | 11.8 |  | 84 | `118` | no_decimal_dot |
| 2019-08 | 5 | 11.8 |  | 90 | `11.8` |  |
| 2019-09 | 4 | 50.2 |  | 70 | `502)` | no_decimal_dot |
| 2019-10 | 3 | 50.2 |  | 91 | `502` | no_decimal_dot |
| 2019-11 | 2 | 50.2 |  | 91 | `502` | no_decimal_dot |
| 2019-12 | 1 | 50.2 |  | 88 | `502` | no_decimal_dot |
| 2020-01 | 0 | 50.2 |  | 80 | `50.2` |  |

## 2019-02

### evening / avion — mediana: **37.5**  (razón: `high_spread_10.0|std_3.0`, 11 lecturas, rango 37.5–47.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-02 | 12 | 37.5 |  | 34 | `37.5` |  |
| 2019-03 | 11 | 37.5 |  | 78 | `37.5` |  |
| 2019-04 | 10 | 37.5 |  | 86 | `37.5` |  |
| 2019-05 | 9 | 37.5 |  | 81 | `37.5` |  |
| 2019-06 | 8 | 37.5 |  | 64 | `37.5` |  |
| 2019-07 | 7 | 37.5 |  | 75 | `37.5.` |  |
| 2019-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 5 | 47.5 |  | 34 | `47.5` |  |
| 2019-10 | 4 | 37.5 |  | 57 | `37.5` |  |
| 2019-11 | 3 | 37.5 |  | 56 | `37.5:` |  |
| 2019-12 | 2 | 37.5 |  | 75 | `37.5` |  |
| 2020-01 | 1 | None |  | 13 | `3F.5` | parse_error |
| 2020-02 | 0 | 37.5 |  | 44 | `37.5` |  |

### night / total — mediana: **50.2**  (razón: `high_spread_36.7|std_16.6`, 12 lecturas, rango 13.5–50.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-02 | 12 | 50.2 |  | 88 | `502` | no_decimal_dot |
| 2019-03 | 11 | 13.5 |  | 92 | `13.5` |  |
| 2019-04 | 10 | 50.2 |  | 94 | `502` | no_decimal_dot |
| 2019-05 | 9 | None |  | 23 | `5o2` | parse_error |
| 2019-06 | 8 | 50.2 |  | 90 | `502` | no_decimal_dot |
| 2019-07 | 7 | 13.5 |  | 79 | `135` | no_decimal_dot |
| 2019-08 | 6 | 13.5 |  | 87 | `13.5` |  |
| 2019-09 | 5 | 50.2 |  | 75 | `502` | no_decimal_dot |
| 2019-10 | 4 | 50.2 |  | 46 | `502)` | no_decimal_dot |
| 2019-11 | 3 | 50.2 |  | 90 | `502` | no_decimal_dot |
| 2019-12 | 2 | 50.2 |  | 85 | `502` | no_decimal_dot |
| 2020-01 | 1 | 50.2 |  | 83 | `502` | no_decimal_dot |
| 2020-02 | 0 | 50.2 |  | 78 | `50.2` |  |

## 2019-03

### night / total — mediana: **49.2**  (razón: `high_spread_35.1|std_13.7`, 12 lecturas, rango 14.1–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-03 | 12 | 14.1 |  | 95 | `14.1` |  |
| 2019-04 | 11 | 49.2 |  | 72 | `49.2` |  |
| 2019-05 | 10 | 49.2 |  | 84 | `492` | no_decimal_dot |
| 2019-06 | 9 | 49.2 |  | 69 | `492` | no_decimal_dot |
| 2019-07 | 8 | None |  | 46 | `41` | parse_error |
| 2019-08 | 7 | 14.1 |  | 88 | `141` | no_decimal_dot |
| 2019-09 | 6 | 49.2 |  | 78 | `492` | no_decimal_dot |
| 2019-10 | 5 | 49.2 |  | 79 | `492` | no_decimal_dot |
| 2019-11 | 4 | 49.2 |  | 86 | `49.2` |  |
| 2019-12 | 3 | 49.2 |  | 76 | `49.2` |  |
| 2020-01 | 2 | 49.2 |  | 92 | `49.2` |  |
| 2020-02 | 1 | 49.2 |  | 89 | `49.2` |  |
| 2020-03 | 0 | 49.2 |  | 75 | `49.2` |  |

## 2019-04

### day / avion — mediana: **39.0**  (razón: `high_spread_34.9|std_14.1`, 6 lecturas, rango 39.0–73.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-04 | 12 | 39.0 |  | 0 | `39.0` |  |
| 2019-05 | 11 | 39.0 |  | 92 | `39.0` |  |
| 2019-06 | 10 | 39.0 | ¹ | 79 | `39.0)` |  |
| 2019-07 | 9 | 39.0 | ¹ | 9 | `39.0)` |  |
| 2019-08 | 8 | 399.0 | ¹ | 51 | `399.0)` | out_of_range |
| 2019-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 6 | None |  | 0 | `73990)` | parse_error |
| 2019-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2019-12 | 4 | 99.0 |  | 16 | `*990)` | out_of_range |
| 2020-01 | 3 | 73.9 |  | 0 | `7390)` | no_decimal_dot |
| 2020-02 | 2 | 41.2 | *¹ | 32 | `*41.2)*390)*3992` |  |
| 2020-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **48.6**  (razón: `high_spread_26.4|std_9.9`, 13 lecturas, rango 22.2–48.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-04 | 12 | 48.6 |  | 83 | `486` | no_decimal_dot |
| 2019-05 | 11 | 48.6 |  | 21 | `486` | no_decimal_dot |
| 2019-06 | 10 | 48.6 |  | 31 | `486` | no_decimal_dot |
| 2019-07 | 9 | 22.2 |  | 67 | `22.2` |  |
| 2019-08 | 8 | 22.3 |  | 56 | `223` | no_decimal_dot |
| 2019-09 | 7 | 48.6 |  | 39 | `486` | no_decimal_dot |
| 2019-10 | 6 | 48.6 |  | 53 | `486` | no_decimal_dot |
| 2019-11 | 5 | 48.6 |  | 76 | `486` | no_decimal_dot |
| 2019-12 | 4 | 48.6 |  | 85 | `486` | no_decimal_dot |
| 2020-01 | 3 | 48.6 |  | 75 | `486` | no_decimal_dot |
| 2020-02 | 2 | 48.6 |  | 87 | `48.6` |  |
| 2020-03 | 1 | 48.6 |  | 90 | `48.6` |  |
| 2020-04 | 0 | 48.6 |  | 76 | `48.6` |  |

## 2019-05

### day / avion — mediana: **39.2**  (razón: `high_spread_20.7|std_10.3`, 4 lecturas, rango 39.2–59.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-05 | 12 | 39.2 | * | 0 | `**39.2` |  |
| 2019-06 | 11 | 39.2 |  | 88 | `39.2` |  |
| 2019-07 | 10 | 39.2 | ¹ | 44 | `39.2)` |  |
| 2019-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 6 | None |  | 0 | `73992)` | parse_error |
| 2019-12 | 5 | None |  | 21 | `73992` | parse_error |
| 2020-01 | 4 | 397.1 | *¹ | 19 | `*992)*397.1)` | out_of_range |
| 2020-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 2 | None |  | 20 | `*3990)*392)*3971)` | parse_error |
| 2020-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 0 | 59.9 | ¹ | 20 | `5992)` | no_decimal_dot |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-06 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2019-07 | 10 | None |  | -1 | `` | row_not_detected |
| 2019-08 | 9 | None |  | -1 | `` | row_not_detected |
| 2019-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 6 | None |  | 20 | `00` | parse_error |
| 2019-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2019-06

### night / total — mediana: **49.7**  (razón: `high_spread_32.4|std_9.4`, 12 lecturas, rango 17.3–49.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-06 | 12 | 49.7 |  | 85 | `497` | no_decimal_dot |
| 2019-07 | 11 | 17.3 |  | 48 | `173` | no_decimal_dot |
| 2019-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 9 | 49.7 |  | 81 | `497` | no_decimal_dot |
| 2019-10 | 8 | 49.7 |  | 28 | `497` | no_decimal_dot |
| 2019-11 | 7 | 49.7 |  | 63 | `497` | no_decimal_dot |
| 2019-12 | 6 | 49.7 |  | 82 | `497` | no_decimal_dot |
| 2020-01 | 5 | 49.7 |  | 88 | `49.7` |  |
| 2020-02 | 4 | 49.7 |  | 75 | `497` | no_decimal_dot |
| 2020-03 | 3 | 49.7 |  | 84 | `497` | no_decimal_dot |
| 2020-04 | 2 | 49.7 |  | 88 | `49.7` |  |
| 2020-05 | 1 | 49.7 |  | 78 | `49.7` |  |
| 2020-06 | 0 | 49.7 |  | 82 | `49.7` |  |

## 2019-07

### evening / total — mediana: **40.95**  (razón: `high_spread_21.3|only_2_readings`, 2 lecturas, rango 30.3–51.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-08 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2019-12 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 2 | 51.6 |  | 36 | `516` | no_decimal_dot |
| 2020-06 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 0 | 30.3 |  | 93 | `30.3` |  |

### night / total — mediana: **49.2**  (razón: `high_spread_26.7|std_10.0`, 13 lecturas, rango 22.5–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-07 | 12 | 22.5 |  | 80 | `22.5` |  |
| 2019-08 | 11 | 22.5 |  | 63 | `22.5` |  |
| 2019-09 | 10 | 49.2 |  | 69 | `49.2` |  |
| 2019-10 | 9 | 49.2 |  | 85 | `492` | no_decimal_dot |
| 2019-11 | 8 | 49.2 |  | 28 | `492)` | no_decimal_dot |
| 2019-12 | 7 | 49.2 |  | 74 | `49.2` |  |
| 2020-01 | 6 | 49.2 |  | 83 | `492` | no_decimal_dot |
| 2020-02 | 5 | 49.2 |  | 87 | `49.2` |  |
| 2020-03 | 4 | 49.2 |  | 75 | `49.2` |  |
| 2020-04 | 3 | 49.2 |  | 80 | `492` | no_decimal_dot |
| 2020-05 | 2 | 49.2 |  | 88 | `49.2` |  |
| 2020-06 | 1 | 49.2 |  | 80 | `49.2` |  |
| 2020-07 | 0 | 49.2 |  | 80 | `49.2` |  |

## 2019-08

### evening / total — mediana: **48.8**  (razón: `high_spread_18.8|std_6.6`, 8 lecturas, rango 30.0–48.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-09 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 9 | 48.8 |  | 0 | `488` | no_decimal_dot |
| 2019-12 | 8 | 43.8 |  | 48 | `438` | no_decimal_dot |
| 2020-01 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 6 | 48.8 |  | 77 | `488` | no_decimal_dot |
| 2020-03 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 4 | 48.8 |  | 89 | `488` | no_decimal_dot |
| 2020-05 | 3 | 48.8 |  | 35 | `488` | no_decimal_dot |
| 2020-06 | 2 | 48.8 |  | 91 | `488` | no_decimal_dot |
| 2020-07 | 1 | 30.0 |  | 91 | `30.0` |  |
| 2020-08 | 0 | 48.8 |  | 76 | `488` | no_decimal_dot |

## 2019-09

### day / avion — mediana: **45.0**  (razón: `high_spread_32.2|std_14.2`, 8 lecturas, rango 42.5–74.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 11 | 42.5 |  | 63 | `*425` | no_decimal_dot |
| 2019-11 | 10 | 42.5 |  | 41 | `*425` | no_decimal_dot |
| 2019-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 8 | 47.5 |  | 28 | `*475)` | no_decimal_dot |
| 2020-02 | 7 | 42.5 |  | 30 | `*425|` | no_decimal_dot |
| 2020-03 | 6 | 42.5 |  | 40 | `*425)` | no_decimal_dot |
| 2020-04 | 5 | 423.5 | ¹ | 1 | `7423.5` | out_of_range |
| 2020-05 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 2 | 74.2 | ¹ | 11 | `7425)` | no_decimal_dot |
| 2020-08 | 1 | 74.7 | ¹ | 17 | `7475)` | no_decimal_dot |
| 2020-09 | 0 | 47.5 |  | 19 | `475)` | no_decimal_dot |

### evening / total — mediana: **51.3**  (razón: `high_spread_15.1|std_4.4`, 12 lecturas, rango 36.2–51.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-10 | 11 | 51.3 |  | 85 | `513` | no_decimal_dot |
| 2019-11 | 10 | 51.3 |  | 82 | `513` | no_decimal_dot |
| 2019-12 | 9 | 51.3 |  | 76 | `513` | no_decimal_dot |
| 2020-01 | 8 | 51.3 |  | 9 | `513` | no_decimal_dot |
| 2020-02 | 7 | 51.3 |  | 43 | `513` | no_decimal_dot |
| 2020-03 | 6 | 51.3 |  | 39 | `513` | no_decimal_dot |
| 2020-04 | 5 | 51.3 |  | 67 | `513` | no_decimal_dot |
| 2020-05 | 4 | 51.3 |  | 72 | `513` | no_decimal_dot |
| 2020-06 | 3 | 51.3 |  | 90 | `513` | no_decimal_dot |
| 2020-07 | 2 | 36.2 | ¹ | 34 | `36.2)` |  |
| 2020-08 | 1 | 51.3 |  | 76 | `513` | no_decimal_dot |
| 2020-09 | 0 | 51.3 |  | 75 | `513` | no_decimal_dot |

## 2019-10

### day / total — mediana: **56.5**  (razón: `only_1_readings`, 1 lecturas, rango 56.5–56.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 11 | 56.5 |  | 44 | `*565` | no_decimal_dot |
| 2019-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **51.9**  (razón: `high_spread_14.0|std_6.8`, 7 lecturas, rango 37.9–51.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-11 | 11 | 51.9 |  | 93 | `519` | no_decimal_dot |
| 2019-12 | 10 | 51.9 |  | 88 | `519` | no_decimal_dot |
| 2020-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 8 | 51.9 |  | 0 | `519` | no_decimal_dot |
| 2020-03 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 6 | 51.9 |  | 7 | `519` | no_decimal_dot |
| 2020-05 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 3 | 37.9 |  | 19 | `379)` | no_decimal_dot |
| 2020-08 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 1 | 51.9 |  | 79 | `519` | no_decimal_dot |
| 2020-10 | 0 | 37.9 | ¹ | 71 | `37.9)` |  |

### evening / avion — mediana: **37.9**  (razón: `high_spread_16.8|std_5.3`, 10 lecturas, rango 37.9–54.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-10 | 12 | 37.9 |  | 92 | `37.9` |  |
| 2019-11 | 11 | 54.7 |  | 19 | `5479` | no_decimal_dot |
| 2019-12 | 10 | 397.9 | ¹ | 70 | `397.9)` | out_of_range |
| 2020-01 | 9 | 37.9 | * | 18 | `*37.9` |  |
| 2020-02 | 8 | 37.9 |  | 43 | `*379)` | no_decimal_dot |
| 2020-03 | 7 | 37.9 | *¹ | 0 | `*37.9)` |  |
| 2020-04 | 6 | 37.9 | ¹ | 67 | `37.9)` |  |
| 2020-05 | 5 | 37.9 |  | 77 | `379` | no_decimal_dot |
| 2020-06 | 4 | 37.9 |  | 4 | `37.9` |  |
| 2020-07 | 3 | None |  | -1 | `` | row_not_detected |
| 2020-08 | 2 | 37.9 | ¹ | 45 | `37.9)` |  |
| 2020-09 | 1 | 37.9 | *¹ | 60 | `*37.9)` |  |
| 2020-10 | 0 | None |  | -1 | `` | row_not_detected |

## 2019-11

### day / total — mediana: **55.8**  (razón: `only_1_readings`, 1 lecturas, rango 55.8–55.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 9 | None |  | 30 | `*565|*558|` | parse_error |
| 2020-03 | 8 | None |  | 46 | `*565|*558|` | parse_error |
| 2020-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 1 | None |  | 68 | `*565|*558|` | parse_error |
| 2020-11 | 0 | 55.8 |  | 56 | `*558|` | no_decimal_dot |

### evening / total — mediana: **37.4**  (razón: `high_spread_10.0|std_5.8`, 3 lecturas, rango 37.4–47.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2019-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 4 | 47.4 |  | 79 | `474` | no_decimal_dot |
| 2020-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 1 | 37.4 | *¹ | 65 | `*37.4)` |  |
| 2020-11 | 0 | 37.4 | ¹ | 70 | `37.4)` |  |

### evening / avion — mediana: **37.4**  (razón: `high_spread_10.0|std_3.2`, 10 lecturas, rango 37.4–47.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-11 | 12 | 37.4 |  | 37 | `*374` | no_decimal_dot |
| 2019-12 | 11 | 37.4 |  | 84 | `374` | no_decimal_dot |
| 2020-01 | 10 | 37.4 |  | 0 | `374)` | no_decimal_dot |
| 2020-02 | 9 | 37.4 |  | 69 | `*374)` | no_decimal_dot |
| 2020-03 | 8 | 37.4 |  | 0 | `374)` | no_decimal_dot |
| 2020-04 | 7 | 37.4 |  | 34 | `*374)` | no_decimal_dot |
| 2020-05 | 6 | 37.4 |  | 84 | `*374` | no_decimal_dot |
| 2020-06 | 5 | 37.4 |  | 85 | `*374` | no_decimal_dot |
| 2020-07 | 4 | None |  | -1 | `` | row_not_detected |
| 2020-08 | 3 | 47.4 |  | 7 | `*474` | no_decimal_dot |
| 2020-09 | 2 | 37.4 | ¹ | 62 | `37.4)` |  |
| 2020-10 | 1 | None |  | -1 | `` | row_not_detected |
| 2020-11 | 0 | None |  | -1 | `` | row_not_detected |

### night / avion — mediana: **17.5**  (razón: `high_spread_54.2|std_19.2`, 8 lecturas, rango 17.5–71.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-11 | 12 | 717.5 |  | 57 | `717.5` | out_of_range |
| 2019-12 | 11 | 17.5 |  | 67 | `*175` | no_decimal_dot |
| 2020-01 | 10 | 17.5 |  | 62 | `*175` | no_decimal_dot |
| 2020-02 | 9 | 71.7 | ¹ | 37 | `7175` | no_decimal_dot |
| 2020-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 5 | 17.5 |  | 66 | `*175` | no_decimal_dot |
| 2020-07 | 4 | 17.5 | * | 52 | `*17.5` |  |
| 2020-08 | 3 | 17.5 |  | 70 | `*175` | no_decimal_dot |
| 2020-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 1 | 17.5 | * | 71 | `*17.5` |  |
| 2020-11 | 0 | 17.5 |  | 90 | `17.5` |  |

## 2019-12

### evening / total — mediana: **51.8**  (razón: `high_spread_14.7|std_6.4`, 5 lecturas, rango 37.1–51.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-12 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 9 | 51.8 |  | 4 | `518` | no_decimal_dot |
| 2020-04 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 5 | 37.1 |  | 87 | `37.1` |  |
| 2020-08 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 3 | 51.8 |  | 0 | `518` | no_decimal_dot |
| 2020-10 | 2 | None |  | 64 | `41` | parse_error |
| 2020-11 | 1 | 47.1 |  | 67 | `47.1` |  |
| 2020-12 | 0 | 51.8 |  | 78 | `518` | no_decimal_dot |

### night / avion — mediana: **0.0**  (razón: `only_1_readings`, 1 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2019-12 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-01 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 3 | None |  | 57 | `00` | parse_error |
| 2020-10 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2020-11 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2020-12 | 0 | 0.0 |  | 54 | `0` |  |

## 2020-01

### evening / total — mediana: **52.3**  (razón: `high_spread_15.2|std_7.1`, 11 lecturas, rango 37.1–52.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-01 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-02 | 11 | 52.3 |  | 80 | `523` | no_decimal_dot |
| 2020-03 | 10 | 52.3 |  | 86 | `523` | no_decimal_dot |
| 2020-04 | 9 | 52.3 |  | 77 | `523` | no_decimal_dot |
| 2020-05 | 8 | 52.3 |  | 82 | `523` | no_decimal_dot |
| 2020-06 | 7 | 52.3 |  | 37 | `523` | no_decimal_dot |
| 2020-07 | 6 | 37.1 |  | 92 | `37.1` |  |
| 2020-08 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 4 | 52.3 |  | 75 | `523` | no_decimal_dot |
| 2020-10 | 3 | 37.1 |  | 46 | `37.1` |  |
| 2020-11 | 2 | 37.1 |  | 82 | `37.1` |  |
| 2020-12 | 1 | 52.3 |  | 82 | `523` | no_decimal_dot |
| 2021-01 | 0 | 52.3 |  | 87 | `523` | no_decimal_dot |

## 2020-02

### evening / total — mediana: **51.7**  (razón: `high_spread_15.2|std_7.9`, 8 lecturas, rango 36.5–51.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-03 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 8 | 51.7 |  | 19 | `517` | no_decimal_dot |
| 2020-07 | 7 | 36.5 |  | 91 | `36.5` |  |
| 2020-08 | 6 | 51.7 |  | 17 | `517` | no_decimal_dot |
| 2020-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 4 | 36.5 |  | 90 | `36.5` |  |
| 2020-11 | 3 | 36.5 |  | 91 | `36.5` |  |
| 2020-12 | 2 | 51.7 |  | 53 | `517` | no_decimal_dot |
| 2021-01 | 1 | 51.7 |  | 78 | `51.7` |  |
| 2021-02 | 0 | 51.7 |  | 37 | `517` | no_decimal_dot |

## 2020-03

### evening / total — mediana: **51.8**  (razón: `high_spread_17.2|std_8.9`, 8 lecturas, rango 34.6–51.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 11 | 51.8 |  | 30 | `518` | no_decimal_dot |
| 2020-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 9 | 51.8 |  | 4 | `518` | no_decimal_dot |
| 2020-07 | 8 | 34.6 |  | 91 | `34.6` |  |
| 2020-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 5 | 34.6 |  | 84 | `34.6` |  |
| 2020-11 | 4 | 34.6 |  | 91 | `34.6` |  |
| 2020-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 2 | 51.8 |  | 58 | `518` | no_decimal_dot |
| 2021-02 | 1 | 51.8 |  | 91 | `518` | no_decimal_dot |
| 2021-03 | 0 | 51.8 |  | 87 | `518` | no_decimal_dot |

### night / avion — mediana: **0.0**  (razón: `only_2_readings`, 2 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-04 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2020-12 | 3 | 0.0 |  | 38 | `0` |  |
| 2021-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2021-02 | 1 | 0.0 |  | 59 | `0` |  |
| 2021-03 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2020-04

### evening / total — mediana: **39.75**  (razón: `high_spread_23.5|std_12.9`, 6 lecturas, rango 28.0–51.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 9 | 28.0 |  | 86 | `28.0` |  |
| 2020-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 6 | 28.0 |  | 87 | `28.0` |  |
| 2020-11 | 5 | 28.0 |  | 86 | `28.0` |  |
| 2020-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 3 | 51.5 |  | 47 | `515` | no_decimal_dot |
| 2021-02 | 2 | 51.5 |  | 80 | `515` | no_decimal_dot |
| 2021-03 | 1 | 51.5 |  | 86 | `515` | no_decimal_dot |
| 2021-04 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **0.0**  (razón: `only_2_readings`, 2 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-04 | 12 | 0.0 |  | 62 | `0.0` |  |
| 2020-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2020-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2020-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2021-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2021-03 | 1 | 0.0 |  | 46 | `0` |  |
| 2021-04 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2020-05

### evening / total — mediana: **51.6**  (razón: `high_spread_25.0|std_12.9`, 8 lecturas, rango 26.6–51.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-06 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 10 | 26.6 |  | 93 | `26.6` |  |
| 2020-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 7 | 26.6 |  | 91 | `26.6` |  |
| 2020-11 | 6 | 26.6 |  | 93 | `26.6` |  |
| 2020-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 4 | 51.6 |  | 48 | `516` | no_decimal_dot |
| 2021-02 | 3 | 51.6 |  | 76 | `516` | no_decimal_dot |
| 2021-03 | 2 | 51.6 |  | 88 | `516` | no_decimal_dot |
| 2021-04 | 1 | 51.6 |  | 69 | `516` | no_decimal_dot |
| 2021-05 | 0 | 51.6 |  | 76 | `516` | no_decimal_dot |

## 2020-06

### day / avion — mediana: **33.3**  (razón: `high_spread_10.0|std_2.8`, 13 lecturas, rango 33.3–43.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-06 | 12 | 33.3 |  | 54 | `33.3` |  |
| 2020-07 | 11 | 33.3 |  | 84 | `33.3` |  |
| 2020-08 | 10 | 33.3 |  | 87 | `33.3` |  |
| 2020-09 | 9 | 33.3 |  | 84 | `33.3` |  |
| 2020-10 | 8 | 33.3 |  | 87 | `33.3` |  |
| 2020-11 | 7 | 33.3 |  | 82 | `33.3` |  |
| 2020-12 | 6 | 33.3 |  | 56 | `33.3` |  |
| 2021-01 | 5 | 33.3 |  | 81 | `33.3` |  |
| 2021-02 | 4 | 33.3 |  | 75 | `33.3` |  |
| 2021-03 | 3 | 33.3 |  | 82 | `33.3` |  |
| 2021-04 | 2 | 33.3 |  | 67 | `33.3` |  |
| 2021-05 | 1 | 33.3 |  | 81 | `33.3` |  |
| 2021-06 | 0 | 43.3 |  | 67 | `43.3` |  |

### evening / total — mediana: **51.3**  (razón: `high_spread_25.9|std_11.7`, 12 lecturas, rango 25.4–51.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-06 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-07 | 11 | 25.4 |  | 93 | `25.4` |  |
| 2020-08 | 10 | 51.3 |  | 71 | `513` | no_decimal_dot |
| 2020-09 | 9 | 51.3 |  | 82 | `513` | no_decimal_dot |
| 2020-10 | 8 | 25.4 |  | 61 | `25.4` |  |
| 2020-11 | 7 | 25.4 |  | 79 | `25.4` |  |
| 2020-12 | 6 | 51.3 |  | 88 | `513` | no_decimal_dot |
| 2021-01 | 5 | 51.3 |  | 84 | `513` | no_decimal_dot |
| 2021-02 | 4 | 51.3 |  | 85 | `513` | no_decimal_dot |
| 2021-03 | 3 | 51.3 |  | 83 | `513` | no_decimal_dot |
| 2021-04 | 2 | 51.3 |  | 85 | `513` | no_decimal_dot |
| 2021-05 | 1 | 51.3 |  | 90 | `513` | no_decimal_dot |
| 2021-06 | 0 | 51.3 |  | 79 | `513` | no_decimal_dot |

### night / avion — mediana: **0.0**  (razón: `only_1_readings`, 1 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-06 | 12 | 0.0 |  | 62 | `0.0` |  |
| 2020-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2020-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2020-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2021-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2021-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2021-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2021-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2021-06 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2020-07

### evening / total — mediana: **51.9**  (razón: `high_spread_30.2|std_13.3`, 9 lecturas, rango 21.7–51.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-08 | 11 | 51.9 |  | 20 | `519` | no_decimal_dot |
| 2020-09 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 9 | 21.7 |  | 92 | `217` | no_decimal_dot |
| 2020-11 | 8 | 21.7 |  | 87 | `217` | no_decimal_dot |
| 2020-12 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2021-01 | 6 | 51.9 |  | 36 | `519` | no_decimal_dot |
| 2021-02 | 5 | 51.9 |  | 38 | `519` | no_decimal_dot |
| 2021-03 | 4 | 51.9 |  | 61 | `519` | no_decimal_dot |
| 2021-04 | 3 | 51.9 |  | 78 | `519` | no_decimal_dot |
| 2021-05 | 2 | 51.9 |  | 59 | `519` | no_decimal_dot |
| 2021-06 | 1 | 51.9 |  | 84 | `519` | no_decimal_dot |
| 2021-07 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **21.7**  (razón: `high_spread_5.4`, 10 lecturas, rango 21.7–27.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-07 | 12 | None |  | -1 | `` | row_not_detected |
| 2020-08 | 11 | 21.7 |  | 79 | `217` | no_decimal_dot |
| 2020-09 | 10 | 21.7 |  | 88 | `217` | no_decimal_dot |
| 2020-10 | 9 | None |  | -1 | `` | row_not_detected |
| 2020-11 | 8 | None |  | -1 | `` | row_not_detected |
| 2020-12 | 7 | 21.7 |  | 81 | `21.7` |  |
| 2021-01 | 6 | 27.1 | ¹ | 52 | `2717` | no_decimal_dot |
| 2021-02 | 5 | 21.7 |  | 81 | `21.7` |  |
| 2021-03 | 4 | 21.7 |  | 90 | `21.7` |  |
| 2021-04 | 3 | 21.7 |  | 85 | `21.7` |  |
| 2021-05 | 2 | 21.7 |  | 91 | `21.7` |  |
| 2021-06 | 1 | 21.7 |  | 94 | `21.7` |  |
| 2021-07 | 0 | 21.7 |  | 86 | `21.7` |  |

## 2020-08

### evening / total — mediana: **48.0**  (razón: `high_spread_24.8|std_9.3`, 12 lecturas, rango 23.2–48.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-09 | 11 | 48.0 |  | 58 | `480` | no_decimal_dot |
| 2020-10 | 10 | 25.2 |  | 56 | `25.2` |  |
| 2020-11 | 9 | 23.2 |  | 68 | `23.2` |  |
| 2020-12 | 8 | 48.0 |  | 48 | `480` | no_decimal_dot |
| 2021-01 | 7 | 48.0 |  | 73 | `480` | no_decimal_dot |
| 2021-02 | 6 | 48.0 |  | 81 | `480` | no_decimal_dot |
| 2021-03 | 5 | 48.0 |  | 82 | `480` | no_decimal_dot |
| 2021-04 | 4 | 48.0 |  | 87 | `480` | no_decimal_dot |
| 2021-05 | 3 | 48.0 |  | 69 | `480` | no_decimal_dot |
| 2021-06 | 2 | 48.0 |  | 87 | `48.0` |  |
| 2021-07 | 1 | 48.0 |  | 63 | `480` | no_decimal_dot |
| 2021-08 | 0 | 48.0 |  | 84 | `48.0` |  |

## 2020-09

### evening / total — mediana: **51.9**  (razón: `high_spread_23.3|std_9.8`, 10 lecturas, rango 28.6–51.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2020-10 | 11 | 28.6 |  | 65 | `28.6` |  |
| 2020-11 | 10 | 28.6 |  | 83 | `28.6` |  |
| 2020-12 | 9 | 51.9 |  | 84 | `519` | no_decimal_dot |
| 2021-01 | 8 | 51.9 |  | 66 | `519` | no_decimal_dot |
| 2021-02 | 7 | 51.9 |  | 13 | `519` | no_decimal_dot |
| 2021-03 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2021-04 | 5 | 51.9 |  | 0 | `519` | no_decimal_dot |
| 2021-05 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2021-06 | 3 | 51.9 |  | 80 | `519` | no_decimal_dot |
| 2021-07 | 2 | 51.9 |  | 55 | `519` | no_decimal_dot |
| 2021-08 | 1 | 51.9 |  | 89 | `519` | no_decimal_dot |
| 2021-09 | 0 | 51.9 |  | 15 | `519` | no_decimal_dot |

## 2020-10

### evening / total — mediana: **52.1**  (razón: `high_spread_19.4|std_7.5`, 12 lecturas, rango 32.8–52.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-10 | 12 | 32.8 |  | 48 | `32.8` |  |
| 2020-11 | 11 | 32.8 |  | 77 | `32.8` |  |
| 2020-12 | 10 | 52.1 |  | 66 | `521` | no_decimal_dot |
| 2021-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2021-02 | 8 | 52.1 |  | 71 | `521` | no_decimal_dot |
| 2021-03 | 7 | 52.2 |  | 72 | `522` | no_decimal_dot |
| 2021-04 | 6 | 52.1 |  | 53 | `521` | no_decimal_dot |
| 2021-05 | 5 | 52.1 |  | 66 | `521` | no_decimal_dot |
| 2021-06 | 4 | 52.1 |  | 72 | `521` | no_decimal_dot |
| 2021-07 | 3 | 52.1 |  | 88 | `521` | no_decimal_dot |
| 2021-08 | 2 | 52.1 |  | 85 | `521` | no_decimal_dot |
| 2021-09 | 1 | 52.1 |  | 88 | `521` | no_decimal_dot |
| 2021-10 | 0 | 52.1 |  | 72 | `521` | no_decimal_dot |

## 2020-11

### day / avion — mediana: **37.5**  (razón: `high_spread_10.0|std_2.8`, 13 lecturas, rango 37.5–47.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-11 | 12 | 37.5 |  | 77 | `37.5` |  |
| 2020-12 | 11 | 37.5 |  | 79 | `37.5` |  |
| 2021-01 | 10 | 37.5 |  | 58 | `37.5` |  |
| 2021-02 | 9 | 37.5 |  | 67 | `37.5:` |  |
| 2021-03 | 8 | 37.5 |  | 82 | `37.5` |  |
| 2021-04 | 7 | 37.5 |  | 54 | `37.5` |  |
| 2021-05 | 6 | 37.5 |  | 60 | `37.5` |  |
| 2021-06 | 5 | 37.5 |  | 79 | `37.5` |  |
| 2021-07 | 4 | 37.5 |  | 67 | `37.5:` |  |
| 2021-08 | 3 | 37.5 |  | 57 | `37.5` |  |
| 2021-09 | 2 | 37.5 |  | 81 | `37.5` |  |
| 2021-10 | 1 | 37.5 |  | 52 | `37.5` |  |
| 2021-11 | 0 | 47.5 |  | 25 | `475` | no_decimal_dot |

### evening / total — mediana: **51.7**  (razón: `high_spread_9.0|std_3.0`, 9 lecturas, rango 42.7–51.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2020-11 | 12 | 42.7 |  | 38 | `427` | no_decimal_dot |
| 2020-12 | 11 | None |  | 15 | `57` | parse_error |
| 2021-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2021-02 | 9 | 51.7 |  | 2 | `517` | no_decimal_dot |
| 2021-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2021-04 | 7 | 51.7 |  | 70 | `517` | no_decimal_dot |
| 2021-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2021-06 | 5 | 51.7 |  | 73 | `517` | no_decimal_dot |
| 2021-07 | 4 | 51.7 |  | 56 | `517` | no_decimal_dot |
| 2021-08 | 3 | 51.7 |  | 85 | `517` | no_decimal_dot |
| 2021-09 | 2 | 51.7 |  | 71 | `517` | no_decimal_dot |
| 2021-10 | 1 | 51.7 |  | 71 | `51.7` |  |
| 2021-11 | 0 | 51.7 |  | 83 | `517` | no_decimal_dot |

## 2021-01

### day / avion — mediana: **36.5**  (razón: `high_spread_10.0|std_3.2`, 10 lecturas, rango 36.5–46.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-01 | 12 | 36.5 |  | 80 | `*365` | no_decimal_dot |
| 2021-02 | 11 | 46.5 |  | 58 | `*465` | no_decimal_dot |
| 2021-03 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2021-04 | 9 | 36.5 | * | 73 | `*36.5` |  |
| 2021-05 | 8 | 36.5 |  | 47 | `*365)` | no_decimal_dot |
| 2021-06 | 7 | 36.5 |  | 71 | `*365)` | no_decimal_dot |
| 2021-07 | 6 | 36.5 |  | 69 | `*365)` | no_decimal_dot |
| 2021-08 | 5 | 36.5 |  | 29 | `*365` | no_decimal_dot |
| 2021-09 | 4 | 736.5 |  | 35 | `736.5` | out_of_range |
| 2021-10 | 3 | 96.5 |  | 65 | `96.5` | out_of_range |
| 2021-11 | 2 | 36.5 |  | 79 | `36.5` |  |
| 2021-12 | 1 | 36.5 |  | 66 | `365)` | no_decimal_dot |
| 2022-01 | 0 | 36.5 | *¹ | 37 | `*36.5|)` |  |

## 2021-06

### day / avion — mediana: **36.3**  (razón: `high_spread_10.0|std_3.7`, 7 lecturas, rango 36.3–46.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-06 | 12 | 36.3 |  | 66 | `363` | no_decimal_dot |
| 2021-07 | 11 | 46.3 |  | 81 | `463` | no_decimal_dot |
| 2021-08 | 10 | 36.3 | ¹ | 69 | `36.35)` |  |
| 2021-09 | 9 | 736.3 | ¹ | 33 | `736.3)` | out_of_range |
| 2021-10 | 8 | 36.3 | *¹ | 44 | `*36.3)` |  |
| 2021-11 | 7 | 96.3 |  | 38 | `*963)` | out_of_range |
| 2021-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2022-01 | 5 | 736.3 | ¹ | 0 | `736.3)` | out_of_range |
| 2022-02 | 4 | 38.1 | *¹ | 27 | `*38.1)736.3)*38.7` |  |
| 2022-03 | 3 | 736.3 | ¹ | 0 | `736.3)` | out_of_range |
| 2022-04 | 2 | 736.3 | ¹ | 0 | `736.3)` | out_of_range |
| 2022-05 | 1 | 36.3 | * | 62 | `*36.3` |  |
| 2022-06 | 0 | 36.3 | ¹ | 23 | `36.3")` |  |

### evening / avion — mediana: **21.1**  (razón: `high_spread_50.0|std_26.4`, 9 lecturas, rango 21.1–71.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-06 | 12 | 21.1 |  | 49 | `21.1` |  |
| 2021-07 | 11 | 71.1 |  | 43 | `711` | no_decimal_dot |
| 2021-08 | 10 | 21.1 |  | 39 | `211` | no_decimal_dot |
| 2021-09 | 9 | 21.1 |  | 75 | `21.1` |  |
| 2021-10 | 8 | 71.1 |  | 77 | `711` | no_decimal_dot |
| 2021-11 | 7 | 21.1 | ¹ | 22 | `21.1)` |  |
| 2021-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2022-01 | 5 | 71.1 |  | 77 | `71.1` |  |
| 2022-02 | 4 | 71.1 |  | 66 | `71.1` |  |
| 2022-03 | 3 | 271.1 |  | 67 | `271.1` | out_of_range |
| 2022-04 | 2 | 271.1 |  | 72 | `271.1` | out_of_range |
| 2022-05 | 1 | 271.1 |  | 71 | `271.1` | out_of_range |
| 2022-06 | 0 | 21.1 |  | 82 | `21.1` |  |

## 2021-07

### day / avion — mediana: **38.7**  (razón: `high_spread_35.1|std_10.7`, 11 lecturas, rango 38.7–73.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-07 | 12 | 38.7 | * | 56 | `*38.7` |  |
| 2021-08 | 11 | 48.7 |  | 0 | `487` | no_decimal_dot |
| 2021-09 | 10 | None |  | 23 | `*387)*378)` | parse_error |
| 2021-10 | 9 | 38.7 |  | 76 | `*387` | no_decimal_dot |
| 2021-11 | 8 | 38.7 |  | 58 | `*387)` | no_decimal_dot |
| 2021-12 | 7 | 38.7 |  | 58 | `*387)` | no_decimal_dot |
| 2022-01 | 6 | 38.7 | ¹ | 77 | `38.7)` |  |
| 2022-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2022-03 | 4 | 38.7 | * | 3 | `*38.7` |  |
| 2022-04 | 3 | 38.7 | * | 0 | `*38.7` |  |
| 2022-05 | 2 | 73.8 | ¹ | 0 | `7387` | no_decimal_dot |
| 2022-06 | 1 | 38.7 | ¹ | 56 | `3877` | no_decimal_dot |
| 2022-07 | 0 | 38.7 | ¹ | 49 | `38.7)` |  |

### evening / avion — mediana: **44.0**  (razón: `high_spread_55.2|std_28.8`, 12 lecturas, rango 16.4–71.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-07 | 12 | 16.4 | * | 40 | `*16.4` |  |
| 2021-08 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2021-09 | 10 | 71.6 | ¹ | 0 | `7164)` | no_decimal_dot |
| 2021-10 | 9 | 71.6 | ¹ | 25 | `7164]` | no_decimal_dot |
| 2021-11 | 8 | 16.4 |  | 22 | `*164)` | no_decimal_dot |
| 2021-12 | 7 | 16.4 |  | 9 | `*164)` | no_decimal_dot |
| 2022-01 | 6 | 71.6 | ¹ | 46 | `7164)` | no_decimal_dot |
| 2022-02 | 5 | 16.4 |  | 48 | `*164` | no_decimal_dot |
| 2022-03 | 4 | 71.6 | ¹ | 17 | `7164` | no_decimal_dot |
| 2022-04 | 3 | 71.6 | ¹ | 7 | `7164` | no_decimal_dot |
| 2022-05 | 2 | 71.6 | ¹ | 5 | `7164` | no_decimal_dot |
| 2022-06 | 1 | 16.4 |  | 93 | `164` | no_decimal_dot |
| 2022-07 | 0 | 16.4 |  | 92 | `16.4` |  |

## 2021-08

### day / avion — mediana: **37.8**  (razón: `high_spread_35.9|std_14.4`, 11 lecturas, rango 37.8–73.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-08 | 12 | 37.8 |  | 86 | `37.8` |  |
| 2021-09 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2021-10 | 10 | 37.8 |  | 92 | `37.8` |  |
| 2021-11 | 9 | 37.8 |  | 27 | `*378)` | no_decimal_dot |
| 2021-12 | 8 | 37.8 |  | 21 | `*378)>` | no_decimal_dot |
| 2022-01 | 7 | 47.8 |  | 29 | `*478)` | no_decimal_dot |
| 2022-02 | 6 | 73.7 |  | 5 | `7378)` | no_decimal_dot |
| 2022-03 | 5 | 73.7 |  | 11 | `7378)` | no_decimal_dot |
| 2022-04 | 4 | 737.8 | ¹ | 12 | `737.8)` | out_of_range |
| 2022-05 | 3 | 37.8 |  | 34 | `*378)` | no_decimal_dot |
| 2022-06 | 2 | 37.8 |  | 38 | `378%` | no_decimal_dot |
| 2022-07 | 1 | 37.8 |  | 2 | `378` | no_decimal_dot |
| 2022-08 | 0 | 37.8 |  | 63 | `378)` | no_decimal_dot |

## 2021-09

### evening / avion — mediana: **32.8**  (razón: `std_2.4`, 13 lecturas, rango 32.8–37.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-09 | 12 | 32.8 |  | 85 | `32.8` |  |
| 2021-10 | 11 | 32.8 |  | 86 | `32.8` |  |
| 2021-11 | 10 | 32.8 |  | 85 | `32.8` |  |
| 2021-12 | 9 | 32.8 |  | 79 | `32.8` |  |
| 2022-01 | 8 | 32.8 |  | 84 | `32.8` |  |
| 2022-02 | 7 | 32.8 |  | 91 | `32.8` |  |
| 2022-03 | 6 | 32.8 |  | 93 | `32.8` |  |
| 2022-04 | 5 | 32.8 |  | 90 | `32.8` |  |
| 2022-05 | 4 | 32.8 |  | 83 | `32.8` |  |
| 2022-06 | 3 | 37.8 |  | 60 | `378` | no_decimal_dot |
| 2022-07 | 2 | 37.8 |  | 78 | `37.8` |  |
| 2022-08 | 1 | 37.8 |  | 75 | `37.8` |  |
| 2022-09 | 0 | 37.8 |  | 73 | `37.8` |  |

### night / avion — mediana: **28.0**  (razón: `high_spread_6.0`, 13 lecturas, rango 22.0–28.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-09 | 12 | 28.0 |  | 89 | `28.0` |  |
| 2021-10 | 11 | 28.0 |  | 87 | `28.0` |  |
| 2021-11 | 10 | 22.0 |  | 78 | `22.0` |  |
| 2021-12 | 9 | 28.0 |  | 80 | `28.0` |  |
| 2022-01 | 8 | 28.0 |  | 84 | `28.0` |  |
| 2022-02 | 7 | 28.0 |  | 84 | `28.0` |  |
| 2022-03 | 6 | 28.0 |  | 80 | `28.0` |  |
| 2022-04 | 5 | 28.0 |  | 80 | `28.0` |  |
| 2022-05 | 4 | 28.0 |  | 81 | `28.0` |  |
| 2022-06 | 3 | 28.0 |  | 82 | `28.0` |  |
| 2022-07 | 2 | 28.0 |  | 88 | `28.0` |  |
| 2022-08 | 1 | 28.0 |  | 88 | `28.0` |  |
| 2022-09 | 0 | 28.0 |  | 75 | `28.0` |  |

## 2021-11

### evening / avion — mediana: **37.2**  (razón: `high_spread_10.0|std_2.8`, 13 lecturas, rango 37.2–47.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-11 | 12 | 37.2 |  | 31 | `37.2` |  |
| 2021-12 | 11 | 47.2 | ¹ | 77 | `47.2)` |  |
| 2022-01 | 10 | 37.2 | * | 69 | `*37.2` |  |
| 2022-02 | 9 | 37.2 | * | 82 | `*37.2` |  |
| 2022-03 | 8 | 37.2 | *¹ | 84 | `*37.2)` |  |
| 2022-04 | 7 | 37.2 | *¹ | 61 | `*37.2)` |  |
| 2022-05 | 6 | 37.2 | *¹ | 68 | `*37.2)` |  |
| 2022-06 | 5 | 37.2 |  | 85 | `37.2` |  |
| 2022-07 | 4 | 37.2 |  | 80 | `37.2` |  |
| 2022-08 | 3 | 37.2 |  | 80 | `37.2` |  |
| 2022-09 | 2 | 37.2 |  | 86 | `37.2` |  |
| 2022-10 | 1 | 37.2 |  | 86 | `37.2` |  |
| 2022-11 | 0 | 37.2 |  | 91 | `37.2` |  |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2021-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2021-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2022-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2022-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2022-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2022-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2022-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2022-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2022-07 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2022-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2022-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2022-10 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2022-11 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2022-01

### day / avion — mediana: **41.2**  (razón: `high_spread_32.9|std_11.0`, 9 lecturas, rango 41.2–74.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-01 | 12 | None |  | 0 | `"42` | parse_error |
| 2022-02 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2022-03 | 10 | 74.1 | ¹ | 12 | `7412)` | no_decimal_dot |
| 2022-04 | 9 | 741.2 | ¹ | 46 | `741.2)` | out_of_range |
| 2022-05 | 8 | 741.2 | ¹ | 39 | `741.2)` | out_of_range |
| 2022-06 | 7 | 41.2 | ¹ | 24 | `41.27)` |  |
| 2022-07 | 6 | 41.2 |  | 45 | `41.2` |  |
| 2022-08 | 5 | 41.2 |  | 51 | `41.2` |  |
| 2022-09 | 4 | 41.2 |  | 52 | `41.2` |  |
| 2022-10 | 3 | 41.2 | ¹ | 54 | `41.27` |  |
| 2022-11 | 2 | 41.2 | ¹ | 52 | `41.2"` |  |
| 2022-12 | 1 | 41.2 | ¹ | 7 | `41.2"` |  |
| 2023-01 | 0 | 41.2 | ¹ | 32 | `41.2"!` |  |

### evening / avion — mediana: **35.6**  (razón: `high_spread_37.9|std_11.4`, 11 lecturas, rango 35.6–73.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-01 | 12 | 35.6 |  | 11 | `35.6` |  |
| 2022-02 | 11 | 35.6 | * | 82 | `*35.6` |  |
| 2022-03 | 10 | 73.5 | ¹ | 22 | `7356)` | no_decimal_dot |
| 2022-04 | 9 | 735.6 | ¹ | 30 | `735.6)` | out_of_range |
| 2022-05 | 8 | 735.6 | ¹ | 10 | `735.6)` | out_of_range |
| 2022-06 | 7 | 35.6 |  | 89 | `35.6` |  |
| 2022-07 | 6 | 35.6 |  | 91 | `35.6` |  |
| 2022-08 | 5 | 35.6 |  | 91 | `35.6` |  |
| 2022-09 | 4 | 35.6 |  | 90 | `35.6` |  |
| 2022-10 | 3 | 35.6 |  | 90 | `35.6` |  |
| 2022-11 | 2 | 35.6 |  | 78 | `35.6` |  |
| 2022-12 | 1 | 35.6 |  | 78 | `35.6` |  |
| 2023-01 | 0 | 35.6 |  | 92 | `35.6` |  |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-01 | 12 | None |  | 69 | `72` | parse_error |
| 2022-02 | 11 | None |  | 73 | `72` | parse_error |
| 2022-03 | 10 | None |  | 51 | `72` | parse_error |
| 2022-04 | 9 | None |  | 74 | `72` | parse_error |
| 2022-05 | 8 | None |  | 75 | `72` | parse_error |
| 2022-06 | 7 | None |  | 77 | `72` | parse_error |
| 2022-07 | 6 | None |  | 67 | `7.2` | parse_error |
| 2022-08 | 5 | None |  | 67 | `7.2` | parse_error |
| 2022-09 | 4 | None |  | 78 | `7.2` | parse_error |
| 2022-10 | 3 | None |  | 78 | `7.2` | parse_error |
| 2022-11 | 2 | None |  | 66 | `7.2` | parse_error |
| 2022-12 | 1 | None |  | 66 | `7.2` | parse_error |
| 2023-01 | 0 | None |  | 77 | `72` | parse_error |

## 2022-02

### night / avion — mediana: **0.0**  (razón: `only_2_readings`, 2 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-03 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2022-04 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2022-05 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2022-06 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2022-07 | 7 | 0.0 |  | 46 | `0` |  |
| 2022-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2022-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2022-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2022-11 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 0 | 0.0 |  | 46 | `0` |  |

## 2022-03

### day / avion — mediana: **39.8**  (razón: `high_spread_34.1|std_9.5`, 13 lecturas, rango 39.8–73.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-03 | 12 | 39.8 | * | 12 | `*39.8` |  |
| 2022-04 | 11 | 73.9 |  | 0 | `7398` | no_decimal_dot |
| 2022-05 | 10 | 39.8 | * | 49 | `*39.8` |  |
| 2022-06 | 9 | 39.8 | ¹ | 83 | `39.87` |  |
| 2022-07 | 8 | 39.8 | ¹ | 0 | `39.87` |  |
| 2022-08 | 7 | 39.8 | ¹ | 20 | `39.87)` |  |
| 2022-09 | 6 | 39.8 |  | 51 | `398°` | no_decimal_dot |
| 2022-10 | 5 | 39.8 | ¹ | 17 | `39.84` |  |
| 2022-11 | 4 | 39.8 |  | 58 | `39.8` |  |
| 2022-12 | 3 | 39.8 | ¹ | 61 | `39.87)` |  |
| 2023-01 | 2 | 39.8 | ¹ | 60 | `39.87` |  |
| 2023-02 | 1 | 39.8 |  | 29 | `39.8` |  |
| 2023-03 | 0 | 39.8 | ¹ | 42 | `39.8"!` |  |

## 2022-04

### night / avion — mediana: **21.6**  (razón: `high_spread_50.0|std_25.3`, 13 lecturas, rango 21.6–71.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-04 | 12 | 71.6 |  | 81 | `71.6` |  |
| 2022-05 | 11 | 21.6 |  | 72 | `21.6` |  |
| 2022-06 | 10 | 21.6 |  | 78 | `21.6` |  |
| 2022-07 | 9 | 21.6 |  | 78 | `21.6` |  |
| 2022-08 | 8 | 71.6 |  | 73 | `71.6` |  |
| 2022-09 | 7 | 71.6 |  | 73 | `71.6` |  |
| 2022-10 | 6 | 71.6 |  | 81 | `71.6` |  |
| 2022-11 | 5 | 71.6 |  | 81 | `71.6` |  |
| 2022-12 | 4 | 21.6 |  | 68 | `21.6` |  |
| 2023-01 | 3 | 21.6 |  | 68 | `21.6` |  |
| 2023-02 | 2 | 21.6 |  | 85 | `21.6` |  |
| 2023-03 | 1 | 21.6 |  | 85 | `21.6` |  |
| 2023-04 | 0 | 21.6 |  | 73 | `21.6` |  |

## 2022-05

### night / avion — mediana: **0.0**  (razón: `only_1_readings`, 1 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-06 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2022-07 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2022-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2022-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2022-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2022-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 0 | 0.0 |  | 46 | `0` |  |

## 2022-07

### night / avion — mediana: **0.0**  (razón: `only_1_readings`, 1 lecturas, rango 0.0–0.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-08 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2022-09 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2022-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2022-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 7 | 0.0 |  | 46 | `0` |  |
| 2023-01 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 0 | None |  | -1 | `` | row_not_detected |

## 2022-10

### evening / total — mediana: **51.6**  (razón: `only_1_readings`, 1 lecturas, rango 51.6–51.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-11 | 11 | 51.6 |  | 31 | `516` | no_decimal_dot |
| 2022-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2022-11

### day / total — mediana: **54.6**  (razón: `only_2_readings`, 2 lecturas, rango 54.6–54.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 10 | 54.6 |  | 86 | `546` | no_decimal_dot |
| 2023-02 | 9 | 54.6 |  | 65 | `546` | no_decimal_dot |
| 2023-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **51.5**  (razón: `only_2_readings`, 2 lecturas, rango 51.5–51.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 11 | 51.5 |  | 86 | `515` | no_decimal_dot |
| 2023-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 8 | 51.5 |  | 72 | `515` | no_decimal_dot |
| 2023-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2022-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 4 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2022-12

### day / total — mediana: **54.4**  (razón: `only_1_readings`, 1 lecturas, rango 54.4–54.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-12 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-02 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 7 | 54.4 |  | 63 | `544` | no_decimal_dot |
| 2023-06 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **50.7**  (razón: `only_2_readings`, 2 lecturas, rango 50.7–50.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2022-12 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-01 | 11 | 50.7 |  | 60 | `507` | no_decimal_dot |
| 2023-02 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 6 | 50.7 |  | 33 | `507` | no_decimal_dot |
| 2023-07 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-02

### evening / total — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **50.0**  (razón: `only_2_readings`, 2 lecturas, rango 50.0–50.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 11 | 50.0 |  | 80 | `500` | no_decimal_dot |
| 2023-04 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 9 | 50.0 |  | 64 | `500` | no_decimal_dot |
| 2023-06 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-02 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-03 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 7 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-03

### evening / total — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **50.4**  (razón: `only_2_readings`, 2 lecturas, rango 50.4–50.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 11 | 50.4 |  | 73 | `504` | no_decimal_dot |
| 2023-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 9 | 50.4 |  | 80 | `504` | no_decimal_dot |
| 2023-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-04 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 8 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-04

### day / total — mediana: **53.9**  (razón: `only_2_readings`, 2 lecturas, rango 53.9–53.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 11 | 53.9 |  | 92 | `539` | no_decimal_dot |
| 2023-06 | 10 | 53.9 |  | 46 | `539` | no_decimal_dot |
| 2023-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **50.2**  (razón: `only_2_readings`, 2 lecturas, rango 50.2–50.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 11 | 50.2 |  | 87 | `502` | no_decimal_dot |
| 2023-06 | 10 | 50.2 |  | 54 | `502` | no_decimal_dot |
| 2023-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **49.1**  (razón: `only_2_readings`, 2 lecturas, rango 49.1–49.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 11 | 49.1 |  | 78 | `491` | no_decimal_dot |
| 2023-06 | 10 | 49.1 |  | 90 | `491` | no_decimal_dot |
| 2023-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 9 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-05

### day / total — mediana: **54.4**  (razón: `only_1_readings`, 1 lecturas, rango 54.4–54.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 11 | 54.4 |  | 87 | `544` | no_decimal_dot |
| 2023-07 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### day / avion — mediana: **37.7**  (razón: `only_1_readings`, 1 lecturas, rango 37.7–37.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | None |  | 35 | `37777` | parse_error |
| 2023-06 | 11 | 37.7 | ¹ | 39 | `37.77"` |  |
| 2023-07 | 10 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **None**  (razón: `no_valid_readings`, 13 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-07 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **33.3**  (razón: `only_2_readings`, 2 lecturas, rango 33.3–33.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | 33.3 |  | 59 | `33.3` |  |
| 2023-06 | 11 | 33.3 |  | 58 | `33.3` |  |
| 2023-07 | 10 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **50.3**  (razón: `only_1_readings`, 1 lecturas, rango 50.3–50.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2023-06 | 11 | 50.3 |  | 80 | `503` | no_decimal_dot |
| 2023-07 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **25.8**  (razón: `only_1_readings`, 1 lecturas, rango 25.8–25.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-05 | 12 | 25.8 |  | 76 | `25.8.` |  |
| 2023-06 | 11 | None |  | 80 | `2.8` | parse_error |
| 2023-07 | 10 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-06

### day / total — mediana: **54.6**  (razón: `only_1_readings`, 1 lecturas, rango 54.6–54.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 54.6 | ¹ | 25 | `5467` | no_decimal_dot |
| 2023-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### day / avion — mediana: **38.0**  (razón: `only_1_readings`, 1 lecturas, rango 38.0–38.0)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 38.0 | ¹ | 55 | `38.07` |  |
| 2023-07 | 11 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **52.4**  (razón: `only_1_readings`, 1 lecturas, rango 52.4–52.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 52.4 | ¹ | 40 | `5247` | no_decimal_dot |
| 2023-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **31.5**  (razón: `only_1_readings`, 1 lecturas, rango 31.5–31.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 31.5 |  | 35 | `315°)` | no_decimal_dot |
| 2023-07 | 11 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **49.9**  (razón: `only_1_readings`, 1 lecturas, rango 49.9–49.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 49.9 | ¹ | 55 | `4997` | no_decimal_dot |
| 2023-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **22.3**  (razón: `only_1_readings`, 1 lecturas, rango 22.3–22.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-06 | 12 | 22.3 | ¹ | 27 | `2237)` | no_decimal_dot |
| 2023-07 | 11 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2023-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2023-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2023-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2023-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2023-07

### night / total — mediana: **37.5**  (razón: `high_spread_17.9|std_5.4`, 11 lecturas, rango 19.6–37.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-07 | 12 | 19.6 |  | 77 | `19.6` |  |
| 2023-08 | 11 | 37.5 |  | 90 | `375` | no_decimal_dot |
| 2023-09 | 10 | 37.5 |  | 73 | `375` | no_decimal_dot |
| 2023-10 | 9 | 37.5 |  | 89 | `375` | no_decimal_dot |
| 2023-11 | 8 | 37.5 |  | 74 | `375` | no_decimal_dot |
| 2023-12 | 7 | 37.5 |  | 64 | `375` | no_decimal_dot |
| 2024-01 | 6 | 37.5 |  | 88 | `375` | no_decimal_dot |
| 2024-02 | 5 | 37.5 |  | 84 | `375` | no_decimal_dot |
| 2024-03 | 4 | 37.5 |  | 43 | `375` | no_decimal_dot |
| 2024-04 | 3 | 37.5 |  | 45 | `375` | no_decimal_dot |
| 2024-05 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2024-07 | 0 | 37.5 |  | 46 | `375` | no_decimal_dot |

### night / avion — mediana: **19.6**  (razón: `high_spread_6.0`, 12 lecturas, rango 13.6–19.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-07 | 12 | None |  | -1 | `` | row_not_detected |
| 2023-08 | 11 | 19.6 |  | 65 | `19.6` |  |
| 2023-09 | 10 | 19.6 |  | 53 | `19.6` |  |
| 2023-10 | 9 | 19.6 |  | 59 | `19.6` |  |
| 2023-11 | 8 | 19.6 |  | 91 | `19.6` |  |
| 2023-12 | 7 | 19.6 |  | 88 | `19.6` |  |
| 2024-01 | 6 | 19.6 |  | 84 | `19.6` |  |
| 2024-02 | 5 | 19.6 |  | 84 | `19.6` |  |
| 2024-03 | 4 | 19.6 |  | 66 | `196` | no_decimal_dot |
| 2024-04 | 3 | 19.6 |  | 70 | `196` | no_decimal_dot |
| 2024-05 | 2 | 19.6 |  | 44 | `196` | no_decimal_dot |
| 2024-06 | 1 | 13.6 |  | 53 | `136` | no_decimal_dot |
| 2024-07 | 0 | 18.6 |  | 66 | `186` | no_decimal_dot |

## 2023-08

### evening / avion — mediana: **43.9**  (razón: `high_spread_20.0|std_8.2`, 6 lecturas, rango 43.9–63.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-08 | 12 | 43.9 |  | 67 | `43.9` |  |
| 2023-09 | 11 | None |  | 51 | `6.9` | parse_error |
| 2023-10 | 10 | None |  | 33 | `5.9` | parse_error |
| 2023-11 | 9 | None |  | 22 | `5.9` | parse_error |
| 2023-12 | 8 | None |  | 84 | `3.9` | parse_error |
| 2024-01 | 7 | None |  | 44 | `85` | parse_error |
| 2024-02 | 6 | None |  | 46 | `65` | parse_error |
| 2024-03 | 5 | 43.9 |  | 72 | `43,9` |  |
| 2024-04 | 4 | 43.9 |  | 64 | `43,9` |  |
| 2024-05 | 3 | 63.9 |  | 40 | `639` | no_decimal_dot |
| 2024-06 | 2 | 43.9 |  | 84 | `439` | no_decimal_dot |
| 2024-07 | 1 | 43.9 |  | 34 | `439.` | no_decimal_dot |
| 2024-08 | 0 | None |  | -1 | `` | row_not_detected |

## 2023-11

### night / avion — mediana: **22.2**  (razón: `high_spread_53.0|std_16.5`, 10 lecturas, rango 21.7–74.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2023-11 | 12 | 21.7 |  | 82 | `21.7` |  |
| 2023-12 | 11 | 21.7 |  | 77 | `21.7` |  |
| 2024-01 | 10 | 21.7 |  | 82 | `21.7` |  |
| 2024-02 | 9 | 21.7 |  | 76 | `217` | no_decimal_dot |
| 2024-03 | 8 | 24.7 |  | 60 | `247` | no_decimal_dot |
| 2024-04 | 7 | 74.7 |  | 53 | `747` | no_decimal_dot |
| 2024-05 | 6 | 24.7 |  | 64 | `247` | no_decimal_dot |
| 2024-06 | 5 | None |  | 61 | `27` | parse_error |
| 2024-07 | 4 | None |  | 52 | `27` | parse_error |
| 2024-08 | 3 | 22.7 |  | 59 | `227` | no_decimal_dot |
| 2024-09 | 2 | 21.7 |  | 70 | `21,7` |  |
| 2024-10 | 1 | 24.7 |  | 27 | `247` | no_decimal_dot |
| 2024-11 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2024-01

### evening / total — mediana: **49.2**  (razón: `high_spread_9.0|std_3.7`, 11 lecturas, rango 40.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-01 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2024-02 | 11 | 49.2 |  | 86 | `49.2` |  |
| 2024-03 | 10 | 49.2 |  | 68 | `49,2` |  |
| 2024-04 | 9 | 49.2 |  | 53 | `49.2` |  |
| 2024-05 | 8 | 40.2 |  | 43 | `402` | no_decimal_dot |
| 2024-06 | 7 | 49.2 |  | 64 | `49,2` |  |
| 2024-07 | 6 | 49.2 |  | 62 | `49.2` |  |
| 2024-08 | 5 | 49.2 |  | 69 | `49,2` |  |
| 2024-09 | 4 | 49.2 |  | 74 | `49,2` |  |
| 2024-10 | 3 | 40.2 |  | 54 | `402` | no_decimal_dot |
| 2024-11 | 2 | 49.2 |  | 70 | `492` | no_decimal_dot |
| 2024-12 | 1 | None |  | 33 | `438492450` | parse_error |
| 2025-01 | 0 | 45.2 |  | 54 | `452` | no_decimal_dot |

## 2024-03

### day / total — mediana: **54.1**  (razón: `only_1_readings`, 1 lecturas, rango 54.1–54.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-03 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2024-04 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2024-05 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2024-06 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2024-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2024-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2024-09 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2024-10 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2024-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2025-03 | 0 | 54.1 |  | 67 | `541` | no_decimal_dot |

### night / avion — mediana: **23.2**  (razón: `high_spread_50.0|std_24.2`, 10 lecturas, rango 23.2–73.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-03 | 12 | 23.2 |  | 2 | `232,` | no_decimal_dot |
| 2024-04 | 11 | 23.2 |  | 43 | `232` | no_decimal_dot |
| 2024-05 | 10 | 23.2 |  | 43 | `232` | no_decimal_dot |
| 2024-06 | 9 | 73.2 |  | 47 | `732` | no_decimal_dot |
| 2024-07 | 8 | 23.2 |  | 49 | `232` | no_decimal_dot |
| 2024-08 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2024-09 | 6 | None |  | 42 | `72` | parse_error |
| 2024-10 | 5 | 23.2 |  | 59 | `232` | no_decimal_dot |
| 2024-11 | 4 | 23.2 |  | 38 | `232` | no_decimal_dot |
| 2024-12 | 3 | 73.2 |  | 40 | `732` | no_decimal_dot |
| 2025-01 | 2 | 73.2 |  | 43 | `732` | no_decimal_dot |
| 2025-02 | 1 | None |  | 59 | `206732` | parse_error |
| 2025-03 | 0 | 23.2 |  | 56 | `232` | no_decimal_dot |

## 2024-04

### night / avion — mediana: **17.7**  (razón: `high_spread_30.0|std_11.7`, 12 lecturas, rango 17.7–47.7)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-04 | 12 | 17.7 |  | 47 | `177` | no_decimal_dot |
| 2024-05 | 11 | 17.7 |  | 52 | `177` | no_decimal_dot |
| 2024-06 | 10 | 17.7 |  | 42 | `177` | no_decimal_dot |
| 2024-07 | 9 | 17.7 |  | 0 | `17.79` |  |
| 2024-08 | 8 | None |  | 41 | `232/177` | parse_error |
| 2024-09 | 7 | 17.7 |  | 54 | `177` | no_decimal_dot |
| 2024-10 | 6 | 17.7 |  | 61 | `177` | no_decimal_dot |
| 2024-11 | 5 | 47.7 |  | 47 | `477` | no_decimal_dot |
| 2024-12 | 4 | 17.7 |  | 52 | `177` | no_decimal_dot |
| 2025-01 | 3 | 17.7 |  | 53 | `177` | no_decimal_dot |
| 2025-02 | 2 | 47.7 |  | 62 | `477` | no_decimal_dot |
| 2025-03 | 1 | 17.7 |  | 56 | `17,7` |  |
| 2025-04 | 0 | 17.7 |  | 54 | `17,7` |  |

## 2024-06

### evening / total — mediana: **49.1**  (razón: `high_spread_9.0|std_2.8`, 12 lecturas, rango 40.1–49.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-06 | 12 | 49.1 |  | 53 | `49,1` |  |
| 2024-07 | 11 | 45.1 |  | 52 | `451` | no_decimal_dot |
| 2024-08 | 10 | 49.1 |  | 53 | `49,1` |  |
| 2024-09 | 9 | 49.1 |  | 68 | `49,1` |  |
| 2024-10 | 8 | 40.1 |  | 46 | `401` | no_decimal_dot |
| 2024-11 | 7 | 49.1 |  | 49 | `49,1` |  |
| 2024-12 | 6 | 49.1 |  | 47 | `491` | no_decimal_dot |
| 2025-01 | 5 | None |  | 9 | `91` | parse_error |
| 2025-02 | 4 | 49.1 |  | 52 | `49.1` |  |
| 2025-03 | 3 | 49.1 |  | 62 | `491` | no_decimal_dot |
| 2025-04 | 2 | 49.1 |  | 59 | `491` | no_decimal_dot |
| 2025-05 | 1 | 45.1 |  | 45 | `45,1` |  |
| 2025-06 | 0 | 49.1 |  | 58 | `49.1` |  |

### night / total — mediana: **42.5**  (razón: `only_2_readings`, 2 lecturas, rango 42.5–42.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-06 | 12 | 42.5 |  | 54 | `425` | no_decimal_dot |
| 2024-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2024-08 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2024-09 | 9 | 42.5 |  | 44 | `425` | no_decimal_dot |
| 2024-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 7 | None |  | 54 | `25` | parse_error |
| 2024-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 4 | None |  | 51 | `25` | parse_error |
| 2025-03 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 2 | None |  | 64 | `25` | parse_error |
| 2025-05 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2025-06 | 0 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **23.3**  (razón: `high_spread_50.0|std_20.4`, 6 lecturas, rango 23.3–73.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-06 | 12 | 23.3 |  | 28 | `233` | no_decimal_dot |
| 2024-07 | 11 | None |  | 51 | `33` | parse_error |
| 2024-08 | 10 | 23.3 |  | 37 | `233` | no_decimal_dot |
| 2024-09 | 9 | 23.3 |  | 38 | `233` | no_decimal_dot |
| 2024-10 | 8 | None |  | 50 | `7S` | parse_error |
| 2024-11 | 7 | 23.3 |  | 20 | `233` | no_decimal_dot |
| 2024-12 | 6 | 79.3 | ¹ | 42 | `79-33` | out_of_range |
| 2025-01 | 5 | 73.3 |  | 46 | `733` | no_decimal_dot |
| 2025-02 | 4 | 23.3 |  | 45 | `233` | no_decimal_dot |
| 2025-03 | 3 | None |  | 55 | `73` | parse_error |
| 2025-04 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2025-05 | 1 | None |  | -1 | `` | row_not_detected |
| 2025-06 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2024-07

### night / total — mediana: **38.6**  (razón: `std_2.2`, 12 lecturas, rango 33.6–38.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-07 | 12 | 38.6 |  | 62 | `386` | no_decimal_dot |
| 2024-08 | 11 | 38.6 |  | 36 | `386` | no_decimal_dot |
| 2024-09 | 10 | 38.6 |  | 44 | `386` | no_decimal_dot |
| 2024-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 8 | 38.6 |  | 54 | `386` | no_decimal_dot |
| 2024-12 | 7 | 35.6 |  | 61 | `356` | no_decimal_dot |
| 2025-01 | 6 | 33.6 |  | 65 | `336` | no_decimal_dot |
| 2025-02 | 5 | 38.6 |  | 43 | `386` | no_decimal_dot |
| 2025-03 | 4 | 38.6 |  | 51 | `386` | no_decimal_dot |
| 2025-04 | 3 | 33.6 |  | 42 | `336` | no_decimal_dot |
| 2025-05 | 2 | 38.6 |  | 61 | `386` | no_decimal_dot |
| 2025-06 | 1 | 33.6 |  | 39 | `336)` | no_decimal_dot |
| 2025-07 | 0 | 36.6 |  | 54 | `366` | no_decimal_dot |

## 2024-08

### night / total — mediana: **44.1**  (razón: `high_spread_13.7|std_7.9`, 3 lecturas, rango 30.5–44.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2024-09 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2024-10 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2024-12 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 6 | 44.1 |  | 38 | `441` | no_decimal_dot |
| 2025-03 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 4 | 44.2 |  | 59 | `442` | no_decimal_dot |
| 2025-05 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-06 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 1 | None |  | 25 | `41` | parse_error |
| 2025-08 | 0 | 30.5 |  | 47 | `305` | no_decimal_dot |

## 2024-09

### night / total — mediana: **41.5**  (razón: `high_spread_17.7|std_7.4`, 5 lecturas, rango 26.8–44.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2024-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 10 | 41.5 |  | 44 | `415` | no_decimal_dot |
| 2024-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-03 | 6 | 44.5 |  | 42 | `445` | no_decimal_dot |
| 2025-04 | 5 | 44.5 |  | 57 | `445` | no_decimal_dot |
| 2025-05 | 4 | None |  | 0 | `15` | parse_error |
| 2025-06 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 2 | None |  | 35 | `1s` | parse_error |
| 2025-08 | 1 | 26.8 |  | 71 | `268` | no_decimal_dot |
| 2025-09 | 0 | 41.5 |  | 45 | `415` | no_decimal_dot |

## 2024-10

### day / avion — mediana: **48.4**  (razón: `std_2.0`, 12 lecturas, rango 43.4–48.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-10 | 12 | 48.4 |  | 34 | `484` | no_decimal_dot |
| 2024-11 | 11 | 48.4 |  | 75 | `484` | no_decimal_dot |
| 2024-12 | 10 | 45.4 |  | 55 | `454` | no_decimal_dot |
| 2025-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 8 | 48.4 |  | 56 | `484` | no_decimal_dot |
| 2025-03 | 7 | 48.4 |  | 48 | `484` | no_decimal_dot |
| 2025-04 | 6 | 48.4 |  | 61 | `484` | no_decimal_dot |
| 2025-05 | 5 | 43.4 |  | 75 | `434` | no_decimal_dot |
| 2025-06 | 4 | 48.4 |  | 68 | `484` | no_decimal_dot |
| 2025-07 | 3 | 43.4 |  | 70 | `434` | no_decimal_dot |
| 2025-08 | 2 | 48.4 |  | 62 | `484` | no_decimal_dot |
| 2025-09 | 1 | 48.4 |  | 60 | `484` | no_decimal_dot |
| 2025-10 | 0 | 48.4 |  | 48 | `484` | no_decimal_dot |

### night / total — mediana: **42.9**  (razón: `high_spread_25.2|std_14.5`, 3 lecturas, rango 17.7–42.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2024-11 | 11 | 42.9 |  | 30 | `429` | no_decimal_dot |
| 2024-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-03 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-05 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2025-06 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 2 | 17.7 |  | 68 | `177` | no_decimal_dot |
| 2025-09 | 1 | 42.9 |  | 49 | `429` | no_decimal_dot |
| 2025-10 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2024-11

### evening / total — mediana: **47.0**  (razón: `std_2.3`, 10 lecturas, rango 43.5–48.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-11 | 12 | 48.5 |  | 35 | `48,5` |  |
| 2024-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 10 | None |  | 36 | `95` | parse_error |
| 2025-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-03 | 8 | 43.5 |  | 47 | `435` | no_decimal_dot |
| 2025-04 | 7 | 48.5 |  | 65 | `485` | no_decimal_dot |
| 2025-05 | 6 | 43.5 |  | 55 | `435` | no_decimal_dot |
| 2025-06 | 5 | 45.5 |  | 69 | `455` | no_decimal_dot |
| 2025-07 | 4 | 48.5 |  | 64 | `485` | no_decimal_dot |
| 2025-08 | 3 | 43.5 |  | 49 | `435` | no_decimal_dot |
| 2025-09 | 2 | 45.5 |  | 57 | `455` | no_decimal_dot |
| 2025-10 | 1 | 48.5 |  | 40 | `485` | no_decimal_dot |
| 2025-11 | 0 | 48.5 |  | 53 | `485` | no_decimal_dot |

### night / total — mediana: **40.9**  (razón: `high_spread_17.4|std_7.8`, 5 lecturas, rango 23.5–40.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-11 | 12 | 40.9 |  | 33 | `409` | no_decimal_dot |
| 2024-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-02 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-03 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-05 | 6 | None |  | 8 | `09` | parse_error |
| 2025-06 | 5 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 4 | 40.9 |  | 57 | `409` | no_decimal_dot |
| 2025-08 | 3 | 23.5 |  | 62 | `235` | no_decimal_dot |
| 2025-09 | 2 | 40.9 |  | 57 | `409` | no_decimal_dot |
| 2025-10 | 1 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 0 | 40.9 |  | 63 | `409` | no_decimal_dot |

## 2024-12

### night / total — mediana: **39.5**  (razón: `high_spread_15.6|std_5.5`, 10 lecturas, rango 23.9–39.5)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-12 | 12 | 39.5 |  | 33 | `395°` | no_decimal_dot |
| 2025-01 | 11 | 39.5 |  | 51 | `395` | no_decimal_dot |
| 2025-02 | 10 | 38.5 |  | 39 | `385` | no_decimal_dot |
| 2025-03 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 8 | 38.5 |  | 50 | `385` | no_decimal_dot |
| 2025-05 | 7 | 39.5 |  | 56 | `395` | no_decimal_dot |
| 2025-06 | 6 | 39.5 |  | 10 | `395` | no_decimal_dot |
| 2025-07 | 5 | 29.5 |  | 44 | `295` | no_decimal_dot |
| 2025-08 | 4 | 23.9 |  | 48 | `239` | no_decimal_dot |
| 2025-09 | 3 | 39.5 |  | 43 | `395` | no_decimal_dot |
| 2025-10 | 2 | None |  | 50 | `09395` | parse_error |
| 2025-11 | 1 | 39.5 |  | 53 | `395` | no_decimal_dot |
| 2025-12 | 0 | 99.5 |  | 64 | `995` | out_of_range |

### night / avion — mediana: **23.9**  (razón: `high_spread_50.0|std_15.8`, 10 lecturas, rango 23.9–73.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2024-12 | 12 | 73.9 |  | 37 | `739` | no_decimal_dot |
| 2025-01 | 11 | 23.9 |  | 55 | `239` | no_decimal_dot |
| 2025-02 | 10 | 23.9 |  | 28 | `239` | no_decimal_dot |
| 2025-03 | 9 | 23.9 |  | 37 | `239` | no_decimal_dot |
| 2025-04 | 8 | 23.9 |  | 56 | `239` | no_decimal_dot |
| 2025-05 | 7 | None |  | -1 | `` | row_not_detected |
| 2025-06 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 5 | 23.9 |  | 56 | `239` | no_decimal_dot |
| 2025-08 | 4 | None |  | -1 | `` | row_not_detected |
| 2025-09 | 3 | 23.9 |  | 56 | `239` | no_decimal_dot |
| 2025-10 | 2 | 23.9 |  | 56 | `239` | no_decimal_dot |
| 2025-11 | 1 | 23.9 |  | 56 | `239` | no_decimal_dot |
| 2025-12 | 0 | 23.9 |  | 36 | `239.` | no_decimal_dot |

## 2025-01

### day / avion — mediana: **49.2**  (razón: `high_spread_6.0`, 12 lecturas, rango 43.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-01 | 12 | 49.2 |  | 16 | `49,2` |  |
| 2025-02 | 11 | 49.2 |  | 24 | `49.2` |  |
| 2025-03 | 10 | 45.2 |  | 63 | `452` | no_decimal_dot |
| 2025-04 | 9 | 49.2 |  | 62 | `492` | no_decimal_dot |
| 2025-05 | 8 | 49.2 |  | 56 | `492` | no_decimal_dot |
| 2025-06 | 7 | 49.2 |  | 43 | `492` | no_decimal_dot |
| 2025-07 | 6 | 49.2 |  | 60 | `49.2` |  |
| 2025-08 | 5 | 43.2 |  | 59 | `432` | no_decimal_dot |
| 2025-09 | 4 | 49.2 |  | 52 | `49.2` |  |
| 2025-10 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 2 | 49.2 |  | 61 | `49,2` |  |
| 2025-12 | 1 | 48.2 |  | 46 | `482` | no_decimal_dot |
| 2026-01 | 0 | 49.2 |  | 69 | `492` | no_decimal_dot |

### night / total — mediana: **43.6**  (razón: `high_spread_25.8|std_11.5`, 5 lecturas, rango 17.8–43.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-01 | 12 | 43.6 |  | 52 | `436` | no_decimal_dot |
| 2025-02 | 11 | 43.6 |  | 48 | `436` | no_decimal_dot |
| 2025-03 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-04 | 9 | None |  | 38 | `3S` | parse_error |
| 2025-05 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-06 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 5 | 17.8 |  | 67 | `178` | no_decimal_dot |
| 2025-09 | 4 | 43.6 |  | 65 | `436` | no_decimal_dot |
| 2025-10 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 1 | 43.6 |  | 62 | `436` | no_decimal_dot |
| 2026-01 | 0 | None |  | -1 | `` | no_token_at_pos |

## 2025-02

### night / total — mediana: **39.8**  (razón: `high_spread_10.0|std_3.8`, 11 lecturas, rango 29.8–39.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-02 | 12 | 30.8 |  | 57 | `308` | no_decimal_dot |
| 2025-03 | 11 | 39.8 |  | 38 | `398` | no_decimal_dot |
| 2025-04 | 10 | 38.8 |  | 35 | `388` | no_decimal_dot |
| 2025-05 | 9 | 39.8 |  | 50 | `398` | no_decimal_dot |
| 2025-06 | 8 | None |  | 45 | `3S` | parse_error |
| 2025-07 | 7 | 29.8 |  | 52 | `298` | no_decimal_dot |
| 2025-08 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-09 | 5 | 39.8 |  | 65 | `398` | no_decimal_dot |
| 2025-10 | 4 | 39.8 |  | 65 | `398` | no_decimal_dot |
| 2025-11 | 3 | 39.8 |  | 51 | `398` | no_decimal_dot |
| 2025-12 | 2 | 39.8 |  | 63 | `398` | no_decimal_dot |
| 2026-01 | 1 | 39.8 |  | 56 | `398` | no_decimal_dot |
| 2026-02 | 0 | 39.8 |  | 58 | `398` | no_decimal_dot |

## 2025-03

### night / total — mediana: **43.9**  (razón: `high_spread_24.4|std_9.3`, 5 lecturas, rango 25.5–49.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-03 | 12 | 49.9 |  | 61 | `499` | no_decimal_dot |
| 2025-04 | 11 | 43.9 |  | 43 | `439` | no_decimal_dot |
| 2025-05 | 10 | None |  | 42 | `9)` | parse_error |
| 2025-06 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 7 | 25.5 |  | 39 | `2550` | no_decimal_dot |
| 2025-09 | 6 | 43.9 |  | 63 | `439` | no_decimal_dot |
| 2025-10 | 5 | 43.9 |  | 65 | `439` | no_decimal_dot |
| 2025-11 | 4 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 2 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 1 | None |  | -1 | `` | no_token_at_pos |

## 2025-04

### night / total — mediana: **44.1**  (razón: `only_1_readings`, 1 lecturas, rango 44.1–44.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-04 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-05 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-06 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-09 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 5 | None |  | 38 | `41` | parse_error |
| 2025-12 | 4 | 44.1 |  | 54 | `441` | no_decimal_dot |
| 2026-01 | 3 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 2 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **23.4**  (razón: `only_2_readings`, 2 lecturas, rango 21.9–24.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-04 | 12 | 21.9 |  | 42 | `219°` | no_decimal_dot |
| 2025-05 | 11 | None |  | -1 | `` | row_not_detected |
| 2025-06 | 10 | None |  | 48 | `79` | parse_error |
| 2025-07 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 8 | None |  | -1 | `` | row_not_detected |
| 2025-09 | 7 | None |  | 57 | `29` | parse_error |
| 2025-10 | 6 | None |  | 48 | `29` | parse_error |
| 2025-11 | 5 | None |  | 52 | `29` | parse_error |
| 2025-12 | 4 | None |  | 64 | `29` | parse_error |
| 2026-01 | 3 | 24.9 |  | 33 | `249` | no_decimal_dot |
| 2026-02 | 2 | None |  | 42 | `7,9` | parse_error |

## 2025-06

### day / avion — mediana: **49.2**  (razón: `high_spread_6.0|std_2.3`, 9 lecturas, rango 43.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-06 | 12 | 49.2 |  | 18 | `492°` | no_decimal_dot |
| 2025-07 | 11 | 49.2 |  | 61 | `49.2` |  |
| 2025-08 | 10 | 45.2 |  | 62 | `452` | no_decimal_dot |
| 2025-09 | 9 | 49.2 |  | 59 | `492` | no_decimal_dot |
| 2025-10 | 8 | 49.2 |  | 56 | `492` | no_decimal_dot |
| 2025-11 | 7 | 49.2 |  | 48 | `49,2` |  |
| 2025-12 | 6 | 49.2 |  | 61 | `49.2` |  |
| 2026-01 | 5 | 43.2 |  | 60 | `432` | no_decimal_dot |
| 2026-02 | 4 | 49.2 |  | 53 | `492` | no_decimal_dot |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 9 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-06 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-07 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 10 | None |  | 38 | `14` | parse_error |
| 2025-09 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 7 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 5 | None |  | 43 | `48328` | parse_error |
| 2026-02 | 4 | None |  | -1 | `` | no_token_at_pos |

## 2025-07

### day / avion — mediana: **49.4**  (razón: `high_spread_6.0|std_2.1`, 8 lecturas, rango 43.4–49.4)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-07 | 12 | 49.4 |  | 69 | `49.4` |  |
| 2025-08 | 11 | 49.4 |  | 70 | `494` | no_decimal_dot |
| 2025-09 | 10 | 49.4 |  | 65 | `494` | no_decimal_dot |
| 2025-10 | 9 | 49.4 |  | 63 | `494` | no_decimal_dot |
| 2025-11 | 8 | 49.4 |  | 74 | `494` | no_decimal_dot |
| 2025-12 | 7 | 49.4 |  | 78 | `494` | no_decimal_dot |
| 2026-01 | 6 | 49.4 |  | 69 | `494` | no_decimal_dot |
| 2026-02 | 5 | 43.4 |  | 67 | `434` | no_decimal_dot |

### night / total — mediana: **41.8**  (razón: `high_spread_11.9|std_5.3`, 5 lecturas, rango 29.9–41.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-07 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-08 | 11 | 29.9 |  | 62 | `299` | no_decimal_dot |
| 2025-09 | 10 | 41.8 |  | 40 | `418` | no_decimal_dot |
| 2025-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 7 | 41.8 |  | 28 | `418` | no_decimal_dot |
| 2026-01 | 6 | 41.8 |  | 62 | `418` | no_decimal_dot |
| 2026-02 | 5 | 41.8 |  | 52 | `418` | no_decimal_dot |

### night / avion — mediana: **23.9**  (razón: `high_spread_6.0|std_3.3`, 5 lecturas, rango 23.9–29.9)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-07 | 12 | 23.9 |  | 41 | `239` | no_decimal_dot |
| 2025-08 | 11 | None |  | -1 | `` | row_not_detected |
| 2025-09 | 10 | 29.9 |  | 63 | `299` | no_decimal_dot |
| 2025-10 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 8 | 23.9 |  | 67 | `239` | no_decimal_dot |
| 2025-12 | 7 | 29.9 |  | 56 | `299` | no_decimal_dot |
| 2026-01 | 6 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 5 | 23.9 |  | 66 | `239` | no_decimal_dot |

## 2025-08

### day / avion — mediana: **48.2**  (razón: `std_2.2`, 6 lecturas, rango 43.2–48.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-08 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-09 | 11 | 48.2 |  | 46 | `482°` | no_decimal_dot |
| 2025-10 | 10 | 48.2 |  | 64 | `482"` | no_decimal_dot |
| 2025-11 | 9 | 48.2 |  | 67 | `482"` | no_decimal_dot |
| 2025-12 | 8 | 43.2 |  | 63 | `432"` | no_decimal_dot |
| 2026-01 | 7 | 48.2 |  | 73 | `482"` | no_decimal_dot |
| 2026-02 | 6 | 45.2 |  | 66 | `452"` | no_decimal_dot |

### night / avion — mediana: **22.1**  (razón: `high_spread_50.0|std_28.9`, 3 lecturas, rango 22.1–72.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-08 | 12 | None |  | -1 | `` | row_not_detected |
| 2025-09 | 11 | 22.1 |  | 51 | `221"` | no_decimal_dot |
| 2025-10 | 10 | None |  | 54 | `2939217` | parse_error |
| 2025-11 | 9 | 22.1 |  | 69 | `221"` | no_decimal_dot |
| 2025-12 | 8 | None |  | 47 | `21°` | parse_error |
| 2026-01 | 7 | None |  | 49 | `299221"` | parse_error |
| 2026-02 | 6 | 72.1 |  | 40 | `721")` | no_decimal_dot |

## 2025-09

### day / total — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

### day / avion — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 6 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-09 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-10 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 8 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 7 | None |  | -1 | `` | no_token_at_pos |

## 2025-10

### day / total — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

### day / avion — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

### evening / total — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **None**  (razón: `no_valid_readings`, 5 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-10 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-11 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 9 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 8 | None |  | -1 | `` | no_token_at_pos |

## 2025-11

### day / avion — mediana: **None**  (razón: `no_valid_readings`, 4 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 10 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 9 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **48.1**  (razón: `only_2_readings`, 2 lecturas, rango 48.1–48.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-11 | 12 | 48.1 |  | 45 | `481"` | no_decimal_dot |
| 2025-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 10 | 48.1 |  | 0 | `481*)` | no_decimal_dot |
| 2026-02 | 9 | None |  | -1 | `` | no_token_at_pos |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 4 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-11 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2025-12 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2026-01 | 10 | 81.2 |  | 6 | `812"` | out_of_range |
| 2026-02 | 9 | None |  | -1 | `` | no_token_at_pos |

## 2025-12

### day / avion — mediana: **52.1**  (razón: `only_1_readings`, 1 lecturas, rango 52.1–52.1)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-12 | 12 | 52.1 |  | 10 | `521` | no_decimal_dot |
| 2026-01 | 11 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 10 | None |  | -1 | `` | no_token_at_pos |

### evening / avion — mediana: **49.2**  (razón: `std_2.3`, 3 lecturas, rango 45.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-12 | 12 | 45.2 |  | 29 | `452°` | no_decimal_dot |
| 2026-01 | 11 | 49.2 |  | 79 | `49,2` |  |
| 2026-02 | 10 | 49.2 |  | 87 | `49,2` |  |

### night / total — mediana: **35.6**  (razón: `only_2_readings`, 2 lecturas, rango 35.6–35.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2025-12 | 12 | 35.6 |  | 37 | `356` | no_decimal_dot |
| 2026-01 | 11 | None |  | 44 | `96` | parse_error |
| 2026-02 | 10 | 35.6 |  | 64 | `356` | no_decimal_dot |

## 2026-01

### day / total — mediana: **53.3**  (razón: `only_2_readings`, 2 lecturas, rango 53.3–53.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | 53.3 |  | 57 | `533,` | no_decimal_dot |
| 2026-02 | 11 | 53.3 |  | 43 | `533` | no_decimal_dot |

### day / avion — mediana: **52.8**  (razón: `only_2_readings`, 2 lecturas, rango 51.3–54.3)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | 51.3 |  | 37 | `513,` | no_decimal_dot |
| 2026-02 | 11 | 54.3 |  | 55 | `543` | no_decimal_dot |

### evening / total — mediana: **50.2**  (razón: `only_2_readings`, 2 lecturas, rango 50.2–50.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | 50.2 |  | 61 | `50.2` |  |
| 2026-02 | 11 | 50.2 |  | 53 | `502` | no_decimal_dot |

### evening / avion — mediana: **48.8**  (razón: `only_2_readings`, 2 lecturas, rango 48.8–48.8)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | 48.8 |  | 22 | `488` | no_decimal_dot |
| 2026-02 | 11 | 48.8 |  | 77 | `488` | no_decimal_dot |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 2 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | None |  | -1 | `` | no_token_at_pos |
| 2026-02 | 11 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **27.55**  (razón: `only_2_readings`, 2 lecturas, rango 27.5–27.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-01 | 12 | 27.6 |  | 49 | `276` | no_decimal_dot |
| 2026-02 | 11 | 27.5 |  | 66 | `275` | no_decimal_dot |

## 2026-02

### day / total — mediana: **58.6**  (razón: `only_1_readings`, 1 lecturas, rango 58.6–58.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | 58.6 |  | 41 | `586` | no_decimal_dot |

### day / avion — mediana: **49.2**  (razón: `only_1_readings`, 1 lecturas, rango 49.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | 49.2 |  | 56 | `49,2` |  |

### evening / total — mediana: **49.2**  (razón: `only_1_readings`, 1 lecturas, rango 49.2–49.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | 49.2 |  | 36 | `492` | no_decimal_dot |

### evening / avion — mediana: **47.2**  (razón: `only_1_readings`, 1 lecturas, rango 47.2–47.2)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | 47.2 |  | 21 | `47,2` |  |

### night / total — mediana: **None**  (razón: `no_valid_readings`, 1 lecturas, rango None–None)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | None |  | -1 | `` | no_token_at_pos |

### night / avion — mediana: **26.6**  (razón: `only_1_readings`, 1 lecturas, rango 26.6–26.6)

| informe | pos | valor | flags | conf | raw | issue |
|---|---|---|---|---|---|---|
| 2026-02 | 12 | 26.6 |  | 23 | `266,` | no_decimal_dot |
