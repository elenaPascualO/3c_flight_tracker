"""Statistical analysis of overflight data for noise impact study."""

from datetime import datetime

import pandas as pd

from src.config import ALTITUDE_NOISY, ALTITUDE_PERCEPTIBLE, TZ

DAYS_ES = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def flights_per_day(df: pd.DataFrame) -> dict:
    """Calculate flights per day statistics."""
    if df.empty:
        return {"mean": 0, "median": 0, "max": 0, "min": 0}

    df = df.copy()
    df["date"] = pd.to_datetime(df["timestamp"], unit="s", utc=True).dt.tz_convert(str(TZ)).dt.date
    daily = df.groupby("date").size()

    return {
        "mean": round(daily.mean(), 1),
        "median": round(daily.median(), 1),
        "max": int(daily.max()),
        "min": int(daily.min()),
    }


def flights_per_hour(df: pd.DataFrame) -> pd.DataFrame:
    """Count flights per hour of the day (0-23)."""
    if df.empty:
        return pd.DataFrame({"hour": range(24), "count": [0] * 24})

    counts = df.groupby("local_hour").size().reindex(range(24), fill_value=0)
    return pd.DataFrame({"hour": counts.index, "count": counts.values})


def flights_per_weekday(df: pd.DataFrame) -> pd.DataFrame:
    """Count flights per day of the week."""
    if df.empty:
        return pd.DataFrame({"day": range(7), "day_name": DAYS_ES, "count": [0] * 7})

    counts = df.groupby("day_of_week").size().reindex(range(7), fill_value=0)
    return pd.DataFrame({
        "day": counts.index,
        "day_name": [DAYS_ES[i] for i in counts.index],
        "count": counts.values,
    })


def altitude_distribution(df: pd.DataFrame) -> dict:
    """Classify flights by altitude category."""
    if df.empty:
        return {"below_1500": 0, "between_1500_3000": 0, "above_3000": 0}

    below = len(df[df["altitude"] < ALTITUDE_NOISY])
    between = len(df[(df["altitude"] >= ALTITUDE_NOISY) & (df["altitude"] < ALTITUDE_PERCEPTIBLE)])
    above = len(df[df["altitude"] >= ALTITUDE_PERCEPTIBLE])

    return {
        "below_1500": below,
        "between_1500_3000": between,
        "above_3000": above,
    }


def heatmap_data(df: pd.DataFrame) -> pd.DataFrame:
    """Generate hour x weekday heatmap data."""
    if df.empty:
        return pd.DataFrame(0, index=range(7), columns=range(24))

    pivot = df.groupby(["day_of_week", "local_hour"]).size().unstack(fill_value=0)
    pivot = pivot.reindex(index=range(7), columns=range(24), fill_value=0)
    return pivot


def hourly_altitude_scatter(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare data for hour vs altitude scatter plot."""
    if df.empty:
        return pd.DataFrame(columns=["local_hour", "altitude"])
    return df[["local_hour", "altitude"]].copy()


def monthly_evolution(df: pd.DataFrame) -> pd.DataFrame:
    """Count flights per month."""
    if df.empty:
        return pd.DataFrame(columns=["month", "count"])

    df = df.copy()
    df["month"] = pd.to_datetime(df["timestamp"], unit="s", utc=True).dt.tz_convert(str(TZ)).dt.to_period("M")
    monthly = df.groupby("month").size().reset_index(name="count")
    monthly["month"] = monthly["month"].astype(str)
    return monthly


def daily_series(df: pd.DataFrame) -> pd.DataFrame:
    """Daily flight count time series."""
    if df.empty:
        return pd.DataFrame(columns=["date", "count"])

    df = df.copy()
    df["date"] = pd.to_datetime(df["timestamp"], unit="s", utc=True).dt.tz_convert(str(TZ)).dt.date
    daily = df.groupby("date").size().reset_index(name="count")
    daily["date"] = pd.to_datetime(daily["date"])
    return daily


def nighttime_stats(df: pd.DataFrame) -> dict:
    """Statistics for nighttime flights (23:00-07:00)."""
    night = df[(df["local_hour"] >= 23) | (df["local_hour"] < 7)]
    total = len(df) if len(df) > 0 else 1
    return {
        "count": len(night),
        "percentage": round(len(night) / total * 100, 1),
        "mean_altitude": round(night["altitude"].mean(), 0) if not night.empty else 0,
    }
