# <!-- https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key} -->
import sys
import os

# Ajoute le répertoire parent au chemin d'accès (erreur 'attempted relative import with no known parent package')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import csv
from config import API_KEY, BASE_URL

# Infos récupérées de geo_data
cities = {
    "Paris": {"lat": 48.8588897, "lon": 2.3200410217200766},
    "Cairo": {"lat": 30.0443879, "lon": 31.2357257},
    "New York": {"lat": 40.7127281, "lon": -74.0060152},
    "London": {"lat": 51.5073219, "lon": -0.1276474},
    "Tokyo": {"lat": 35.6828387, "lon": 139.7594549}
}

weather_data = []

for city_name, coordinates in cities.items():
    url = f"{BASE_URL}/data/2.5/weather?lat={coordinates['lat']}&lon={coordinates['lon']}&appid={API_KEY}"
    r = requests.get(url)
    data = r.json()
    
    # Récup data
    weather_info = {
        "city": city_name,
        "weather": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "temperature_min": data["main"]["temp_min"],
        "temperature_max": data["main"]["temp_max"]
    }
    weather_data.append(weather_info)

# add data to CSV file
csv_file = "data_csv/weather_data.csv"
headers = ["city", "weather", "temperature", "feels_like", "temperature_min", "temperature_max"]
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(weather_data)


