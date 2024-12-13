map = []
with open("input.txt", "r") as file:
    map = [list(line.strip()) for line in file]

def print_map(map):
    for row in map:
        print("".join(row))

print(map)
ROWS=len(map)
COLS=len(map[0])

print("ROWS:", ROWS, "COLS:", COLS)

# make a deep copy of the map to a visited map (visited_map)
visited_map = [['.' for _ in range(COLS)] for _ in range(ROWS)]
print_map(visited_map)  
print_map(map)

def find_starting_point(visited_map):
    for r in range(ROWS):
        for c in range(COLS):
            if visited_map[r][c] == '.':
                return r, c
    return -1, -1

def searchNextField(row, column, plant):
    global fences
    global area
    connected_fields=[(row, column)]
    visited_map[row][column] = 'X'
    directions=[(0,1), (1,0), (0,-1), (-1,0)]
    while len(connected_fields)>0:
        print(f"CHECK FOR fields:", connected_fields)
        row, column = connected_fields.pop()
        area += 1
        print(f"CHECK FOR field: {row}, {column}, area: {area} fences: {fences}")
        visited_map[row][column] = 'X'
        for direction in directions:
            new_row = row + direction[0]
            new_column = column + direction[1]
            if new_row < 0 or new_row >= ROWS or new_column < 0 or new_column >= COLS:
                fences += 1
                print(f"Out of bounds: {new_row}, {new_column} - one more fence for plant {plant}")
                continue
            if map[new_row][new_column] == plant and visited_map[new_row][new_column] == '.':
                print(f"Plant {plant} at {new_row}, {new_column} - area: {area}")
                # append a new field to the list of connected fields if it is not in the list
                if (new_row, new_column) not in connected_fields:
                    connected_fields.append((new_row, new_column))
                continue
            if map[new_row][new_column] != plant:
                print(f"Different Plant {plant} at {new_row}, {new_column} - one more fence")
                fences += 1
                continue
            
    return 
        
fences=0
area=0
result=0
while True:
    row,column=find_starting_point(visited_map)
    print("Starting point:", row, column)
    if row == -1:
        break
    fences=0
    area=0
    searchNextField(row, column, map[row][column])
    print_map(visited_map)
    print("Plant:", map[row][column], "Area:", area, "Fences:", fences)
    result += area*fences
    print("Result:", result)

print("Result:", result)

