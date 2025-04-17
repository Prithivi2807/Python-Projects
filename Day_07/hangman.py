from words import words
import random

def hangman():
    word = random.choice(words).upper()
    guessed = set()
    tries = 6
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
    
    while tries > 0 and not set(word).issubset(guessed):
        print('\n' + ' '.join([c if c in guessed else '_' for c in word]))
        guess = input("Guess letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        elif guess in word:
            guessed.add(guess)
        elif guess in guessed:
            print("You already guessed the letter", guess)
        else:
            tries -= 1
            print(stages[6 - tries])
    
    print(f"Word was: {word}")
    if set(word).issubset(guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost.")

hangman()







# step 1

word_list = ["ardvard", "baboon", "camel"]

# Todo 1 - Randomly choose a word from the word_list 
# and assign it to a variable called chosen_word.

# Todo 2 - Ask the user to guess a letter and assign 
# their answer to a variable called guess. Make guess
lowercase.

# Todao 3 - Check if the letter the user guessed (guess)
# is one of the letters in the chosen_word.

