class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """
    def __init__(self):
        # In a real application, you would initialize your notification client here
        # e.g., self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        pass

    def send_sms(self, message):
        """Simulates sending an SMS. In a real app, this would use Twilio or similar."""
        print("--- SIMULATING SMS ---")
        print(f"Message: {message}")
        print("----------------------")

    def send_emails(self, emails, message):
        """
        Simulates sending an email to a list of users.
        In a real app, this would use smtplib to send emails.
        """
        print("--- SIMULATING EMAILS ---")
        for email in emails:
            print(f"Sending email to: {email}")
            print(f"Subject: New Low Price Flight!\n{message}")
            print("-------------------------")
