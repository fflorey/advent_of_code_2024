positions = []

def printMap(superpoints, ROWS, COLUMNS):
    for row in range(ROWS):
        for column in range(COLUMNS):
            if (row, column) in superpoints:
                print("X", end="")
            else:
                print(".", end="")
        print()

ROWS=0
COLUMNS=0
# hashmap to check if an "antenna" is more than once in the list
check_antennas = {}
with open("input.txt", "r") as file:
    for row, line in enumerate(file):
        ROWS+=1
        COLUMNS=len(line.strip())
        for column, char in enumerate(line.strip()):
            if char != '.':
                positions.append((char, row, column))
                if char in check_antennas:
                    check_antennas[char] += 1
                else:
                    check_antennas[char] = 1

# for exercise 8b): all antennas needs to be taken into account - but "single" antennas are not valid
valid_antennas = 0
for antenna in check_antennas:
    if check_antennas[antenna] > 1:
        valid_antennas += check_antennas[antenna] 

print("Rows:", ROWS)
print("Columns:", COLUMNS)

# make a copy of the positions list
original_positions = positions.copy()
superpoints = []
checkpoints = []
# add all positions and only the position) from the original list to the superpoints list
for position in original_positions:
    checkpoints.append((position[1], position[2]))
while positions:
    element = positions.pop(0)
    for other in positions:
        if element[0] == other[0]:
            ## calculate the x- and y-differences between the two elements
            dx = element[1] - other[1]
            dy = element[2] - other[2]
            for i in range(1,int(ROWS)):                
            # calculate two points: One is the position of the first element minus the difference, the other is the position of the second element plus the difference
                point1 = (element[1] + dx*i, element[2] + dy*i)
                point2 = (other[1] - dx*i, other[2] - dy*i)
                for point in [point1, point2]:
                    if point[0] < 0 or point[0] >= ROWS or point[1] < 0 or point[1] >= COLUMNS:
                        continue                
                    if point in superpoints:
                        continue            
                    if point in checkpoints:
                        continue
                    superpoints.append(point)

printMap(superpoints, ROWS, COLUMNS)
print("Result (superpoints + valid antennas):", len(superpoints) + valid_antennas)