def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations={
  "+": add,
  "-": sub, 
  "*": mul,
  "/": div
}

def calculator():
  num1 = int(input("what's the first number?: "))

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to exit.") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()
    
    
calculator()