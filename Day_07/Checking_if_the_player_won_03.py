#Step 3

# a = 3 
# if not a > 1: # false
# a = 0 
# if not a > 1: # True

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all
#  the letters in the chosen_word and 'display' has no more 
# blanks ("_"). Then you can tell the user they've won.
while "_" in display:
    guess = input("Guess a letter: ").lower()

#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

print()
print(display)

if "_" not in display: 