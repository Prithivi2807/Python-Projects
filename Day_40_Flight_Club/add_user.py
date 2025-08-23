import csv
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
users_csv_path = os.path.join(script_dir, 'users.csv')

print("Welcome to the Flight Club!")
print("We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email1 = "initial"
email2 = "confirmation"

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit":
        exit()
    email2 = input("Type your email again. ")
    if email2.lower() == "quit":
        exit()
    if email1 != email2:
        print("Emails do not match. Please try again.")

print("You're in the club!")

# Append the new user to the CSV file
with open(users_csv_path, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([first_name, last_name, email1])
