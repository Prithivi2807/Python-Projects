# Write a program to remove the duplicates in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for num in numbers:
    if num not in uniques:
        uniques.append(num)
print(uniques)