enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside a function : {enemies}")

increase_enemies()
print(f"enemies outside a function: {enemies}")
print()

# Global scope
player_health = 10 

def game():
  def drink_potion():
    potion_strength = 2
    print(player_health)

  drink_potion()
print(player_health)

game()