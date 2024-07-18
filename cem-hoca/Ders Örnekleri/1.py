start_value = eval (input("Enter the start value: "))
start_value_original = start_value
end_value = eval(input("Enter the end value: "))
end_value_original = end_value
if start_value < end_value:
    sum_val = 0
    while start_value < end_value:
        sum_val += start_value
        start_value += 1
else:
    temp = end_value
    end_value = start_value
    start_value = temp
    sum_val = 0
    while start_value < end_value:
        sum_val += start_value
        start_value += 1
print(start_value_original, " to ", end_value_original,
" sum of numbers = ", sum_val)