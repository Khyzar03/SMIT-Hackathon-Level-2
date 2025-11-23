How to Use the Weather Predictor

Step 1: Install the project requirements
Make sure you have Python installed. Then install all required dependencies from the provided requirements file.

Step 2: Set up the environment configuration
Create a file named .env in the project folder and add your OpenWeather API key to it. This key is required for the application to fetch weather data.

Step 3: Start the application
Run the main Python file using Streamlit. This will open the weather predictor in your browser.

Step 4: Provide user input
Once the application opens, enter the following details in the input fields:

* City name
* Desired date
* Desired time

Step 5: View the weather forecast
The application will display the following information based on your selected city, date, and time:

* Temperature in Celsius and Fahrenheit
* Weather condition such as sunny, cloudy, or rainy
* Humidity level
* Wind speed
* Exact forecast timestamp

Step 6: Understanding the folder structure
The project is divided into modules. The API client handles data requests, the extract module filters and prepares data, and the utility module manages calculations such as unit conversions. The main file provides the user interface.

Notes:
Make sure your API key is correct. The date and time options will only work within the available forecast range supported by the API.
