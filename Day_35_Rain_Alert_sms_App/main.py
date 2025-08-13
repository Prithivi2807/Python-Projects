import requests
import os
from twilio.rest import Client




# url = "https://api.openweathermap.org/data/2.5/weather?lat=12.82709699438328&lon=78.77788575040059&appid=e7c45666db44505c71c38c9ccac129be"

api_key = "e7c45666db44505c71c38c9ccac129be"
weather_url = "https://api.openweathermap.org/data/2.5/weather?"
weather_params = {
  "lat": 24.2500,
  "lon": 43.2000,
  "appid":api_key,
  "exclude":"current, minutely, daily"
}
"""
current_rain location 
Latitude: 16.9833  
Longitude: 40.1667

default:
  "lat": 12.82709699438328,
  "lon": 78.77788575040059,
"""

response = requests.get(url=weather_url, params=weather_params)
# print(response)
# print(response.json())
weather_data = response.json()


# weather_slice = weather_data["hourly"][:12]
# print(weather_slice)

# will_rain = False

# for hour_data in weather_slice:
#   condition_code = (hour_data["weather"][0]["id"])
#   if int(condition_code) < 700:
#     will_rain = True

# if will_rain:
  # print("Bring an umbrella.")

# print(weather_data["hourly"][0]["weather"][0]["id"])  ## Not working 

will_rain = False

condition_code = (weather_data["weather"][0]["id"])


if int(condition_code) < 900:
  will_rain = True

if will_rain:
  print("Bring an Umbrella.")




print((weather_data["weather"][0]["id"]))