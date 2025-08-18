import requests 

GENDER = "Male"
WEIGHT_KG = 75.2
HEIGHT_CM = 180.0
AGE = 24

APP_ID = "a5c654e1"
API_KEY = "a1a70deb44116c34fb0e239f9c9efe18"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)