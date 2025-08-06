import smtplib
import datetime as dt
import random

MY_EMAIL = "tikemon200@gmail.com"
MY_PASSWORD = "yioebxgjtekqrsln"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
  with open(r"C:\Users\Hi\Documents\Python_Practice\Day_32_Email_Automation_Project\quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

  print(quote)

  with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=MY_EMAIL,
       msg=f"Subject:Monday Motivation \n\n{quote}"
       )