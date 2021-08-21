# 2-D list Means list inside a list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# can access the sublist
print(matrix[0])
# can access a certain element in sublist
print(matrix[0][1])
# can modify entire sublist
matrix[0] = [11, 13, 15]
print(matrix)
# can modify particular element
matrix[0][1] = 12
print(matrix)

# print all the elements:

for row in matrix:
    for ele in row:
        print(ele)
