# Flight Deal Finder

This project helps you find cheap flights to your dream destinations.

## How it works

The script uses the Amadeus and Sheety APIs to find the best flight deals. Here's how it works:

1.  **Data from Google Sheet**: The script reads a list of destinations from a Google Sheet using the Sheety API. The sheet should contain the following columns: `city`, `iataCode`, and `lowestPrice`.
2.  **IATA Code Lookup**: If the `iataCode` column is empty, the script uses the Amadeus API to find the IATA code for each city and updates the Google Sheet.
3.  **Flight Search**: The script then searches for the cheapest flights from a specified origin city to each of the destinations in the Google Sheet. The search is for flights within the next 6 months.
4.  **Notifications**: If a flight is found that is cheaper than the `lowestPrice` in the Google Sheet, the script will print a notification to the console.

## Changes Made

I have made the following changes to the code:

*   **Refactored `flight_search.py`:** Removed duplicated `FlightSearch` class.
*   **Refactored `main.py`:** Removed duplicated `main` function and `if __name__ == "__main__":` block.
*   **Added `requirements.txt`:** Created a `requirements.txt` file to list the project dependencies.
*   **Improved Error Handling:** Added more specific error handling in `flight_search.py`.

### Before Changes

#### `flight_search.py`

```python
import requests
from flight_data import FlightData
import time

AMADEUS_AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_LOCATION_URL = "https://test.api.amadeus.com/v1/reference-data/locations"
AMADEUS_FLIGHT_OFFERS_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"


CLIENT_API = "Add Your Amendeus API key Code"
CLIENT_SECRET_AUTH = "Add Your Amendeus Auth Code "

class FlightSearch:

    def __init__(self):
        self.access_token = self.get_access_token()

    def _request_with_retry(self, method, url, max_retries=3, backoff=2, **kwargs):
        """
        Generic helper function to retry API requests.
        Retries on 5xx errors or connection issues.
        """
        for attempt in range(1, max_retries + 1):
            try:
                response = requests.request(method, url, timeout=10, **kwargs)

                # Retry only if server-side error
                if response.status_code >= 500:
                    print(f"[Attempt {attempt}] Server error {response.status_code}, retrying...")
                else:
                    requests.raise_for_status()
                    return response
            except requests.exceptions.RequestException as e:
                print(f"[Attempt {attempt}] Request failed : {e}")

                if attempt == max_retries:
                    raise # re-raise after last attempt
                time.sleep(backoff ** attempt)

    def get_access_token(self):
        """Authenticate with amadeus and return and access token."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_API,
            "client_secret": CLIENT_SECRET_AUTH
        }
        response = self._request_with_retry("POST", AMADEUS_AUTH_URL, data = data, headers = headers)
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        """Get the IATA code for a city using Amadeus Locations API."""
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"keyword": city_name,
                   "subType": "CITY"}
        response = self._request_with_retry("GET", AMADEUS_LOCATION_URL, headers=headers, params=params)
        data = response.json()
        
        if "data" not in data or len(data["data"]) == 0:
            print(f"WARNING: No IATA code found for '{city_name.strip()}'")
            return "N/A"
        
        return data["data"][0]["iataCode"]

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

        response = self._request_with_retry("GET", AMADEUS_FLIGHT_OFFERS_URL, headers=headers, params=params)

        try:
            data = response.json()["data"]
        except (KeyError, IndexError):
            print("No flight data found.")
            return None
        
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
        except (requests.exceptions.HTTPError, KeyError, IndexError):
            print(f"No direct flights found for {destination_city_code}. Trying with 1 stopover.")
            params["nonStop"] = "false"
            params["max"] = 2 # Increase max to get more options
            try:
                response = requests.get(AMADEUS_FLIGHT_OFFERS_URL, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()["data"]
            except (requests.exceptions.HTTPError, KeyError, IndexError):
                print(f"No flights found for {destination_city_code} with 1 stopover either.")
                return None

        if not data:
            print("No flights found.")
            return None

        flight_data = data[0]
        price = float(flight_data["price"]["total"])

        return FlightData(
            price=price,
            origin_city=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            origin_airport=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            destination_city=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            destination_airport=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            out_date=flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
            return_date=flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
            stop_overs=len(flight_data["itineraries"][0]["segments"]) - 1
        )


        flight_data = data[0]
        price = float(flight_data["price"]["total"])
        
        return FlightData(
            price=price,
            origin_city=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            origin_airport=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            destination_city=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            destination_airport=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            out_date=flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
            return_date=flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
        )
```

