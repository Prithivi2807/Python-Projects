# import smtplib

# my_email = "tikemon200@gmail.com"
# my_password = "yioebxgjtekqrsln"

# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#   connection.starttls() # Nake this connection secure
#   connection.login(user=my_email, password= my_password)
#   connection.sendmail(from_addr=my_email, 
#                       to_addrs="tikemon200@gmail.com",
#                       msg="Subject: Hello\n\n This is the body of my email")
#   connection.close()


# Experiment 2
# import datetime as dt

# now =dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year= 2000, month= 6, day= 2, hour= 8)
# print(date_of_birth)