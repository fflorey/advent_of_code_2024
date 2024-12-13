import re

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


def bruteForceSolver ( claw_machine):
    button_a, button_b, prize = claw_machine
    print("button_a:", button_a)
    print("button_b:", button_b)
    print("prize:", prize)
    print("")
    xtarget = prize[0]
    ytarget = prize[1]
    xvalue1 = button_a[0]
    yvalue1 = button_a[1]
    xvalue2 = button_b[0]
    yvalue2 = button_b[1]
    maxx1 = xtarget//xvalue1
    maxx2 = xtarget//xvalue2
    maxy1 = ytarget//yvalue1
    maxy2 = ytarget//yvalue2
    print("maxx1:", maxx1)
    print("maxx2:", maxx2)
    print("maxy1:", maxy1)
    print("maxy2:", maxy2)
    button1=0
    button2=0
    solutions=[]
    while button1*xvalue1+button2*xvalue2 <= xtarget:
        button1+=1
        while button1*xvalue1+button2*xvalue2 <= xtarget:
            # print(f"button1: {button1} button2: {button2} value: {button1*xvalue1+button2*xvalue2}")
            button2+=1
            value=button1*xvalue1+button2*xvalue2
            # print("Value:", value) 
            if value==xtarget:
                if button1*yvalue1+button2*yvalue2 == ytarget:
                    print(f"found solution! button1: {button1} button2: {button2} value: {value} yvalue: {button1*yvalue1+button2*yvalue2}")
                    solutions.append((button1, button2))
        button2=0
    print(solutions)
    return solutions
      
 
result=0
for claw_machine in data:
    print(claw_machine)
    solution_list=bruteForceSolver(claw_machine)
    # print(f"claw_machine {claw_machine} has {len(solution_list)} solutions")
    if len(solution_list)==1:
        print(f"claw_machine {claw_machine} has {len(solution_list)} solutions")
        for solution in solution_list:
            print(f"Solution: {solution}")
            tokens=solution[0]*3+solution[1]*1
            result+=tokens
    elif len(solution_list)>1:
        print("MORE THAN ONE SOLUTION")

print("Result:", result)



