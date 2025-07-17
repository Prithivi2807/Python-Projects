import pandas as pd

# Read the squirrel data CSV file
data = pd.read_csv(r"C:\Users\Hi\Documents\Python Practice\Day_25_US_State_Game\The Great Squirrel Cences_02\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250716.csv")

# Print unique fur colors
print(data["Primary Fur Color"].unique())

# Count squirrels by fur color
Gray_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_count = len(data[data["Primary Fur Color"] == "Black"])

## Print counts (optional)
print(Gray_count)
print(Cinnamon_count)
print(Black_count)

# Find the max Hectare Squirrel Number
data = data["Hectare Squirrel Number"].max()
print(data)


# Create a dictionary for fur color counts
data_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [Gray_count, Cinnamon_count, Black_count]
}

print(data_dict)

# Convert dictionary to DataFrame and save to CSV
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")