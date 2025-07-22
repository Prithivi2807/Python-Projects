
# Modify the add function to take an unlimited number of arguments. Use a loop to sum all the arguments inside the function. Test it out by calling add() to calculate sum of some arguments.

# def add(*args):
#   # print(args[1]) # Posiitonal Arguments

#   sum = 0
#   for n in args:
#     sum += n
#   return sum

# print(add(3, 5, 8, 1, 2, 2))


def calculate(n, **kwargs):
  print(kwargs)  # it is stored in a dictionary   # print(type(kwargs))
  # for key, value in kwargs.items():
  #   print(key)
  #   print(value)
  n += kwargs["add"]
  n *= kwargs["multiply"] # add & multiply dict values are used.
  print(n)

calculate(2, add=3, multiply=5)

class Car:
  def __init__(self, **kw):
    self.make = kw.get("make")   # kw argument dict key values are used
    self.model = kw.get("model") # .get method is used if there is no input in model it will return None
    self.colour = kw.get("colour")
    self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)