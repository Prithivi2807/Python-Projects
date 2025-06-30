import os
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

MENU = {
    "espresso": {
          "ingredients": {
        "water": 50,
        "coffee":18,
      },
          "cost": 1.5,
    },
    "latte": {
          "ingredients":{
        "water": 200,
        "milk": 150,
        "coffee": 24,
      },
          "cost":2.5,
    },
    "cappuccino": {
          "ingredients": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
      },
          "cost": 3.0,
    }
}

def is_resource_sufficient(order_ingredients):
  """Returns True when order can be made, False if ingredients are insufficient."""
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"sorry there is not enough {item}")
      return False
  return True

def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please Insert Coins")
  total = int(input("Enter how many quarters you have ? $"))
  total += int(input("Enter how many dimes you have ? $"))
  total += int(input("Enter how many nickles you have ? $"))
  total += int(input("Enter how many pennies you have ? $"))
  return total

def is_transaction_successful(money_received, drink_cost):
  """Returns True when the payment is accepted, or False if money is insufficient."""
  if money_received >= drink_cost:
    change = round(money_received - drink_cost, 2)
    print(f"Here is ${change} in change.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name, ordered_ingredients):
    """ Deducts the required ingredients from resources and coverts user input into a drink."""
    for item in ordered_ingredients:
      resources[item] -= ordered_ingredients[item]
    print(f"Heres is your {drink_name}☕. Enjoy!")

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

profit = 0
is_on = True

while is_on:
  choice = input("What would you like ? (espresso/latte/cappuccino): ")
  if choice =='off':
    clear()
    is_on = False
  elif choice =="report":
      print(f"Water: {resources['water']}ml ")
      print(f"Milk: {resources['milk']}ml ") 
      print(f"Coffee: {resources['coffee']}g ") 
      print(f"Money: ${profit}") 
  else:
     drink = MENU[choice]
    #  print(drink)
     if is_resource_sufficient(drink['ingredients']):
        payment=process_coins()
        if is_transaction_successful(payment, drink['cost']):
          make_coffee(choice, drink["ingredients"])