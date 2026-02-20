user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
  amount = int(input("Enter the amount to withdaw: "))
  if amount % 10 == 0:
    print("Amount dispensed: ", amount)
  else:
    print("Please enter a multiple of 10.")
else:
  print("Thankyou for using the ATM.")