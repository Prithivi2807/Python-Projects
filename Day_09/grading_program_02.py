student_scores = {
  "Harry" : 81,
  "Ron" : 78,
  "Hermione" : 99,
  "Draco" : 74,
  "Neville" : 62
}
# Don't change the code above 

# TODO-1 : Create a function called `update_scores` that takes in a dictionary of student names and their corresponding
student_grade={}
# TODO-2 : Write your code below to add the grades to start with the grades of the students in the `student_scores` dictionary.
for student_names in student_scores:
  score = student_scores[student_names]
  # print(score)
  if score > 90: 
    student_grade[student_names] = "Outstanding"
  elif score > 80:
    student_grade[student_names] = "Exceeds Expectations"
  elif score > 70:
    student_grade[student_names] = "Acceptable"
  else:
    student_grade[student_names] = "Fail"
  
print(student_grade)