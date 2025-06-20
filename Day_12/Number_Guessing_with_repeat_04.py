import random
import sys
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
print(
"""
Welcome to the Number Guessing game!
I'm thinking of a number between 1 and 100
"""
)
lives = 0

def play():
  play = input("do you want to play again say 'yes' or 'no' ? ")
  if play == 'yes':
    game()
  else: 
    print("good bye")
    sys.exit() #Immediately stop the entire script

def game():
  difficulty = input("Choose a difficulty. Type'easy' or 'hard': ")
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5

  guess_number = random.randrange(0, 100)
  print(guess_number)

  while lives != 0:
    print(f"you have {lives} attempts remaining to guess the number")

    user_number = int(input("Make a guess: "))

    if user_number == guess_number:
      print(f"you guessed the right number {guess_number} in the {lives} attempt.")
      play()
    elif user_number > guess_number:
      print("too high")
      lives -= 1
    elif user_number < guess_number:
      print("too low")
      lives -= 1

  if lives == 0:
    print(f"you lose {lives} you have {lives} lives ?") 
    play()

game()