from random import randint
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against actual answer. 
def check_answer(guess, answer, turns):
  """Checks answer against guess. Returns the number of turns remaining"""
  if guess > answer: 
    print("Too high")
    return turns -1
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print(f"you got it! The answer was {answer}")

# Make function to get difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  # Chooseing a random number between 1 and 100. 
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  # Repeat the guessing functionality if they get it wrong.
  guess = 0 
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")  
 
    # Let the user guess a number. 
    guess = int(input("Make a guess: "))

    # Track the number of turns and reduce by 1 if they get it wrong. 
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("you've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()