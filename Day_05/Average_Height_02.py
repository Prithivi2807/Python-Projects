student_heights = input("Input a list of a student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
print(type(student_heights))
print()
# for i in studenttotal_height_heights:
total_height = 0
for i in student_heights:
    total_height += i
print(total_height)

# 156 178 165 171 187
# don't use length and sum function

# average_height = (total_height / number_of_students)

total_students = 0
for s in student_heights:
    total_students += 1
print(total_students)

average_height = total_height / total_students 
print(average_height)

