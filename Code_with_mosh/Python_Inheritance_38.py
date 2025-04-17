class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):  # inherit the mammal function
    def bark(self):
        print("Barking")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

class Frog(Mammal):
    def jump(self):
        print("frog is jumping")


cat1 = Cat()
cat1.be_annoying()

dog1 = Dog()
dog1.walk()

frog1 = Frog()
frog1.jump()
