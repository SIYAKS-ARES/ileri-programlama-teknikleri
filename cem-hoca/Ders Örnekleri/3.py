import random

def createMatrix():
    print("Creating a matrix")
    rows = eval(input("Enter the number of rows: "))
    columns = eval(input("Enter the number of columns: "))
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(random.randint(0, 10))
    print("Matrix created")
    print(matrix)
    return matrix

def printMatrix(matrix):
    print("Printing the matrix...")
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column], end="  ")
        print()

def calculateMatrix(matrix):
    print("Performing operations on the matrix...")
    sum_odd = 0
    sum_even = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] % 2 == 0:
                sum_even += matrix[row][column]
            else:
                sum_odd += matrix[row][column]
    return sum_odd, sum_even

def main():
    matrix = createMatrix()
    printMatrix(matrix)
    odd_sum, even_sum = calculateMatrix(matrix)
    print("Sum of odd numbers = ", odd_sum)
    print("Sum of even numbers = ", even_sum)

main()