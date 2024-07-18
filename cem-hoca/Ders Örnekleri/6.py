'''import random

# Generate random floating-point numbers between 0 and 10
number1 = random.uniform(0, 10)
number2 = random.uniform(0, 10)

print(number1, "-", number2, "=?")

# Round the numbers to two decimal places for better readability
number1 = round(number1, 3)
number2 = round(number2, 3)

print(number1, "-", number2, "=?")
result = float(input("Your answer = ? "))

result_sub = round(number1 - number2, 3)  # Round the result to two decimal places
if result == result_sub:
    print("Congratulations!")
else:
    print("Wrong, correct answer is", result_sub)'''


########################################################################################

import random

correct_count = 0
question_count = 3
counter = 0

while counter < question_count:
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)

    print(number1, "-", number2, "=?")
    result = eval(input("Your answer = ? "))

    result_sub = number1 - number2
    if result == result_sub:
        print("Congratulations!")
        correct_count += 1
    else:
        print("Wrong")
    counter += 1

print(correct_count, "/", question_count)

random3 = random.uniform(0, 10)