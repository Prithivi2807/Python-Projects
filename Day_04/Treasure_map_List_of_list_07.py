row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure ?")
# Don't change the code above
# 23
# wRITE YOUR CODE BELOW THIS ROW
horizontal = int(position[0]) #"2"
vertical = int(position[1])  #"3"

# print(map[vertical]) #row 0, 1, 2
# print(map[vertical - 1 ])
selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"
# print(selected_row)

# print(selected_row)
print(f"{row1}\n{row2}\n{row3}")