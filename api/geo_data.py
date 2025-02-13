import sys
import os
# Ajoute le répertoire parent au chemin d'accès (erreur 'attempted relative import with no known parent package')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
import csv
from config import API_KEY, BASE_URL

# Latitude et longitude des villes
def geo_data_fetch_save():
    cities = [
        "Paris", "Le Caire", "New York", "Londres", "Tokyo", "Delhi",
        "Shanghai", "Los Angeles", "Moscou", "São Paulo", "Mexico",
        "Pékin", "Istanbul", "Jakarta", "Séoul", "Bangkok", "Mumbai",
        "Buenos Aires", "Lagos", "Hong Kong", "Singapour", "Sydney",
        "Toronto", "Dubaï", "Rome"
    ]

    geo_data = []

    for city in cities:
        url =f"{BASE_URL}geo/1.0/direct?q={city}&appid={API_KEY}"
        r = requests.get(url)
        data = r.json()
        # print(data)

        geo_info = {
            "city": city,
            "country": data[0]["country"],
            "lat": data[0]["lat"],
            "long": data[0]["lon"]
        }
        geo_data.append(geo_info)

    csv_file = "data_csv/geo_data.csv"
    headers = ["city","country","lat","long"]
    with open(csv_file, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(geo_data)

if __name__ == "__main__":
    geo_data_fetch_save()