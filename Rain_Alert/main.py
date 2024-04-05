import requests
import json

OWM_Endpoint = "http://api.weatherapi.com/v1/forecast.json"

longitude = -105.704742
latitude = 41.881831

parameters = {
    "key": "21503cb73a9648f286333921240404",
    "q": "8.100122,80.278970",
    "days": "4",
}

response_api = requests.get(url=OWM_Endpoint, params=parameters)
response_api.raise_for_status()
response_api_data = response_api.json()

weather_slice = response_api_data["forecast"]["forecastday"][0]["hour"][:23]

for hour_data in weather_slice:
    hour_rain_value = hour_data["will_it_rain"]
    hour_chance_of_rain = hour_data["chance_of_rain"]
    hour_time = hour_data["time"]
    if hour_rain_value == 1:
        print(f"{hour_time}, Bring an Umbrella , chance of rain :{hour_chance_of_rain}")
