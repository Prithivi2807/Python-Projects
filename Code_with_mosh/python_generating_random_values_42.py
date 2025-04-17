# Built in modules in python 
import random

for i in range(3):
    print(random.randint(10, 20))

members = ["John", "mary", "bob", "Mosh"]
leader = random.choice(members)
print(leader)
