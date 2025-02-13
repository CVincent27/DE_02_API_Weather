# <!-- https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key} -->
import sys
import os

# Ajoute le répertoire parent au chemin d'accès (erreur 'attempted relative import with no known parent package')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import csv
import pandas as pd
from config import API_KEY, BASE_URL

def weather_data_fetch_save():
    df = pd.read_csv("data_csv/geo_data.csv")
    weather_data = []

    # itérer sur chaque ligne
    for row in df.itertuples(index=False):
        lat = row.lat
        long = row.long
        city_name = row.city
        country = row.country
        url = f"{BASE_URL}/data/2.5/weather?lat={lat}&lon={long}&units=metric&lang=fr&appid={API_KEY}"
        r = requests.get(url)
        data = r.json()


        # Récup data
        weather_info = {
            "city": city_name,
            "country": country,
            "weather": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temperature_min": data["main"]["temp_min"],
            "temperature_max": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "wind_direction_deg": data["wind"]["deg"],
            "cloud_cover": data["clouds"]["all"],
            "rain": data.get("rain", {}).get("1h", 0), 
            "snow": data.get("snow", {}).get("1h", 0),
            "sunrise": data["sys"]["sunrise"],
            "sunset": data["sys"]["sunset"],
            "timezone": data["timezone"]
        }
        weather_data.append(weather_info)

    # add data csv weather
    csv_file = "data_csv/weather_data.csv"
    headers = ["city", "country", "weather", "temperature", "feels_like", "temperature_min", "temperature_max",
               "pressure", "humidity", "wind_speed", "wind_direction_deg", "cloud_cover", "rain", "snow",
               "sunrise", "sunset", "timezone"
            ]
    with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(weather_data)

if __name__ == "__main__":
    weather_data_fetch_save()