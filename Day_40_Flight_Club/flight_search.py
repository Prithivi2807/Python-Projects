import requests
from flight_data import FlightData
import time
from config import AMADEUS_AUTH_URL, AMADEUS_LOCATION_URL, AMADEUS_FLIGHT_OFFERS_URL, CLIENT_API, CLIENT_SECRET_AUTH

class FlightSearch:

    def __init__(self):
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        """Authenticate with amadeus and return and access token."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_API,
            "client_secret": CLIENT_SECRET_AUTH
        }
        
        response = requests.post(AMADEUS_AUTH_URL, data=data, headers=headers)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        """Get the IATA code for a city using Amadeus Locations API."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"keyword": city_name,
                   "subType": "CITY"}
        response = requests.get(AMADEUS_LOCATION_URL, headers=headers, params=params)
        try:
            response.raise_for_status()
            data = response.json()
            if "data" not in data or len(data["data"]) == 0:
                print(f"WARNING: No IATA code found for '{city_name.strip()}'")
                return "N/A"
            return data["data"][0]["iataCode"]
        except requests.exceptions.HTTPError as e:
            print(f"Error getting destination code for {city_name}: {e}")
            return "N/A"

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """Search for flights using Amadeus Flight Offers API."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 1
        }

        try:
            response = requests.get(AMADEUS_FLIGHT_OFFERS_URL, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()["data"]
            flight_data = data[0]
            
            return FlightData(
                price=float(flight_data["price"]["total"]),
                origin_city=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                origin_airport=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                destination_city=flight_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                destination_airport=flight_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
                out_date=flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                return_date=flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            )

        except (requests.exceptions.HTTPError, KeyError, IndexError):
            print(f"No direct flights found for {destination_city_code}. Trying with 1 stopover.")
            params["nonStop"] = "false"
            params["max"] = 2 # Increase max to get more options
            try:
                response = requests.get(AMADEUS_FLIGHT_OFFERS_URL, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()["data"]
                if not data:
                    print(f"No flights found for {destination_city_code} with 1 stopover either.")
                    return None

                flight_data = data[0]
                return FlightData(
                    price=float(flight_data["price"]["total"]),
                    origin_city=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    origin_airport=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                    destination_city=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
                    destination_airport=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
                    out_date=flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                    return_date=flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
                    stop_overs=1,
                    via_city=flight_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                )
            except (requests.exceptions.HTTPError, KeyError, IndexError):
                print(f"No flights found for {destination_city_code} with 1 stopover either.")
                return None