# Read the file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Parse the integers
data = []
for line in lines:
    numbers = [int(num) for num in line.replace(':', ' ').split()]
    data.append(numbers)

def recursive_check_line ( list, result, accumulator):
    # print (f"rec call with: {list},accu:{accumulator}, result:{result}")
    if len(list) == 0:  
        if result == accumulator:
            print("perfect!")
            return True
        else:
            return False
    element=list.pop()
    if recursive_check_line(list.copy(), result, accumulator*element) == True:
        return True
    if recursive_check_line(list.copy(), result, accumulator+element) == True:
        return True
    return False
            
overall_result = 0
for line in data:
    if not line:
        continue
    result = line.pop(0)
    # revert the list line, so that we can evaluate from left to right by using pop()
    line = list(reversed(line))
    first_element = line.pop()

    if recursive_check_line(line,result,first_element):
        overall_result += result
        print("yes!")
    else:
        print("oh no :-(")


print("Overall: ",overall_result)





    






