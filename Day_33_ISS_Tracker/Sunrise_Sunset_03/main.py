import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758 # Your longitude


parameters = { 
  "lat": MY_LAT,
  "lng": MY_LONG,
  "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) 
response.raise_for_status()
data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)