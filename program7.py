# Question 7
# Level 2
#
# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
input_str = raw_input()
dimensions=[int(x) for x in input_str.split(',')]
print type(dimensions)
rowNum=dimensions[0]
colNum=dimensions[1]
print [0 for col in range(colNum)]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print multilist

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print multilist
