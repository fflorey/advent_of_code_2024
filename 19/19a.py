
# Read the input.txt file
def read_input(filename):
    patterns={}
    with open(filename, 'r') as file:
        content = file.read().strip()    
        parts = content.split('\n\n')
        towel_patterns=parts[0].strip().split(',')
        designs=parts[1].split('\n')    
    for p in towel_patterns:    
        starts_with = p.strip()[0]
        if starts_with not in patterns:
            patterns[starts_with] = [p.strip()]
        else:
            patterns[starts_with].append(p.strip())  

    return patterns, designs



towel_patterns,designs=read_input('input.txt.large')
print(f"DESIGN {len(designs)}")
print(f"towel_patterns: {towel_patterns}")

startpoints={}
for design in designs:
    start=[]    
    print(f"design: >{design}<")
    starts_with=design[0]
    # print(f"starts_with: {starts_with}")
    if starts_with in towel_patterns:
        for p in towel_patterns[starts_with]:
            # print(f"p: >{p}<")
            if design.startswith(p):
                # print(f"design: {design} starts with p: {p}")
                start.append(p)
    else:
        print(f"design: {design} does not start with any p")    

    print(f"start: {start}")

    startpoints[design]=start

print(f"startpoints: {startpoints}")


def findPossibleStart(design, possible_starts):
    global towel_patterns
    starts_with=design[0]
    if starts_with in towel_patterns:
        for p in towel_patterns[starts_with]:
            if design.startswith(p):
                possible_starts.append(p)
    return possible_starts

find_counter=0
def findDesignPattern(design, startpoints, used_towels=[], solutions=[]):    
    global towel_patterns, find_counter
    orig_design=design 
    for start in startpoints:
        used_towels.append(start)
        print(f"design: {design}, start: {start}")
        design=orig_design[len(start):]   # remove the start from the design
        print(f"design after deleting start: {design}")
        if len(design)==0:
            print(f"design: {design} is FOUND")
            find_counter+=1
            solutions.append(used_towels)
            return True
        possible_starts=[]
        possible_starts=findPossibleStart(design, possible_starts.copy())
        print(f"for design >{design}< possible_starts: {possible_starts}")
        if len(possible_starts)>0:            
            if findDesignPattern(design, possible_starts.copy(), used_towels.copy(), solutions):
                return True
        else:
            used_towels.pop()
        
    return False
    


found=set()
for design in startpoints:
    print(f"DESIGN: {design} starts with: {startpoints[design]}")
    solution=[]
    if len(startpoints[design]) > 0:
        print(f"design: {design} has startpoint")
        solultion=findDesignPattern(design, startpoints[design],[],[])
        if solution == True:
            print(f"FOUND! design: {design} has solution! {solultion}")
            found.add(design)

        
print("found solutions: ", found, " total: ", len(found), "find_counter: ", find_counter)