
# try: 
#   file = open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\a_file.txt")
#   a_dictionary = {"key": "value"}
#   # print(a_dictionary["sdfsdf"])
#   print(a_dictionary["key"])
# except FileNotFoundError:
#   file = open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\a_file.txt", "w")
#   file.write("Something")
# except KeyError as error_message:
#   # print("That key does not exist.")
#   print(f"The key {error_message} does not exist.")
# else:   # once the try function triggered that time only the else block will be triggered
#   content = file.read()
#   print(content)
# finally:
#   raise TypeError("This is an error that i made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
