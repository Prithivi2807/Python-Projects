student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}


import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# # Looping through dictionaries: 
# for (key, value) in student_data_frame.items():
  # print(key)
  # print(value)
# # Looping through rows of a dataframe:
# print()
for (index, row) in student_data_frame.iterrows():
  # print(row)
  # print(row.student)
  # print(row.score)
  if row.student == "Angela":
    print(row.score)