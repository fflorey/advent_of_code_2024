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
    newline=numbers[0:]
    for i in range(len(numbers)-1):
        if numbers[i] - numbers[i+1] == 0 or abs(numbers[i] - numbers[i+1]) > 3:
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
    ascending_numbers = sorted(numbers)
    print(ascending_numbers)
    descending_numbers = sorted(numbers, reverse=True)  
    print(descending_numbers)
    if numbers == ascending_numbers:
        print("Ascending")
        # check, if the gap between the numbers is a maximum of 3 and a minimum of 1 
        if is_jolly(numbers):
            count_jolly += 1
            print("Jolly")
        else:
            print("Not jolly")

    elif numbers == descending_numbers:
        print("Descending")
        # check, if the gap between the numbers is a maximum of 3 and a minimum of 1
        if is_jolly(numbers):
            count_jolly += 1
            print("Jolly")
        else:
            print("Not Jolly")
    else:
        print("Neither")
        break

print("Safe report", count_jolly)
second_run=1
print("Second chance list", second_chance_list)
for numbers in second_chance_list:
    print(numbers)
    ascending_numbers = sorted(numbers)
    print(ascending_numbers)
    descending_numbers = sorted(numbers, reverse=True)  
    print(descending_numbers)
    if numbers == ascending_numbers:
        print("Ascending")
        # check, if the gap between the numbers is a maximum of 3 and a minimum of 1 
        if is_jolly(numbers):
            count_jolly += 1
            print("Jolly")
        else:
            print("Not jolly")

    elif numbers == descending_numbers:
        print("Descending")
        # check, if the gap between the numbers is a maximum of 3 and a minimum of 1
        if is_jolly(numbers):
            count_jolly += 1
            print("Jolly")
        else:
            print("Not Jolly")
    else:
        print("Neither")



print("Safe report", count_jolly)