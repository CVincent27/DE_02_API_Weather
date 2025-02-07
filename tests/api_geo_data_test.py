import requests

url ="http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=f97e5e8433890fa465d0c519e73f49f3"
r = requests.get(url)
data_test = r.json()
print(data_test)