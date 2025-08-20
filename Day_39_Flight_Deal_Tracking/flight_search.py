import requests

AMADEUS_AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_LOCATION_URL = "https://test.api.amadeus.com/v1/reference-data/locations"


CLIENT_API = "1D2GveE42z206TbR7A1vKtQ1CalYUAgO"
CLIENT_SECRET_AUTH = "xg1ePvncwslQTWZT"

class FlightSearch:

    def __init__(self):
        self.access_token = self.get_access_token()

    def get_access_token(self):
        """Authenticate with amadeus and return and access token."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_API,
            "client_secret": CLIENT_SECRET_AUTH
        }
        response = requests.post(AMADEUS_AUTH_URL, headers=headers, data=data)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        """Get the IATA code for a city using Amadeus Locations API."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"keyword": city_name, "subType": "CITY"}
        response = requests.get(AMADEUS_LOCATION_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or len(data["data"]) == 0:
            print(f"WARNING: No IATA code found for '{city_name.strip()}'")
            return "N/A"
        
        return data["data"][0]["iataCode"]