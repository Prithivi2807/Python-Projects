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
                    return_date=flight.return_date
                )

if __name__ == "__main__":
    main()