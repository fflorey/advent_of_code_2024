import re

# Step 1: Read the contents of "input.txt"
with open("input.txt", "r") as file:
    lines = file.readlines()

# Step 2: Split each line into two integers and store them in separate arrays
array1 = []
array2 = []

for line in lines:
    num1, num2 = map(int, line.split())
    array1.append(num1)
    array2.append(num2)

# Step 3: Sort both arrays
array1.sort()
array2.sort()

# Step 4: Loop over the sorted arrays and print the difference
mysum = 0
for num1 in array1:
    # print num1, numw and num1-num2
    print(num1, array2.count(num1))
    mysum += num1*array2.count(num1)      
    
# Step 5: Print the sum of the differences
print('Sum: ', mysum)



