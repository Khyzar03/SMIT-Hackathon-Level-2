def basic_stats(df):
    return {
        "avg_temp": round(df["temp"].mean(), 2),
        "min_temp": df["temp"].min(),
        "max_temp": df["temp"].max(),
        "avg_humidity": round(df["humidity"].mean(), 2),
    }
