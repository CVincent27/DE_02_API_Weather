import requests
from config import BASE_URL, API_KEY  # Import des variables de config

# Permet d'obtenir la latitude et longitude des villes
cities = ["Paris", "Le Caire", "New York", "Londres", "Tokyo"]

for city in cities:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"  # Utilisation des variables importées
    r = requests.get(url)
    data = r.json()
    result = data[0]
    name = result.get('name')
    lat = result.get('lat')
    lon = result.get('lon')
    print(f"Ville: {name}, Latitude: {lat}, Longitude: {lon}")
