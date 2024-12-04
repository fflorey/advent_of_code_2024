# template for advent of code 2024, day 2, part 1

import re

# Step 1: Read the contents of "input.txt"
with open("input.txt", "r") as file:
    lines = file.readlines()

# Step 2: Initialize an empty list to store the numbers
numbers_list = []

# Step 3: Process each line to extract integers
for line in lines:
    # Use regular expression to find all integers in the line
    numbers = list(map(int, re.findall(r'\d+', line)))
    numbers_list.append(numbers)

# Now numbers_list contains all the lines with their respective integers
for line in numbers_list:
    print(line)
    ascending = 0
    lastnumber=-1  # indicates that i have not seen any number yet
    for number in line:
        print(number)
        if lastnumber == -1:
            lastname = number
        else:
            


