# enemies = "Skeleton"

# def increase_enemies():
#   enemies = "Zombie"
#   print(f"enemies inside a function: {enemies}")


# increase_enemies()
# print(f"enemies outside a function: {enemies}")

enemies = 1 

def increase_enemies():
  # global enemies  ## it can modify the gloabl scope but it is not recommended
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")