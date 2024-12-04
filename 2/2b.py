# template for advent of code 2024, day 2, part 1

import re

# Step 1: Read the contents of "input.txt"
with open("input.txt", "r") as file:
    lines = file.readlines()

# Step 2: Initialize an empty list to store the numbers
numbers_list = []
second_chance_list = []

# Step 3: Process each line to extract integers
for line in lines:
    # Use regular expression to find all integers in the line
    numbers = list(map(int, re.findall(r'\d+', line)))
    numbers_list.append(numbers)

def is_jolly(numbers):
    ascending = 0
    newline=numbers[0:]
    for i in range(len(numbers)-1):
        stetig_monoton_error = 0
        if ascending == 1 and numbers[i] - numbers[i+1] > 0:
            stetig_monoton_error = 1
        if ascending == -1 and numbers[i] - numbers[i+1] < 0:
            stetig_monoton_error = 1
        if i == 0:
            if numbers[i] - numbers[i+1] < 0:
                ascending = 1
            if numbers[i] - numbers[i+1] > 0:
                ascending = -1
        if stetig_monoton_error == 1 or numbers[i] - numbers[i+1] == 0 or abs(numbers[i] - numbers[i+1]) > 3:
            # delete current number from newline
            if ( second_run == 0):
                newline.remove(numbers[i])
                # add newline to second_chance_list
                second_chance_list.append(newline)
            return False
    return True

second_run=0
count_jolly = 0
for numbers in numbers_list:
    print(numbers)
    for i in range(len(numbers)):
        check_numbers = numbers[0:i] + numbers[i+1:]
        print("Check run", i, "check_numbers", check_numbers)
        if is_jolly(check_numbers):
            count_jolly += 1
            print("Jolly")
            break
        else:
            print("Not jolly")


print("Safe report", count_jolly)