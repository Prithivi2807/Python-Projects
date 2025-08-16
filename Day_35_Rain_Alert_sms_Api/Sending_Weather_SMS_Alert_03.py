import requests
import os
from twilio.rest import Client

weather_url = "https://api.openweathermap.org/data/2.5/weather?"

api_key = "ENTER Your api through twilio account"
api_key = os.environ.get("OWM_API_KEY")

account_sid = 'ENTER Your sid through twilio account '

auth_token = os.environ.get("AUTH_TOKEN")
auth_token = 'ENTER Your AUTH_TOKEN through twilio account'

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

will_rain = False
condition_code = (weather_data["weather"][0]["id"])
if int(condition_code) < 900:
  will_rain = True
  print("Bring an umbrella")

if will_rain:
  client = Client(account_sid, auth_token)
  message = client.messages \
  .create(
    body="It's going to rain today. remember to bring an umbrella 🌂 ☔",
    from_ = '+12187488075',
    to="Enter your number "
  )

print(message.status)
print()
print(message.sid)


# import os 
# TWILIO_SID = os.getenv("TWILIO_SID")