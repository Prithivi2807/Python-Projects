import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "Enter your mail"
MY_PASSWORD = "Gmail Security Password"  

"""
https://myaccount.google.com/apppasswords
create your app password through this link

"""
# Get today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Load birthday data
data = pandas.read_csv(r"C:\Users\Hi\Documents\Python_Practice\Day_32_Email_Automation_Project\Birthday_Automation_03\birthdays.csv")

# create a dictionary where each (month, day) maps to a list of people 
birthdays_dict = {}
for (index, data_row) in data.iterrows():
  birthday_key = (data_row["month"], data_row["day"])
  if birthday_key not in birthdays_dict:
    birthdays_dict[birthday_key] = []
  birthdays_dict[birthday_key].append(data_row)


# If today's date is in the dict, send emails to all people having birthday today
if today_tuple in birthdays_dict:
  letter_template = r"C:\Users\Hi\Documents\Python_Practice\Day_32_Email_Automation_Project\Birthday_Automation_03\letter_templates"

  for person in birthdays_dict[today_tuple]:
    try:
      rand_num = random.randint(1,3)
      file_path = f"{letter_template}/letter_{rand_num}.txt"

      with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])    

      with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
          from_addr = MY_EMAIL,
          to_addrs=person["email"], 
          msg=f"Subject: Happy Birthday! \n\n {contents}")
        
      print(f"Email sent to {person["name"]} at {person['email']}")
    except Exception as e:
      print(f"Failed to send to {person['name']}: {e}")