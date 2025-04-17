# How to pass information in your function
def greet_user(first_name, last_name): # Parameters
    print(f"Hi {first_name}{last_name}!")
    print("Welcome aboard") #when ever you create a new function create two spaces


print("Start")
greet_user("John", "Smith") # Posiitional Arguments
greet_user(last_name = "Smith", first_name = "John") # Keyword Arguments
# calc_cost(total = 50, shipping=5, discount = 0.1) # keyword arguments used in numerical values
print("Finish")
greet_user("Mary", last_name="Smith")
