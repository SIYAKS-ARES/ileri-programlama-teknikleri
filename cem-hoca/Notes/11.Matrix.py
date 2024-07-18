'''# Create a 2D matrix using user input


matrix = [] # Create an empty list

numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))

for row in range(numberOfRows):
    matrix.append([]) # Add an empty new row
    for column in range(numberOfColumns):
        value = eval(input("Enter an element and press Enter: "))
        matrix[row].append(value)
print(matrix)


# Create a 2D matrix with random numbers

import random


matrix = [] # Create an empty list

numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))

for row in range(numberOfRows):
    matrix.append([]) # Add an empty new row
    for column in range(numberOfColumns):
        matrix[row].append(random.randint(0, 99))
print(matrix)


# Printing Lists


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        print(matrix[row][column], end = " ")
print() # Print a new line


# Or you can write:


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for row in matrix:
    for value in row:
        print(value, end = " ")
print()


# Summing All Elements


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
total = 0

for row in matrix:
    for value in row:
        total += value
print("Sum:", total)


# Finding the Maximum & Minimum Element


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
maxValue = matrix[0][0]
minValue = matrix[0][0]

for row in matrix:
    for value in row:
        if value > maxValue:
            maxValue = value
        if value < minValue:
            minValue = value

print("Max value:", maxValue)
print("Min value:", minValue)


# Finding the Average Element

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
total = 0

for row in matrix:
    for value in row:
        total += value
average = total / (len(matrix) * len(matrix[0]))
print("Average:", average)


# Summing Elements by Column


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

for column in range(len(matrix[0])):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
print("Sum for column", column, "is", total)


# Finding the Row with the Largest Sum


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
maxRow = sum(matrix[0]) # Get sum of the first row in maxRow
indexOfMaxRow = 0

for row in range(1, len(matrix)):
    if sum(matrix[row]) > maxRow:
        maxRow = sum(matrix[row])
        indexOfMaxRow = row
print("Row", indexOfMaxRow, "has the maximum sum of", maxRow)


# Random Shuffling


import random


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given

print(len(matrix))

for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        i = random.randint(0, len(matrix) - 1)
        j = random.randint(0, len(matrix[row]) - 1)
        print(matrix)
    # Swap matrix[row][column] with matrix[i][j]
    matrix[row][column], matrix[i][j] = \
        matrix[i][j], matrix[row][column]
print(matrix)'''


# Sorting


points = [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]]
points.sort()
print(points)


matrix = []
matrix.append(3 * [1]) # Adds 3 times 1 in the matrix
matrix.append(3 * [1])
matrix.append(3 * [1])
matrix[0][0] = 2
print(matrix)


matrix = []
matrix.append([3 * [1]])
matrix.append([3 * [1]])
matrix.append([3 * [1]])
print(matrix)
matrix[0] = 3
print(matrix)


matrix = []
matrix.append([1, 2, 3])
matrix.append([4, 5])
matrix.append([6, 7, 8, 9])
print(matrix)