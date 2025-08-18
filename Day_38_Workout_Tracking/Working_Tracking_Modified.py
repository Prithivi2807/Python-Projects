import requests 
from datetime import datetime


import os

GENDER = os.environ["GENDER"]
WEIGHT_KG = float(os.environ["WEIGHT_KG"])
HEIGHT_CM = float(os.environ["HEIGHT_CM"])
AGE = int(os.environ["AGE"])

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]


# GENDER = "Male"
# WEIGHT_KG = 75.2
# HEIGHT_CM = 180.0
# AGE = 24

# APP_ID = "a5c654e1"
# API_KEY = "a1a70deb44116c34fb0e239f9c9efe18"

# AUTH_TOKEN = "veprdaskhlkainthiba3028"



sheety_headers = {
  "Authorization": f"Bearer {AUTH_TOKEN}"
  }

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/5f4bf42926e63aec53e487d48b4e6bd8/myWorkouts/sheet1"

exercise_text = input("Tell me which exercises you did: ?")

headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,   
}

parameters = {
  "query": exercise_text,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)
print(result)

"""start of step 4 solution"""

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
  sheet_inputs = {
    "sheet1": {
      "date": today_date,
      "time": now_time,
      "exercise": exercise["name"].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
    }
  }


  sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_headers)
  print(sheet_response.text)