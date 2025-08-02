# Keyword Method with iterrows()
# {new_key: new_value for (index, row) in df.iterrows()}

import pandas 

# TODO 1. Create a dictionary in this format
data = pandas.read_csv(r"C:\Users\Hi\Documents\Python_Practice\Day_30_Errors_Exception_Json_Data_Improving\Exception_Handling_NATO_Alphabet_Project\nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs. 

def generate_phonetic():
  word = input("Enter a word: ").upper()
  try:
    output_list = [phonetic_dict[letter] for letter in word]
  except KeyError:
    print("Sorry, only in the alphabet please.")
    generate_phonetic()
  else:
    print(output_list)

generate_phonetic()