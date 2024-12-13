import re
import numpy as np

def parse_block(block):
    lines = block.strip().split('\n')
    print("lines:", lines)
    # read all integers from the first line lines[0] with a regular expression
    
    button_a = tuple(map(int, re.findall(r'\d+', lines[0])))
    button_b = tuple(map(int, re.findall(r'\d+', lines[1])))
    prize = tuple(map(int, re.findall(r'\d+', lines[2])))
    return (button_a,button_b,prize)

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    blocks = content.strip().split('\n\n')
    parsed_blocks = [parse_block(block) for block in blocks]
    return parsed_blocks

file_path = "input.txt"
data = read_input_file(file_path)
print(data)


def bruteForceSolver ( button1, button2, xvalue1, yvalue1, xvalue2, yvalue2, xtarget, ytarget):
    solutions=[]
    b2=button2
    while button1*xvalue1+button2*xvalue2 <= xtarget:
        button1+=1
        while button1*xvalue1+button2*xvalue2 <= xtarget:
            print(f"button1: {button1} button2: {button2} value: {button1*xvalue1+button2*xvalue2}")
            button2+=1
            value=button1*xvalue1+button2*xvalue2
            print("Value:", value) 
            if value==xtarget:
                if button1*yvalue1+button2*yvalue2 == ytarget:
                    print(f"found solution! button1: {button1} button2: {button2} value: {value} yvalue: {button1*yvalue1+button2*yvalue2}")
                    solutions.append((button1, button2))
        button2=b2
    print(solutions)
    return solutions


def find_min_tokens(x1, y1, cost1, x2, y2, cost2, xtarget, ytarget):
    a = np.array([[x1, x2], [y1, y2]])
    b = np.array([xtarget, ytarget])
    x = np.linalg.solve(a, b)
    print("x:", x)
    px = int(x[0])-2
    py = int(x[1])-2
    print("px (button1):", px)
    print("py: (button2)", py)
    if px<0 or py<0:
        print("No solution")
        return 0
    solutions = bruteForceSolver(px, py, x1, y1, x2, y2, xtarget, ytarget)
    if len(solutions)==0:
        return 0
    button1, button2 = solutions[0]
    print("button1:", button1)
    print("button2:", button2)
    print("cost:", cost1*button1+cost2*button2)
    return cost1*button1+cost2*button2



result=0
for claw_machine in data:
    tokens = 0
    print(claw_machine)
    button_a, button_b, prize = claw_machine
    print("find_min_tokens:", button_a[0], button_a[1], 3, button_b[0], button_b[1], 1, prize[0], prize[1])
    # tokens = find_min_tokens(button_a[0], button_a[1], 3, button_b[0], button_b[1], 1, prize[0], prize[1])
    tokens = find_min_tokens(button_a[0], button_a[1], 3, button_b[0], button_b[1], 1, prize[0]+10000000000000, prize[1]+10000000000000)
    print("tokens:", tokens)
    result += int(tokens)
print("Result:", result)


# This script leverages the Extended Euclidean Algorithm to efficiently find solutions.




