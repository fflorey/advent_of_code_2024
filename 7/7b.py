# Read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Parse the integers
data = []
for line in lines:
    numbers = [int(num) for num in line.replace(':', ' ').split()]
    data.append(numbers)

def recursive_check_line ( list, result, accumulator):
    if len(list) == 0:  
        if result == accumulator:
            return True
        else:
            return False
    element=list.pop()
    # concatenate the accumulator with the element as a new integer
    if recursive_check_line(list.copy(), result, int(str(accumulator)+str(element))) == True:
        return True
    if recursive_check_line(list.copy(), result, accumulator*element) == True:
        return True
    if recursive_check_line(list.copy(), result, accumulator+element) == True:
        return True
    return False
            

overall_result = 0
i=0
for line in data:
    i+=1
    if not line:
        continue
    result = line.pop(0)
    print(f"checking line {i} of {len(data)}")
    # revert the list line, so that we can evaluate from left to right by using pop()
    line = list(reversed(line))
    first_element = line.pop()
    if recursive_check_line(line,result,first_element):
        overall_result += result

print("Overall: ",overall_result)





    






