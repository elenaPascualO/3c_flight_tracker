"""Tests for the database module."""

from datetime import date

from src.database import (
    get_downloaded_ranges,
    insert_overflights,
    query_overflights,
    register_collection_run,
)


class TestInsertOverflights:
    def test_insert(self, sample_overflights, tmp_db):
        count = insert_overflights(sample_overflights, db_path=tmp_db)
        assert count == len(sample_overflights)

    def test_insert_empty(self, tmp_db):
        import pandas as pd
        count = insert_overflights(pd.DataFrame(), db_path=tmp_db)
        assert count == 0


class TestQueryOverflights:
    def test_query_all(self, sample_overflights, tmp_db):
        insert_overflights(sample_overflights, db_path=tmp_db)
        result = query_overflights(db_path=tmp_db)
        assert len(result) == len(sample_overflights)

    def test_filter_altitude(self, sample_overflights, tmp_db):
        insert_overflights(sample_overflights, db_path=tmp_db)
        result = query_overflights(max_altitude=1500, db_path=tmp_db)
        assert all(result["altitude"] <= 1500)
        assert len(result) == 3  # 1200, 900, 1100

    def test_filter_hour(self, sample_overflights, tmp_db):
        insert_overflights(sample_overflights, db_path=tmp_db)
        result = query_overflights(hour_min=10, hour_max=14, db_path=tmp_db)
        assert all((result["local_hour"] >= 10) & (result["local_hour"] <= 14))

    def test_filter_days(self, sample_overflights, tmp_db):
        insert_overflights(sample_overflights, db_path=tmp_db)
        result = query_overflights(days_of_week=[0], db_path=tmp_db)
        assert all(result["day_of_week"] == 0)
        assert len(result) == 2

    def test_empty_db(self, tmp_db):
        result = query_overflights(db_path=tmp_db)
        assert result.empty


class TestCollectionRuns:
    def test_register_and_get(self, tmp_db):
        register_collection_run(date(2024, 3, 1), date(2024, 3, 7), 42, db_path=tmp_db)
        ranges = get_downloaded_ranges(db_path=tmp_db)
        assert len(ranges) == 1
        assert ranges[0]["start_date"] == "2024-03-01"
        assert ranges[0]["end_date"] == "2024-03-07"
        assert ranges[0]["num_flights"] == 42

    def test_multiple_runs(self, tmp_db):
        register_collection_run(date(2024, 3, 1), date(2024, 3, 7), 42, db_path=tmp_db)
        register_collection_run(date(2024, 3, 8), date(2024, 3, 14), 35, db_path=tmp_db)
        ranges = get_downloaded_ranges(db_path=tmp_db)
        assert len(ranges) == 2
