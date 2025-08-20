import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5f4bf42926e63aec53e487d48b4e6bd8/flightData/sheet1"
SHEETY_BEARER_TOKEN = "priajptivryvennbthikuanyttukutaamm"


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self):
        """
        Initializes the DataManager.
        """
        self.destination_data = {}
        self.sheet_key = None
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
        }

    def get_destination_data(self):
        """
        Gets all the data from the Google Sheet.
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.sheet_key = list(data.keys())[0]
        self.destination_data = data[self.sheet_key]
        return self.destination_data

    def update_destination_codes(self):
        """
        Updates the Google Sheet with the IATA codes.
        """
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            response.raise_for_status()
            print(response.text)