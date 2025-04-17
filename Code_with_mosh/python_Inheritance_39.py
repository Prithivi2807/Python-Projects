# Parent class
class Animal:
    def __init__(self, name):
        self.name = name # initialize the name attribute

    def speak(self):
        pass # Placeholder method to be overridden by child classes


# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!" # Override the speak method
    
# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())