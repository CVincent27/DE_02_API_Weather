# <!-- https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key} -->
import sys
import os

# Ajouter le répertoire parent au chemin d'accès (erreur 'attempted relative import with no known parent package')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import requests
from config import API_KEY, BASE_URL
# Récupère les infos météos

url = f"{BASE_URL}/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}"
r = requests.get(url)
data = r.json()
print(data)
# weather = data.get('weather')
# temp = data.get('main')
# print(f"météo: {weather}, conditions: {temp}")