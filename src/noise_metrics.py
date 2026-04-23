"""Métricas acústicas derivadas de los LAeq por periodo.

Calcula Lden (day-evening-night) y Lnight según Directiva 2002/49/CE,
y compara con umbrales de:
- Real Decreto 1367/2007 (España)
- WHO Environmental Noise Guidelines 2018 (aircraft)
- Directiva 2002/49/CE (mapeo estratégico)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

# Duraciones en horas de cada periodo según RD 1367/2007 (idéntico al EU para cálculo Lden)
DAY_HOURS = 12      # 07-19h
EVENING_HOURS = 4   # 19-23h
NIGHT_HOURS = 8     # 23-07h

# Penalizaciones de la métrica Lden (Directiva 2002/49/CE, Anexo I)
EVENING_PENALTY_DB = 5
NIGHT_PENALTY_DB = 10


# Umbrales (dB)

# Real Decreto 1367/2007, Anexo II, Tabla A — zona residencial, tipo a) uso residencial
RD_1367_RESIDENTIAL = {
    "day": 65,
    "evening": 65,
    "night": 55,
}

# WHO Environmental Noise Guidelines 2018 — aircraft noise, "strong recommendation"
# https://www.who.int/europe/publications/i/item/9789289053563
WHO_2018_AIRCRAFT = {
    "lden": 45,
    "lnight": 40,
}

# Directiva 2002/49/CE no fija valores límite propios (los delega a estados miembros)
# pero obliga a mapear superficies expuestas a >55 dB Lden y >50 dB Lnight
# en "major airports" (> 50.000 movimientos anuales — Barajas supera con creces).
EU_2002_49_REPORTING_THRESHOLDS = {
    "lden": 55,
    "lnight": 50,
}


def compute_lden(laeq_day: float, laeq_evening: float, laeq_night: float) -> float:
    """Calcula Lden según Directiva 2002/49/CE (Anexo I).

    Lden = 10·log10( (1/24) · (12·10^(Ld/10) + 4·10^((Le+5)/10) + 8·10^((Ln+10)/10)) )
    """
    numerator = (
        DAY_HOURS * 10 ** (laeq_day / 10)
        + EVENING_HOURS * 10 ** ((laeq_evening + EVENING_PENALTY_DB) / 10)
        + NIGHT_HOURS * 10 ** ((laeq_night + NIGHT_PENALTY_DB) / 10)
    )
    return 10 * math.log10(numerator / 24)


def compute_lnight(laeq_night: float) -> float:
    """Lnight es el LAeq del periodo noche (23-07h) sin penalización.

    En la Directiva 2002/49/CE se define como indicador separado, pero
    numéricamente es el LAeq_noche tal cual lo publica AENA.
    """
    return laeq_night


@dataclass
class ComplianceResult:
    label: str
    value: float
    threshold: float
    compliant: bool
    margin_db: float  # positivo = bajo umbral; negativo = excede

    def __str__(self) -> str:
        status = "✓ cumple" if self.compliant else "✗ EXCEDE"
        sign = "+" if self.margin_db >= 0 else ""
        return f"{self.label}: {self.value:.1f} vs {self.threshold} dB → {status} ({sign}{self.margin_db:.1f} dB de margen)"


def check_compliance(value: float, threshold: float, label: str) -> ComplianceResult:
    """Compara un valor medido con un umbral. `margin_db > 0` significa que cumple."""
    margin = threshold - value
    return ComplianceResult(
        label=label, value=value, threshold=threshold,
        compliant=margin >= 0, margin_db=margin,
    )
