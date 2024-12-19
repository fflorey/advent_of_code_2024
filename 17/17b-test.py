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

# print(f"Registers: {registers}")
# print(f"Instructions: {instructions}")
output_buffer = []

def performCombo ( registers ):
    global output_buffer
    a=registers['A']
    b=registers['B']
    c=registers['C']
    print(f"Initial values: A={a}, B={b}, C={c}")
    while ( a > 0 ):
        value = a%8
        value2 = a
        print(f"eingabe {value:03b} und {value2:010b}")
        b=a%8  # 3 bits from the right of A
        print(f"b = a%8: {b:03b} (b:{b})")
        b = b ^ 3       
        print(f"b ^= 3: {b:03b} (b:{b})")
        c = a >> b
        print("shift c b bits to the right: ",b, "c: ",c)
        b = b ^ 5 ^ c 
        print(f"b = b ^ 5 ^ c: {b:03b} (b:{b})")
        a >>= 3
        print(f"output ist: {b%8}, mit eingabe {value:03b} und {value2:010b}, a ist jetzt: {a:010b}")
        output_buffer.append(b%8)

registers['A'] = 470
performCombo(registers)
print("Output buffer: ",output_buffer)
input("Press Enter to continue...")

def invertCombo ( ):
    global output_buffer
    a = 0
    b = 0
    c = 0
    while ( len(output_buffer) > 0 ):
        print(f"register values: A={a}, B={b}, C={c}")
        b = output_buffer.pop(0)
        print("b ist: ", b)
        a <<= 3
        a |= b
        print(f"a ist: {a:010b}")
        # ok, a is correct now
        # now b
        b = b ^ 3
        print("shift left: ", b, "oder ", b%8)
        # Ok, shift a by b bits to the left
        c = a << b
        print(f"c = a << b: c:{c:010b} c:{c}")        
        b = b ^ 5 ^ c 
        print(f"b^3 = {b}, {b:010b}")
        print(f"RESULT SO FAR - a = {a}, {a:010b}")

    # value <<= 3
    print(f"Value: {a}")
    return a
registers['A'] = 0
registers['B'] = 0
registers['C'] = 0
output_buffer = [6, 1, 1]
value=invertCombo( )
print("Value: ",value)
registers['A'] = (value)
performCombo(registers)
print("Output buffer: ",output_buffer)
exit(0)

# now the inverted, programm, wie start with the last number of the 
# output buffer as the inout for b
required_buffer = [2,4,1,3,7,5,1,5,0,3,4,3,5,5,3,0]
print ("required bufffer:", required_buffer)
b = required_buffer[-1]
c = 0
print("len required_buffer: ",len(required_buffer))
print("len output_buffer: ",len(output_buffer))
