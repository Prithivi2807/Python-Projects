## File Not Found
# with open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Catching_Exceptions_01.py\a_file.txt") as file:
#   file.read()

# ## Key Error
# a_directory = {"key": "value"}
# value = a_directory["non_existent_key"]

# # Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # Type Error 
# text = "abc"
# print(text + 3)

# File Not Found Error 

try: 
  file = open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\a_file.txt")
  a_dictionary = {"key": "value"}
  # print(a_dictionary["sdfsdf"])
  print(a_dictionary["key"])
except FileNotFoundError:
  file = open(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\a_file.txt", "w")
  file.write("Something")
except KeyError as error_message:
  # print("That key does not exist.")
  print(f"The key {error_message} does not exist.")
else:   # once the try function triggered that time only the else block will be triggered
  content = file.read()
  print(content)
finally:
  file.close()
  print("File was closed")
