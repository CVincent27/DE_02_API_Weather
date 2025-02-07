import requests

# Permet d'obtenir la latitude et longitude des villes
cities = ["Paris", "Le Caire", "New York", "Londres", "Tokyo"]

for city in cities:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=f97e5e8433890fa465d0c519e73f49f3"
    r = requests.get(url)
    data = r.json()
    result = data[0]
    name = result.get('name')
    lat = result.get('lat')
    lon = result.get('lon')
    print(f"Ville: {name}, Latitude: {lat}, Longitude: {lon}")

