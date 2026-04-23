"""Tests de las métricas acústicas (Lden, Lnight, compliance)."""

import math

from src.noise_metrics import (
    RD_1367_RESIDENTIAL,
    WHO_2018_AIRCRAFT,
    check_compliance,
    compute_lden,
    compute_lnight,
)


class TestComputeLden:
    def test_flat_level(self):
        """Si los tres periodos tienen el mismo LAeq L, el Lden se acerca a L+6.4 dB
        por las penalizaciones tarde (+5) y noche (+10)."""
        # Con LAeq=60 en todos los periodos:
        result = compute_lden(60, 60, 60)
        # Esperado ≈ 10·log10((12·10^6 + 4·10^6.5 + 8·10^7)/24) ≈ 66.4 dB
        assert abs(result - 66.4) < 0.1

    def test_silent_night(self):
        """Si la noche está silenciosa, la tarde con +5 dB domina sobre el día."""
        result = compute_lden(60, 60, 0)
        assert abs(result - 60.1) < 0.2

    def test_tmr16_2025_total(self):
        """Los valores oficiales del TMR-16 2025 Total (55.1/49.9/43.6)
        deberían dar Lden ≈ 54.6 dB."""
        result = compute_lden(55.1, 49.9, 43.6)
        assert abs(result - 54.6) < 0.2

    def test_tmr16_2025_avion(self):
        """TMR-16 2025 Avión (50.4/47.2/25.0) → Lden ≈ 49.2 dB."""
        result = compute_lden(50.4, 47.2, 25.0)
        assert abs(result - 49.2) < 0.2


class TestComputeLnight:
    def test_passthrough(self):
        assert compute_lnight(43.6) == 43.6


class TestCompliance:
    def test_compliant_below_threshold(self):
        r = check_compliance(50.0, 65.0, "LAeq día")
        assert r.compliant
        assert r.margin_db == 15.0

    def test_exceeds_threshold(self):
        r = check_compliance(49.2, WHO_2018_AIRCRAFT["lden"], "Lden Avión TMR-16")
        assert not r.compliant
        assert abs(r.margin_db - (-4.2)) < 0.01

    def test_rd_1367_thresholds_values(self):
        assert RD_1367_RESIDENTIAL["night"] == 55
        assert RD_1367_RESIDENTIAL["day"] == 65

    def test_who_2018_values(self):
        assert WHO_2018_AIRCRAFT["lden"] == 45
        assert WHO_2018_AIRCRAFT["lnight"] == 40
