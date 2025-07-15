#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os

PLACEHOLDER = "[name]"

with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Mail_Merging\Mail_Merge\Input\Names\invited_names.txt") as names_file:
  names = names_file.readlines()
#   print(names)

with open(r"C:\Users\Hi\Documents\Python Practice\Day_24_Mail_Merging\Mail_Merge\Input\Letters\starting_letter.txt") as letter_file:
  letter_contents = letter_file.read()
#   print(letter_contents)

output_dir = r"C:\Users\Hi\Documents\Python Practice\Day_24_Mail_Merging\Mail_Merge\Output\ReadyToSend"

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    # print(new_letter)
    with open(f"{output_dir}\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
       completed_letter.write(new_letter)