#### `main.py`

```python
import time
from data_manager import DataManager
from flight_search import FlightSearch

def main():
    """
    This script retrieves flight destination data and updates IATA codes if missing.
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()

    if sheet_data and sheet_data[0].get("iataCode") == "":
        print("Updating IATA codes...")
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(1) # To avoid hitting API rate limits
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()
        print("IATA codes updated successfully.")

    """
This file is responsible for running the flight search and sending notifications.
"""
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

def main():
    """
    This script retrieves flight destination data, updates IATA codes if missing,
    searches for the cheapest flights and sends a notification if a deal is found.
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    # Update IATA codes if missing
    for row in sheet_data:
        if row["iataCode"] == "":
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(1) # To avoid hitting API rate limits
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

    # Search for flights
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        if destination["iataCode"] != "N/A":
            flight = flight_search.search_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_month_from_today
            )

            if flight is not None and flight.price < destination["lowestPrice"]:
                notification_manager.send_notification(
                    price=flight.price,
                    origin_city=flight.origin_city,
                    origin_airport=flight.origin_airport,
                    destination_city=flight.destination_city,
                    destination_airport=flight.destination_airport,
                    out_date=flight.out_date,
                    return_date=flight.return_date,
                    stop_overs=flight.stop_overs,
                    via_city=flight.via_city
                )

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
```

### After Changes

#### `flight_search.py`

```python
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
        except (requests.exceptions.HTTPError, KeyError, IndexError):
            print(f"No direct flights found for {destination_city_code}. Trying with 1 stopover.")
            params["nonStop"] = "false"
            params["max"] = 2 # Increase max to get more options
            try:
                response = requests.get(AMADEUS_FLIGHT_OFFERS_URL, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()["data"]
            except (requests.exceptions.HTTPError, KeyError, IndexError):
                print(f"No flights found for {destination_city_code} with 1 stopover either.")
                return None

        if not data:
            print("No flights found.")
            return None

        flight_data = data[0]
        price = float(flight_data["price"]["total"])

        return FlightData(
            price=price,
            origin_city=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            origin_airport=flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"],
            destination_city=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            destination_airport=flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
            out_date=flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
            return_date=flight_data["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
            stop_overs=len(flight_data["itineraries"][0]["segments"]) - 1
        )
```

#### `main.py`

```python
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

def main():
    """
    This script retrieves flight destination data, updates IATA codes if missing,
    searches for the cheapest flights and sends a notification if a deal is found.
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    # Update IATA codes if missing
    for row in sheet_data:
        if row["iataCode"] == "":
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(1) # To avoid hitting API rate limits
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

    # Search for flights
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        if destination["iataCode"] != "N/A":
            flight = flight_search.search_flights(
                ORIGIN_CITY_IATA,
                destination["iataCode"],
                from_time=tomorrow,
                to_time=six_month_from_today
            )

            if flight is not None and flight.price < destination["lowestPrice"]:
                notification_manager.send_notification(
                    price=flight.price,
                    origin_city=flight.origin_city,
                    origin_airport=flight.origin_airport,
                    destination_city=flight.destination_city,
                    destination_airport=flight.destination_airport,
                    out_date=flight.out_date,
                    return_date=flight.return_date,
                    stop_overs=flight.stop_overs,
                    via_city=flight.via_city
                )

if __name__ == "__main__":
    main()
```

## How to use

1.  **Install the required libraries**:

    ```
    pip install -r requirements.txt
    ```

2.  **Create a Google Sheet**: Create a Google Sheet with the following columns: `city`, `iataCode`, and `lowestPrice`.
3.  **Set up the Sheety API**: Use the Sheety API to get an endpoint for your Google Sheet.
4.  **Get Amadeus API keys**: Get API keys from the Amadeus for Developers portal.
5.  **Update the `config.py` file**: Update the `config.py` file with your Sheety API endpoint, Sheety bearer token, and Amadeus API keys.
6.  **Run the script**:

    ```
    python main.py
    ```