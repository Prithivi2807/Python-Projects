class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def send_notification(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):
        message = f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}."
        if stop_overs > 0:
            message += f"\nFlight has {stop_overs} stop over, via {via_city}."
        print(message)