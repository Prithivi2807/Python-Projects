# class Car:
#     def __init__(self):
#         # Initialize the car with default attributes
#         self.make = "Toyota"
#         self.model = "Corolla"
#         self.year = "2020"


# # Creating an instance using the default constructor
# # car = Car(make="Toyota",model= "Corolla",year= "2020")

# car = Car()
# print(car.make)
# print(car.model)
# print(car.year)

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self): # self --> parameter  # it is a one method 
        print(f"Hi, I am {self.name}")


john = Person("John Smith") #Object 
john.talk()

bob = Person("Bob Smith")
bob.talk()
