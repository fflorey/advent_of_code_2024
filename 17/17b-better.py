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


def performCombo ( combo_operand, registers ):
    if combo_operand <= 3:
        return combo_operand
    else:
        if combo_operand == 7:
            print(f"exception-invalid oppcode - terminate")
            exit(1)
        if combo_operand == 4:
            return registers['A']
        if combo_operand == 5:
            return registers['B']
        if combo_operand == 6:
            return registers['C']

def adv ( combo_operand ):
    global registers
    operand = performCombo(combo_operand, registers)
    registers['A'] = int(registers['A']/(pow(2,operand)))

def bxl ( operand):
    global registers
    registers['B'] = registers['B'] ^ operand

def bst ( combo_operand ):
    global registers
    operand = performCombo(combo_operand, registers)%8
    registers['B'] = operand

def jnz ( operand):
    global registers, instruction_ptr
    if registers['A'] != 0:
        instruction_ptr = operand

def bxc ( operand ):
    global registers
    registers['B'] = registers['B'] ^ registers['C']

def out ( combo_operand ):
    global registers, output_buffer
    output_buffer.append(performCombo(combo_operand, registers)%8)

def bdv ( combo_operand ): 
    global registers
    operand = performCombo(combo_operand, registers)
    registers['B'] = int(registers['A']/(pow(2,operand)))

def cdv ( combo_operand ): 
    global registers
    operand = performCombo(combo_operand, registers)
    registers['C'] = int(registers['A']/(pow(2,operand)))

imap = { 0:"adv", 1:"bxl", 2:"bst", 3:"jnz", 4:"bxc", 5:"out", 6:"bdv", 7:"cdv" }

print("imap[0]: ", imap[0])
output_buffer = []
instruction_ptr=0
while instruction_ptr<len(instructions):
    instruction=instructions[instruction_ptr]
    oppcode=instructions[instruction_ptr+1]
    instruction_ptr+=2
    # print(f"Instruction: {instruction} Oppcode: {oppcode}")
    # perform the instruction
    istr = imap[instruction]+'('+str(oppcode)+')'
    print(f"Performing: {istr}")
    eval(istr)
    # print("done....")
    # print(f"Registers: {registers}")
    # print(f"Output: {output_buffer}")
    # print(f"Instruction Pointer: {instruction_ptr}")
    # print("")
    

print("Result (output_bufer as string, seperated by comma): ", ",".join(map(str,output_buffer)))
print("Registers: ", registers)

print("NOW INVERS!")
# now work invers, so we need all the invers operations
def adv ( combo_operand ):
    global registers
    operand = performCombo(combo_operand, registers)
    registers['A'] = registers['A'] * (pow(2,operand))

def bxl ( operand):
    global registers
    registers['B'] = registers['B'] ^ operand

def bst ( combo_operand ):
    global registers
    print("invers called!")
    operand = performCombo(combo_operand, registers)%8
    registers['B'] = operand

def jnz ( operand):
    global registers, instruction_ptr
    if registers['A'] != 0:
        instruction_ptr = operand

def bxc ( operand ):
    global registers
    registers['B'] = registers['B'] ^ registers['C']

def out ( combo_operand ):
    global registers, output_buffer
    output_buffer.append(performCombo(combo_operand, registers)%8)

def bdv ( combo_operand ):
    global registers
    operand = performCombo(combo_operand, registers)
    registers['B'] = registers['A'] * (pow(2,operand))

def cdv ( combo_operand ):  
    global registers
    operand = performCombo(combo_operand, registers)
    registers['C'] = registers['A'] * (pow(2,operand))

imap = { 0:"adv", 1:"bxl", 2:"bst", 3:"jnz", 4:"bxc", 5:"out", 6:"bdv", 7:"cdv" }
print("imap[0]: ", imap[0])
output_buffer = []
instruction_ptr=0
print("instructions: ", instructions)
registers['A'] = 1
while instruction_ptr<len(instructions):
    instruction=instructions[instruction_ptr]
    oppcode=instructions[instruction_ptr+1]
    instruction_ptr+=2
    print(f"Instruction: {instruction} Oppcode: {oppcode}")
    # perform the instruction
    istr = imap[instruction]+'('+str(oppcode)+')'
    print(f"Performing: {istr}")
    eval(istr)
    print("done....")
    print(f"Registers: {registers}")
    print(f"Output: {output_buffer}")
    print(f"Instruction Pointer: {instruction_ptr}")
    print("")
    

print("Result (output_bufer as string, seperated by comma): ", ",".join(map(str,output_buffer)))
print("Registers: ", registers)

print(len(output_buffer))
print(len(instructions))