# 🌦 Dynamic ETL Pipeline & Live Weather Analytics Dashboard

## Objective
A fully functional real-time ETL (Extract–Transform–Load) data pipeline that fetches live weather data using the OpenWeatherMap API and visualizes trends through an interactive Streamlit dashboard.
The app supports city-based filtering, dynamic caching, and date/time selection using 5-day forecast data.

## Features
- Real-time data extraction from OpenWeather API
- ETL pipeline built with Pandas (Extract → Transform → Load)
- Local caching to reduce API calls & improve performance
- User-selected parameters: City, Date, Time
- Interactive charts using Plotly
- Robust error handling (invalid city, API failure, etc.)
- Modular architecture for scalability & readability
- Fully interactive Streamlit dashboard

## 🛠 Tech Stack
Python(Pandas, Streamlit, plotly), OpenWeatherMap API


# How to Use the Weather Predictor?

## 1. Install Dependencies

Make sure you have Python 3.8 or higher and create a virtual environment. Then install the required packages:
pip install -r requirements.txt

## 2. Set Up the Environment Variables

Create a .env file in the root directory and add your API key:
WEATHER_API_KEY=your_api_key_here (You can get a free API key from: https://openweathermap.org/api)

## 3. Run the Application

Execute the following command to start the Streamlit weather predictor:
streamlit run main.py

## 4. Input Parameters

When the app loads in your browser, you will see three required inputs:

City Name: Enter the name of any global city (e.g., London, Karachi).
Date: Select any date within the forecast range supported by the API.
Time: Select a time to get weather details closest to that hour.

## 5. View Forecast Results

After submitting inputs, the app will display:

Temperature (in Celsius and Fahrenheit)
Weather Condition (e.g., Cloudy, Clear)
Humidity
Wind Speed
Timestamp of the forecast

## Notes
Ensure your API key is valid, otherwise the application will not fetch weather data.
Date and time selections work only for future forecast ranges available in the OpenWeather API.
