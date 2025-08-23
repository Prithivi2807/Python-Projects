import csv
import os

class DataManager:
    """
    This class is responsible for talking to the local CSV files.
    """
    def __init__(self):
        """
        Initializes the DataManager.
        Finds the absolute path of the directory the script is in.
        """
        self.destination_data = []
        self.customer_data = []
        # Get the directory where the script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.deals_csv_path = os.path.join(script_dir, 'flight_deals.csv')
        self.users_csv_path = os.path.join(script_dir, 'users.csv')

    def get_destination_data(self):
        """
        Reads the destination data from the flight_deals.csv file.
        """
        try:
            with open(self.deals_csv_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.destination_data = [row for row in reader]
                for row in self.destination_data:
                    row['lowestPrice'] = int(row['lowestPrice'])
                    row['id'] = int(row['id'])
            return self.destination_data
        except FileNotFoundError:
            print(f"Error: The file {self.deals_csv_path} was not found.")
            return []

    def update_destination_codes(self):
        """
        Updates the flight_deals.csv file with the IATA codes.
        """
        if not self.destination_data:
            print("No destination data to update.")
            return
        try:
            with open(self.deals_csv_path, mode='w', newline='', encoding='utf-8') as file:
                header = self.destination_data[0].keys()
                writer = csv.DictWriter(file, fieldnames=header)
                writer.writeheader()
                writer.writerows(self.destination_data)
            print("CSV file updated successfully with IATA codes.")
        except Exception as e:
            print(f"An error occurred while writing to the CSV file: {e}")

    def get_customer_emails(self):
        """
        Reads the customer data from the users.csv file.
        """
        try:
            with open(self.users_csv_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.customer_data = [row for row in reader]
            return self.customer_data
        except FileNotFoundError:
            print(f"Error: The file {self.users_csv_path} was not found.")
            return []