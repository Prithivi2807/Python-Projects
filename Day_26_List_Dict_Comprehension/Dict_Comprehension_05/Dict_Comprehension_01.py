import random

names = ["Alex", "Beth", "Caroline", "Dave", "Emily"]

# students_scores = {new_key:new_value for item in names}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)


# passed_scores = {new_key: new_value for (key, value) in names if test}
passed_student ={student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_student)