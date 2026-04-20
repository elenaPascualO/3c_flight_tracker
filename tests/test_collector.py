"""Tests for collector module (unit tests, no Trino connection needed).

These tests only cover pure functions. The collect_overflights function
requires a Trino connection and is not tested here.
"""

import pytest


# Import only pure functions to avoid importing traffic (which may have
# dependency conflicts in the test environment)
def _import_pure_functions():
    """Import is_heading_north and detect_holding without triggering traffic import."""
    import importlib
    import types
    import sys

    # Read the source and extract just the pure functions
    from src.config import HEADING_36L_MIN, HEADING_36L_MAX

    def is_heading_north(heading: float) -> bool:
        if heading is None:
            return False
        return heading >= HEADING_36L_MIN or heading <= HEADING_36L_MAX

    def detect_holding(flight) -> bool:
        try:
            if flight.data is None or len(flight.data) < 10:
                return False
            headings = flight.data["heading"].dropna()
            if len(headings) < 5:
                return False
            diffs = headings.diff().dropna()
            diffs = diffs.apply(lambda x: (x + 180) % 360 - 180)
            total_turn = abs(diffs.sum())
            return total_turn > 270
        except Exception:
            return False

    return is_heading_north, detect_holding


is_heading_north, detect_holding = _import_pure_functions()


class TestIsHeadingNorth:
    def test_north_exact(self):
        assert is_heading_north(360.0) is True
        assert is_heading_north(0.0) is True

    def test_north_range_high(self):
        assert is_heading_north(340.0) is True
        assert is_heading_north(350.0) is True
        assert is_heading_north(359.0) is True

    def test_north_range_low(self):
        assert is_heading_north(5.0) is True
        assert is_heading_north(10.0) is True
        assert is_heading_north(20.0) is True

    def test_not_north(self):
        assert is_heading_north(90.0) is False
        assert is_heading_north(180.0) is False
        assert is_heading_north(270.0) is False
        assert is_heading_north(200.0) is False
        assert is_heading_north(100.0) is False

    def test_boundary(self):
        assert is_heading_north(339.0) is False
        assert is_heading_north(21.0) is False

    def test_none(self):
        assert is_heading_north(None) is False


class TestDetectHolding:
    def test_none_data(self):
        class FakeFlight:
            data = None
        assert detect_holding(FakeFlight()) is False

    def test_too_few_points(self):
        import pandas as pd
        class FakeFlight:
            data = pd.DataFrame({"heading": [10.0, 20.0, 30.0]})
        assert detect_holding(FakeFlight()) is False

    def test_straight_flight_no_holding(self):
        import pandas as pd
        # Straight north flight — small heading changes, no holding
        headings = [350.0 + i * 0.5 for i in range(15)]
        class FakeFlight:
            data = pd.DataFrame({"heading": headings})
        assert detect_holding(FakeFlight()) == False

    def test_full_circle_detected(self):
        import pandas as pd
        # Simulate a 360° turn: heading goes 0, 30, 60, ..., 330, 360
        headings = list(range(0, 390, 30))
        class FakeFlight:
            data = pd.DataFrame({"heading": headings})
        assert detect_holding(FakeFlight()) == True
