import re

# Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()
    line = ''.join([l.strip() for l in lines])

# Extract all mul expressions
mul_expressions = re.findall(r'mul\(\d+,\d+\)', line)

# Multiply the integers in each mul expression
results = []
mulresult = 0
for expr in mul_expressions:
    print("Expression: ", expr)
    numbers = re.findall(r'\d+', expr)
    result = int(numbers[0]) * int(numbers[1])
    results.append(result)
    mulresult += result

# Print the results
print(results)
print(mulresult)
