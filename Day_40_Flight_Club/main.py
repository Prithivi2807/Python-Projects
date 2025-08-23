from datetime import datetime, timedelta
import time
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
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    # Update IATA codes in memory if they are missing
    iata_codes_updated = False
    for row in sheet_data:
        if not row.get("iataCode"):
            print(f"Updating IATA code for {row['city']}...")
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            iata_codes_updated = True
            time.sleep(1) # To avoid hitting API rate limits
    
    # If any codes were updated, write the changes back to the CSV file
    if iata_codes_updated:
        print("Saving updated IATA codes to CSV...")
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    # Search for flights
    tomorrow = datetime.now() + timedelta(days=1)
    six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

    for destination in sheet_data:
        if destination["iataCode"] == "N/A":
            continue # Skip destinations for which we couldn't find an IATA code

        print(f"Searching for flights to {destination['city']}...")
        flight = flight_search.search_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_months_from_today
        )

        if flight is not None and flight.price < destination["lowestPrice"]:
            print(f"Low price found for {destination['city']}! Price: £{flight.price}")
            
            # Get customer emails
            users = data_manager.get_customer_emails()
            emails = [user["email"] for user in users]
            names = [user["firstName"] for user in users]

            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            
            notification_manager.send_emails(emails, message)

if __name__ == "__main__":
    main()
