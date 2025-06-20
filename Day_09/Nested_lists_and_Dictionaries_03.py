
# Nesting a Dictionary in a Dictionary

travel_log={
  "France":{"Cities_visited": ["Paris", "Lille", "dijon"], "Total_visits": 12}, 
  "Germany":{"Cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 5},
}

print(travel_log)

# Nesting a dictionary in a List

travel_log_1=[
  {
    "Country":"France",
    "Cities_visited": ["Paris", "Lille", "dijon"],
    "Total_visits": 12
  }, 
  {
    "Country":"Germany",
    "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "Total_visits": 5
  },
]
print()
print(travel_log_1)