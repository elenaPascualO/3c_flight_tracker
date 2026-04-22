"""Tests for the database module."""

from datetime import date

from src.database import (
    get_downloaded_ranges,
    insert_noise_annual,
    insert_noise_monthly,
    insert_overflights,
    query_noise_annual,
    query_noise_monthly,
    query_overflights,
    register_collection_run,
)
from src.noise_report_parser import AnnualRow, MonthlyRow


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


def _annual_row(year=2025, tmr_id=16, location_index=None, tmr_flag="") -> AnnualRow:
    return AnnualRow(
        year=year, tmr_id=tmr_id, location_index=location_index, tmr_flag=tmr_flag,
        laeq_total_day=55.1, flags_total_day="",
        laeq_avion_day=50.4, flags_avion_day="",
        laeq_total_evening=49.9, flags_total_evening="",
        laeq_avion_evening=47.2, flags_avion_evening="",
        laeq_total_night=43.6, flags_total_night="",
        laeq_avion_night=25.0, flags_avion_night="",
    )


class TestNoiseAnnual:
    def test_insert_and_query(self, tmp_db):
        row = _annual_row()
        count = insert_noise_annual([row], source_file="2025_informe_anual.pdf", db_path=tmp_db)
        assert count == 1
        df = query_noise_annual(tmr_id=16, db_path=tmp_db)
        assert len(df) == 1
        assert df.iloc[0]["laeq_avion_night"] == 25.0
        assert df.iloc[0]["source_file"] == "2025_informe_anual.pdf"

    def test_two_locations_same_year(self, tmp_db):
        """El TMR-16 tuvo dos ubicaciones en 2023: el PK (year, tmr_id, location_index) debe permitirlas."""
        r1 = _annual_row(year=2023, location_index=3)
        r2 = _annual_row(year=2023, location_index=4)
        count = insert_noise_annual([r1, r2], source_file="2023_informe_anual.pdf", db_path=tmp_db)
        assert count == 2
        df = query_noise_annual(tmr_id=16, db_path=tmp_db)
        assert len(df) == 2

    def test_replace_on_reimport(self, tmp_db):
        """Re-ejecutar la importación debe hacer upsert, no duplicar."""
        row = _annual_row()
        insert_noise_annual([row], source_file="a.pdf", db_path=tmp_db)
        insert_noise_annual([row], source_file="a.pdf", db_path=tmp_db)
        df = query_noise_annual(db_path=tmp_db)
        assert len(df) == 1


class TestNoiseMonthly:
    def test_insert_and_query(self, tmp_db):
        rows = [
            MonthlyRow(year=2025, month=m, tmr_id=16, period=p,
                       laeq_total=40.0, flags_total="",
                       laeq_avion=20.0, flags_avion="")
            for m in (1, 2) for p in ("day", "evening", "night")
        ]
        count = insert_noise_monthly(rows, source_file="2025_informe_anual.pdf", db_path=tmp_db)
        assert count == 6
        df = query_noise_monthly(tmr_id=16, db_path=tmp_db)
        assert len(df) == 6

    def test_nd_stored_as_null(self, tmp_db):
        rows = [MonthlyRow(year=2025, month=9, tmr_id=16, period="night",
                           laeq_total=None, flags_total="",
                           laeq_avion=None, flags_avion="")]
        insert_noise_monthly(rows, source_file="x.pdf", db_path=tmp_db)
        df = query_noise_monthly(db_path=tmp_db)
        assert df.iloc[0]["laeq_total"] is None or (df.iloc[0]["laeq_total"] != df.iloc[0]["laeq_total"])  # NaN
