programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that can be called multiple times from different parts of a program.",
  "Variable": "A value that can be changed by the program."
}

# Retrieving items from dictionary
# print(programming_dictionary["Bug"])
# print()
# print()

# print(programming_dictionary["Function"])

# Adding New items to dictionary 
programming_dictionary["Loop"] = "The Action of doing something over and over again."

# Create an empty dictionay.
empty_dictionary = {}

# Wipe an existing dictioanry
# programming_dictionary = {}
# print(programming_dictionary)

# loop through a dictionary 
for Key in programming_dictionary:
  print(Key)
  print(programming_dictionary[Key])