import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv(r"C:\Users\Hi\Documents\Python_Practice\Day_26_List_Dict_Comprehension\NATO_Alphabet_Project_05\nato_phonetic_alphabet.csv")
# print(data)
student_letter = {row.letter:row.code for (index, row) in data.iterrows()}
# print(student_letter)
print(student_letter)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a Word: ").upper()
result=[student_letter[letter] for letter in word]
print(result)