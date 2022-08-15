import requests

API_KEY = "" # Paste API key from website here #
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round((data['main']['temp'] - 273.15) * (9/5) + 32, 2)
    print (f"Weather is {weather}, and temperature is {temperature}F.")
 else:
    print("An error occurred.")