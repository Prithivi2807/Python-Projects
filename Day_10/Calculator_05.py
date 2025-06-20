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
   
num1 = int(input("what's the first number?: "))
num2 = int(input("what's the second number?: "))

operation_symbol = input("Enter the symbol: ")

calculation = operations[operation_symbol]
print(calculation(num1, num2))
# calculation 