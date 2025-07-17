# Method 1
# import csv
# with open(r"C:\Users\Hi\Documents\Python Practice\Day_25\weather_data.csv") as data:
#   data = csv.reader(data)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)

# Method 2
import pandas
data = pandas.read_csv(r"C:\Users\Hi\Documents\Python Practice\Day_25_US_State_Game\Pandas_Practice_01\weather_data.csv")
print(data["temp"])
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))\
# Find the mean in the temperature column
# method 1
temperature_avg = sum(temp_list)/ len(temp_list)
print(temperature_avg)

# Method 2
print()
print(data["temp"].mean())

# Find the maximum value in the temp column
print(data["temp"].max())

# Get Data in columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])

# Which row of data is the highest in the week ?
print(data[data["temp"] == data["temp"].max()])

# Find the particular data data
print()
monday = data[data["day"] == "Monday"]
print(f"find a maximum temperature day condition {monday["condition"]}")

# Convert Monday's Temperature to Fahrenheit

monday_temp = int(monday["temp"].iloc[0]) * 9/5 + 32
print(f"converted temp Fahrenheit {monday_temp}")


# Create a Data Frame from scratch
data_dict = {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")