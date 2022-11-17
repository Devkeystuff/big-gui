import os

import requests
from dotenv import load_dotenv

from utils.kelvin_to_celsius import kelvin_to_celsius

load_dotenv()

URI = "https://api.openweathermap.org/data/2.5/weather"

def get_city_temperature(name: str):
    try:
        res = requests.get(f"{URI}?q={name}&appid={os.getenv('API_KEY')}")
        weather_data = res.json()
        return {
            "temp": kelvin_to_celsius(weather_data["main"]["temp"]),
            "feels_like": kelvin_to_celsius(weather_data["main"]["feels_like"])
        }
    except ValueError as e:
        print("Couldn't fetch city")