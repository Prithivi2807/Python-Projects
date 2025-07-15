# # Method 1 Read the file after reading need to use close cmd

# file = open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game\Day_24\my_file.txt")
# contents = file.read()
# print(contents)

# file.close()

# Method 2 Alternative the close the cmd

with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game\Day_24\my_file.txt") as file:
  contents = file.read()
  print(contents)

# Method 1 Write method
with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game\Day_24\new_file.txt", mode="w") as file:
  file.write("\n new_text.")

# method 2 append method
with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Snake_Game\Day_24\new_file.txt", mode="a") as file:
  file.write("\n this words are from appended doc.")
