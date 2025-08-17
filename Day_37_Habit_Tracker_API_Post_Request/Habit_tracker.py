import requests
from datetime import datetime

USERNAME = "YOURNAME"
TOKEN = "CUSTOMTEXT"
GRAPH_ID = "GRAPHNAME"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": GRAPH_ID,
  "name": "Cycling Graph",
  "unit": "km",
  "type": "float", 
  "color": "ajisai"
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime(year=2025, month=8, day=15)
today = datetime.now()
print(today.strftime("%Y%m%d"))


pixel_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": input("How many kilometers did you cycle today ? "),
}


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
  "quantity": "15.02"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

date = "20250812"

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)