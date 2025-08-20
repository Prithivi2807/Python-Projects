import time
from data_manager import DataManager
from flight_search import FlightSearch

def main():
    """
    This script retrieves flight destination data, updates IATA codes if missing,
    and then updates the destination data.
    """
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()
    # print(sheet_data)
    print()
    if sheet_data and sheet_data[0].get("iataCode") == "":
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(1)
            print(row)
        print(f"sheet_data:\n {sheet_data}")

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

if __name__ == "__main__":
    main()
