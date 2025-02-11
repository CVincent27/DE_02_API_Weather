# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

# Ajoute le répertoire parent au chemin d'accès (erreur 'attempted relative import with no known parent package')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import os
import requests
from config import API_KEY, BASE_URL

url =f"{BASE_URL}geo/1.0/direct?q=London&appid={API_KEY}"
r = requests.get(url)
data_test = r.json()
print(data_test)