print("Welcome to the rollercoaster")
height = int(input("what is your height in cm ?"))
bill = 0
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("what is your age ?"))
    if age < 12:
        bill = 5
        print("Please pa $5.")
    elif age <=18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $ 12.")
    photo = input("do you want photos ? say yes or no ?")
    if photo == "Y" or "y":
        bill += 3
        print(f"your totol bill amount is ${bill}")
    else:
        print(f"your total bill amount is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")