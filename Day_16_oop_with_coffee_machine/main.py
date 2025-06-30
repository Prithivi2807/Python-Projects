from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
"""
MenuItem Class - name, cost, ingredients
Menu Class - get_item(), find_drink(order_name)
CoffeeMaker Class - report(), is_resource_sufficient(drink),make_coffee(order)
MoneyMachine Class - report(), make_payment(cost)
"""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# coffee_maker.report()
# money_machine.report()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"what would you like? ({options}) ")
  if choice == "off":
      is_on = False
  elif choice == "report":
     coffee_maker.report()
     money_machine.report()
  else:
     drink = menu.find_drink(choice)
     if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)