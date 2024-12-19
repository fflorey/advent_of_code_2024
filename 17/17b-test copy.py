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
        # 2,4
        b=a%8  # lowest 3 bits of A
        print(f"b = a%8 = {b}")
        # 1,3
        b = b ^ 3
        print(f"b = b ^3  = {b}")
        # 7,5
        # right-shift a by b bits (max 3)
        c = a//2**b # -> ignore, as c is allways 0
        print(f"c = a//2**b = {c}")
        print(f"binary c: {c:018b}")
        # 1,5
        # 101 for the lowest three bits... no idea for what is that good for
        b = b ^ 5
        print(f"b = b ^5 = {b}")
        # remember: b ^3 ^5 == b ^ 2 
        # 0,3
        # right shift A by 3 bits
        a = a//2**3
        print(f"a = a//2**3 = {a}")
        # 4,3
        b = b ^ c 
        print(f"b = b ^ c = {b}")
        print(f"binary b: {b:018b}")
        # 5,5
        print("Output: ",b%8, "(B was: ",b)
        output_buffer.append(b%8)
        print(f"register values: A={a}, B={b}, C={c}")

def performCombo ( registers ):
    global output_buffer
    a=registers['A']
    b=registers['B']
    c=registers['C']
    # print(f"Initial values: A={a}, B={b}, C={c}")
    while ( a > 0 ):
        # 2,4
        b=a%8  # lowest 3 bits of A
        b = b ^ 3
        c = a >> b 
        # c = a//2**b
        b = b ^ 5
        a >>= 3
        b = b ^ c 
        output_buffer.append(b%8)


for i in range(2**(3*16),2**(3*16+3)):
    if i%1000000 == 0:
        print(f"i={i}")
    registers['A'] = i
    performCombo(registers)
    if output_buffer == [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]:
        print("Found: ",i)
        break
    output_buffer = []

performCombo(registers)
print("Output buffer: ",output_buffer)
exit(0)


def invertCombo ( ):
    global output_buffer
    a = 0
    b = 0
    c = 0
    value = 0
    while ( len(output_buffer) > 0 ):
        print(f"register values: A={a}, B={b}, C={c}")
        # 5,3
        b = output_buffer.pop(-1)
        print(f"b = {b}, output_buffer.pop() = {b:010b}")
        # invert b = b ^ c
        b = (b ^ c)%8
        print(f"b = b^c = {b}, = {b:010b}")
        # invert a = a//2**3
        a <<= 3
        print(f"a = {a}, leftshift by 3 = {a:010b}")
        # invert b = b ^ 5
        b = b ^ 5
        # invert c = a//2**b
        c = a << b

        print(f"c = {c}, leftshift by B:{b} = {c:010b}")        
        # invert b = b ^ 3
        b = b^3 
        print(f"b^3 = {b}, {b:010b}")

        # invert b = a%8
        a = a ^ b
        value = a
        print(f"b = {b}, value = {value} value(Binär) = {value:010b}")
    # value <<= 3
    print(f"Value: {value}")
    return value

registers['A'] = 0b01110101000100100000111000001011110101001011111010
registers['A'] = 0
registers['B'] = 0
registers['C'] = 0
output_buffer = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
value=invertCombo( )
print("Value: ",value)
registers['A'] = (value)
performCombo(registers)
print("Output buffer: ",output_buffer)

# now the inverted, programm, wie start with the last number of the 
# output buffer as the inout for b
required_buffer = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
print ("required bufffer:", required_buffer)
b = required_buffer[-1]
c = 0
print("len required_buffer: ",len(required_buffer))
print("len output_buffer: ",len(output_buffer))
