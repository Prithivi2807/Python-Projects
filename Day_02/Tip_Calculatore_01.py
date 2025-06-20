# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00/ 5) * 1.12
# Round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tips = int(input("How much tip would you like to give ? 10, 15, 20 ? "))
people = int (input("How many people to split the bill? "))
# bill_with_tip = tips / 100 * bill + bill
bill_with_tip = bill * (1+ tips /100)
print("Total bill", bill_with_tip)
each_pay = bill_with_tip/people
print(f"each person should pay ${each_pay}")