import random

def createArray(size):
    print("Creating an array...")
    array = []
    for i in range(size):
        array.append(random.randint(0, 10))
    print(array)
    return array

def printArray(array):
    print("Printing the array")
    for i in range(len(array)):
        print(array[i], end="  ")
    print()

def sumArray(array):
    print("Performing operations on the array...")
    sum_val = 0
    for i in range(len(array)):
        sum_val += array[i]
    return sum_val

def main():
    size = eval(input("Enter the size of the array: "))
    array = createArray(size)
    printArray(array)
    print("Sum of array elements = ", sumArray(array))

main()

'''
In the given code, len() is a built-in Python function used to return the number of elements in an object.
Here's how it works in the context of your code:
len(array) is used inside the printArray() and sumArray() functions to determine the length of the input array.
In printArray(), len(array) returns the number of elements in the array. This value is used in the for loop to
iterateover each element of the array. In sumArray(), len(array) similarly returns the number of elements in the array.
This value is used in the for loop to iterate over each element of the array and calculate their sum.
So, in summary, len(array) is used to find the number of elements in the array array,
which is crucial for iterating over the elements in the array in both the printing and summing functions.
'''