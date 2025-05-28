# Dice class
# roll tuple method
import random


class Dice():
    def roll(self):
            first = random.randint(1,6)
            second = random.randint(1, 6)
            return first, second # when you separate values by a comma in a 
    # return statement, they are automatically packed into a tuple.


dice = Dice()
print(dice.roll())