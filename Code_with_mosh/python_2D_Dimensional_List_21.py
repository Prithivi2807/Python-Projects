# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]

# 3x3 matrix  2D list   3 rows --> 3 columns V
#                               
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
# print(matrix[0][1])


# Nested loop to iterate over all the items in this matrix
for row in matrix:
    # print(row)
    for item in row:
        print(item)