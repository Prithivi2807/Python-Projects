print("Welcome to python pizza deliveries")
bill = 0
size = input("what size pizza do you want ? S, M, L ? ")

if size.lower() == "s":
    bill += 15
elif size.lower() == "m":
    bill += 20
elif size.lower() == "l":
    bill += 25

add_pepperoni = input("Do you want Pepperoni Y or N ? ")
if add_pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill += 3

extra_cheese = input ("Do you want extra cheese ? Y or N ")
if extra_cheese == "y":
    bill += 1

print(f"your total bill amaount ${bill}")
