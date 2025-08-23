# Flight Club

This project helps you find the best flight deals and notifies you when prices drop for your dream destinations.

## Project Overview

The application tracks flight prices for a list of destinations and compares them against a target price you set. If a flight is found that is cheaper than your target price, it notifies all the members of your "Flight Club" via email.

This project uses the Amadeus API to find flight deals in real-time.

## Key Features & Corrections

This version includes several major improvements:

1.  **Local Data Storage**: The original dependency on the Sheety API has been completely removed. The application now uses local `.csv` files (`flight_deals.csv` and `users.csv`) to store data. This removes the need for a paid API service and makes the project easier to run and manage.
2.  **User Management**: A full user management system has been added.
    *   `users.csv` stores a list of all flight club members.
    *   A new script, `add_user.py`, provides an easy way to add new users to the club.
3.  **Enhanced Notifications**: The notification system has been updated to send alerts to all registered users. It also includes more detailed information in the alert, such as stopover details.

## How to Use

### 1. Add or Edit Flight Deals

To change the destinations you are tracking, simply edit the `flight_deals.csv` file. You can add new rows with the city name and your target `lowestPrice`.

### 2. Add a New User

To add a new user to the notification list, run the `add_user.py` script from your terminal:

```bash
python add_user.py
```

The script will prompt you to enter the new user's first name, last name, and email address.

### 3. Find Cheap Flights

To run the main application and search for flight deals, execute the `main.py` script:

```bash
python main.py
```

The script will:
- Read the destinations from `flight_deals.csv`.
- Automatically find and update any missing IATA codes.
- Search for the latest flight prices.
- If a cheap flight is found, it will print simulated email notifications for all users in `users.csv`.

## File Structure

- `main.py`: The main entry point for the application.
- `data_manager.py`: Manages all communication with the local CSV data files.
- `flight_search.py`: Handles searching for flights using the Amadeus API.
- `flight_data.py`: A data class for structuring flight information.
- `notification_manager.py`: Responsible for sending notifications.
- `add_user.py`: The script for adding new users.
- `flight_deals.csv`: The database of flight destinations and target prices.
- `users.csv`: The database of registered users.
- `config.py`: Stores API keys and endpoints.
