numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

"Python Sequences = list, range, string, tuple"

new_range = [num * 2 for num  in range(1, 5)]
print(new_range)

# List comprehension with conditional statement 
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) < 5]
print(short_names)

Long_names = [name.upper() for name in names if len(name) > 5]
print(Long_names)
