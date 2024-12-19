def parse_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
    
    parts = content.split('\n\n')
    registers_part = parts[0].split('\n')
    program_part = parts[1].split(': ')[1]
    
    registers = {}
    for line in registers_part:
        name, value = line.split(': ')
        registers[name.split(' ')[1]] = int(value)
    
    instructions = list(map(int, program_part.split(',')))
    
    return registers, instructions

registers, instructions = parse_input('input.txt')

print(f"Registers: {registers}")
print(f"Instructions: {instructions}")

# coding programm by hand
# 2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0
output_buffer = []

def performCombo ( registers ):
    global output_buffer
    a=registers['A']
    b=registers['B']
    c=registers['C']
    print(f"Initial values: A={a}, B={b}, C={c}")
    while ( a > 0 ):
        # print a as binary
        print(f"binary: {a:018b}")
        # 0,3
         # right shift A by 3 bits
        a = a//2**3
        print(f"a after shift binary: {a:018b}")
        # 5,4
        # output a
        print("Output: ",a%8, "(A was: {a:010b}")
        output_buffer.append(a%8)
        print(f"register values: A={a}, B={b}, C={c}")


def invertCombo ( ):
    global output_buffer

    value = 0
    while ( len(output_buffer) > 0 ):
        # 5,3
        a = output_buffer.pop(-1)
        print(f"a = {a}, output_buffer.pop() = {a:010b}")
        # 5,5
        value <<= 3
        value |= a
        print(f"value = {value}, {value:010b}")
    value <<= 3
    print(f"Value: {value}")
    return value


registers['A'] = 0b000011100101011000000
registers['B'] = 0
registers['C'] = 0
output_buffer = [0,3,5,4,3,0]
value=invertCombo( )
print("Value: ",value)
registers['A'] = value
registers['B'] = 0
registers['C'] = 0
performCombo(registers)

print("Output buffer: ",output_buffer)

# now the inverted, programm, wie start with the last number of the 
# output buffer as the inout for b
required_buffer = [0,3,5,4,3,0]
print (required_buffer)
b = required_buffer[-1]
c = 0
print("len required_buffer: ",len(required_buffer))
print("len output_buffer: ",len(output_buffer))
