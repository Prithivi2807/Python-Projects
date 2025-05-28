import random

print("Welcome to the game")
dice = random.randint(0, 1)
if dice == 0:
    print("Heads")
else :
    print("Tails")