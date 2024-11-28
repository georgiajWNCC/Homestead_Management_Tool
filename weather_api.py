"""
    Name: weather_api.py
    Author: Jonathan Georgiades
    Created: 28 November 2024
    Purpose: Weather API using OpenWeatherMap that gets request for weather related data.
    Integrated into main homestead GUI program.
"""
# Import requests
import requests

# Sign-up on https://openweathermap.org/api to request API Key
# OpenWeatherMap API Key
API_KEY = "d29ac40cbb2084a1c670f50a862f88ea"

# URL to access current weather from OpenWeatherMap API
URL = "https://api.openweathermap.org/data/2.5/weather"

# Create function to get weather data for a given location
def get_weather(location):
    query_string = {
        "units": "imperial",  # Units of measure: Imperial system (Fahrenheit, mph, etc.)
        "q": location,        # Location for weather
        "appid": API_KEY      # OpenWeatherMap API Key
    }

    # Send the GET request to OpenWeatherMap API
    response = requests.get(URL, params=query_string)

    # Check if the response status is OK
    if response.status_code == 200:
        # Return the JSON data if the request was successful
        return response.json()
    else:
        # If the request failed, return an error message
        return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
