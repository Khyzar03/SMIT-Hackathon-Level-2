from api_client.weather_client import fetch_weather

def extract(city: str):
    """Extract weather data from API client."""
    return fetch_weather(city)
