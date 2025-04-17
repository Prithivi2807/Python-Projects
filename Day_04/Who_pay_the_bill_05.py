import random

names_string = input("Give me everybody's names, separated by a"
                     "comma.")
names = names_string.split(", ")
# print(len(names))
rand_num = len(names)

rand = random.randint(0, rand_num)

print(f"{names[rand]} is going to pay the bill. ")