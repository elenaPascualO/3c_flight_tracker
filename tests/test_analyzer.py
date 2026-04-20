"""Tests for the analyzer module."""

import pandas as pd

from src.analyzer import (
    altitude_distribution,
    daily_series,
    flights_per_day,
    flights_per_hour,
    flights_per_weekday,
    heatmap_data,
    hourly_altitude_scatter,
    monthly_evolution,
    nighttime_stats,
    DAYS_ES,
)


class TestFlightsPerDay:
    def test_with_data(self, sample_overflights):
        result = flights_per_day(sample_overflights)
        assert result["mean"] > 0
        assert result["max"] >= result["min"]
        assert result["max"] >= result["mean"]
        assert all(k in result for k in ("mean", "median", "max", "min"))

    def test_empty(self):
        result = flights_per_day(pd.DataFrame())
        assert result == {"mean": 0, "median": 0, "max": 0, "min": 0}


class TestFlightsPerHour:
    def test_with_data(self, sample_overflights):
        result = flights_per_hour(sample_overflights)
        assert len(result) == 24
        assert result["count"].sum() == len(sample_overflights)

    def test_empty(self):
        result = flights_per_hour(pd.DataFrame())
        assert len(result) == 24
        assert result["count"].sum() == 0


class TestFlightsPerWeekday:
    def test_with_data(self, sample_overflights):
        result = flights_per_weekday(sample_overflights)
        assert len(result) == 7
        assert list(result["day_name"]) == DAYS_ES
        assert result["count"].sum() == len(sample_overflights)

    def test_empty(self):
        result = flights_per_weekday(pd.DataFrame())
        assert len(result) == 7
        assert result["count"].sum() == 0


class TestAltitudeDistribution:
    def test_with_data(self, sample_overflights):
        result = altitude_distribution(sample_overflights)
        total = result["below_1500"] + result["between_1500_3000"] + result["above_3000"]
        assert total == len(sample_overflights)

    def test_categories(self, sample_overflights):
        result = altitude_distribution(sample_overflights)
        # 1200, 900, 1100 are below 1500
        assert result["below_1500"] == 3
        # 1800, 2500 are between 1500-3000
        assert result["between_1500_3000"] == 2
        assert result["above_3000"] == 0

    def test_empty(self):
        result = altitude_distribution(pd.DataFrame())
        assert result == {"below_1500": 0, "between_1500_3000": 0, "above_3000": 0}


class TestHeatmapData:
    def test_shape(self, sample_overflights):
        result = heatmap_data(sample_overflights)
        assert result.shape == (7, 24)

    def test_values_sum(self, sample_overflights):
        result = heatmap_data(sample_overflights)
        assert result.values.sum() == len(sample_overflights)

    def test_empty(self):
        result = heatmap_data(pd.DataFrame())
        assert result.shape == (7, 24)
        assert result.values.sum() == 0


class TestHourlyAltitudeScatter:
    def test_with_data(self, sample_overflights):
        result = hourly_altitude_scatter(sample_overflights)
        assert len(result) == len(sample_overflights)
        assert list(result.columns) == ["local_hour", "altitude"]

    def test_empty(self):
        result = hourly_altitude_scatter(pd.DataFrame())
        assert result.empty


class TestMonthlyEvolution:
    def test_with_data(self, sample_overflights):
        result = monthly_evolution(sample_overflights)
        assert "month" in result.columns
        assert "count" in result.columns
        assert result["count"].sum() == len(sample_overflights)

    def test_empty(self):
        result = monthly_evolution(pd.DataFrame())
        assert result.empty


class TestDailySeries:
    def test_with_data(self, sample_overflights):
        result = daily_series(sample_overflights)
        assert "date" in result.columns
        assert "count" in result.columns
        assert result["count"].sum() == len(sample_overflights)

    def test_empty(self):
        result = daily_series(pd.DataFrame())
        assert result.empty


class TestNighttimeStats:
    def test_with_data(self, sample_overflights):
        result = nighttime_stats(sample_overflights)
        assert "count" in result
        assert "percentage" in result
        assert "mean_altitude" in result
        # Hours 2 and 23 are nighttime
        assert result["count"] == 2
        assert 0 <= result["percentage"] <= 100

    def test_empty(self):
        result = nighttime_stats(pd.DataFrame(columns=["local_hour", "altitude"]))
        assert result["count"] == 0
        assert result["percentage"] == 0.0
