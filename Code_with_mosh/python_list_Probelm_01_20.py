# Write a program to find the largest number in a list
# My Own Approach

# list_of_numbers = [22, 95, 66, 55, 60, 1999999, 100, 39]
# L_num = 0
# for i in list_of_numbers:
#     if L_num < i:
#         L_num = i
# print(L_num)

numbers = [3, 6, 2, 10, 8, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)