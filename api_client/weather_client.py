import requests
from config.config import OPENWEATHER_API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def fetch_weather(city: str):
    """Fetch 5-day weather forecast for a city."""
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }
    

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        if response.status_code == 404:
            raise ValueError(f"❌ Invalid city name: {city}")
        response.raise_for_status()  # raises error for 4xx/5xx errors

        return response.json()

    except requests.exceptions.RequestException:
        raise ConnectionError("⚠️ API Connection Failed! Check your network or API key.")
