weather_c = {
  "Monday": 12,
  "Tuesday": 14,
  "Wednesday":15,
  "Thursday": 14,
  "Friday": 21,
  "Saturday": 22,
  "Sunday": 24,
 }

"""Syntax"""
# weather_f = {new_key:new_value for (key, value) in dictionary.items()} 
result = {weather:((weather_c[weather]*9/5)+32) for (weather, temperature )in weather_c.items()}
print(result)