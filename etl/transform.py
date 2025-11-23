import pandas as pd

def transform(raw_data: dict):
    """Transform raw weather JSON into a clean DataFrame."""
    records = []
    for item in raw_data.get("list", []):
        records.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "weather": item["weather"][0]["description"]
        })

    df = pd.DataFrame(records)
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df
