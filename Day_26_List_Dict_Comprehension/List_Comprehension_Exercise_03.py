with open(r"C:\Users\Hi\Documents\Python Practice\Day_26_List_Dict_Comprehension\file1.txt", mode="r") as file_1:
  data_1 = file_1.readlines()

with open(r"C:\Users\Hi\Documents\Python Practice\Day_26_List_Dict_Comprehension\file2.txt", mode="r") as file_2:
  data_2 = file_2.readlines()

result = [int(i) for i in data_1 if i in data_2]
# Write your code above 👆

print(result)