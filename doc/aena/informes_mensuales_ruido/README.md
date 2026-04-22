# Informes mensuales de ruido — AENA Madrid-Barajas

**⚠️ Los PDFs de esta carpeta no están en el repo.** Son unos ~656 MB en total (2017–2026, ~10 PDFs/año) y se han dejado fuera del control de versiones para no inflar el repositorio. Están listados en `.gitignore`.

## Dónde descargarlos

AENA publica estos informes de forma pública en:

https://www.aena.es/es/corporativa/sostenibilidad-ambiental/ruido/sistemas-de-monitorado-de-ruido/as-madrid-barajas.html

Sección **"Mediciones acústicas"** → informes mensuales del aeropuerto Madrid-Barajas.

## Estructura esperada

Para que los scripts del repo (`scripts/extract_config_sur.py`, `src/noise_report_parser.py`) encuentren los PDFs, colócalos así:

```
doc/aena/informes_mensuales_ruido/
├── 2017/
│   ├── 2017-01_informe_ruido.pdf
│   ├── 2017-02_informe_ruido.pdf
│   └── ...
├── 2018/
│   └── ...
└── 2026/
    └── ...
```

Convención de nombre: `YYYY-MM_informe_ruido.pdf`.

## Informes anuales

Los informes **anuales** (23 MB en total) sí están incluidos en el repo, en `doc/aena/informes_anuales_ruido/` (2016–2025).
