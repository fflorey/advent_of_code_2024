positions = []

ROWS=0
COLUMNS=0
with open("input.txt", "r") as file:
    for row, line in enumerate(file):
        ROWS+=1
        COLUMNS=len(line.strip())
        for column, char in enumerate(line.strip()):
            if char != '.':
                positions.append((char, row, column))

print("Rows:", ROWS)
print("Columns:", COLUMNS)

# make a copy of the positions list
original_positions = positions.copy()
print("Positions:", positions)
superpoints = []
while positions:
    element = positions.pop(0)
    for other in positions:
        if element[0] == other[0]:
            print("Element: ", element, "Other: ", other)
            ## calculate the x- and y-differences between the two elements
            dx = element[1] - other[1]
            dy = element[2] - other[2]
            # calculate two points: One is the position of the first element minus the difference, the other is the position of the second element plus the difference
            point1 = (element[1] + dx, element[2] + dy)
            point2 = (other[1] - dx, other[2] - dy)
            for point in [point1, point2]:
                if (point[0] < 0 or point[0] >= ROWS or point[1] < 0 or point[1] >= COLUMNS):
                    print("Out of bounds")
                    continue                
                if point in superpoints:
                    print("Already added")
                    continue                
                print("Adding superpoint, element:", element[0], "point:", point)            
                superpoints.append(point)

print("Superpoints:", superpoints, "Length:", len(superpoints))
