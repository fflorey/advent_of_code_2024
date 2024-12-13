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
    global toBeDeletedFences
    lines=0
    connected_fields=[(row, column)]
    visited_map[row][column] = 'X'
    directions=[(0,1), (1,0), (0,-1), (-1,0)]
    fences_map=[]
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
                fences_map.append((new_row, new_column, direction))
                print(f"Out of bounds: {new_row}, {new_column} - 1one more fence for plant {plant}")
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
                fences_map.append((new_row, new_column, direction))
                continue
    print("Fences map:", fences_map)
    # print a map with size COLS x ROWS with the fences
    supermap=[['.' for _ in range(2*(COLS+2))] for _ in range(2*(ROWS+2))]
    for fence in fences_map:
        supermap[(fence[0]+1)][(fence[1]+1)] = 'F'
    print_map(supermap)
    while fences_map:
        fence=fences_map.pop()
        lines+=1
        print(f"lines: {lines}")
        check_direction=fence[2]
        toBeDeletedFences=[]
        deleteRecursive(fence[0], fence[1], fences_map, check_direction)
        print(f"Delete fences: {toBeDeletedFences}")
        for fence in toBeDeletedFences:
            fences_map.remove(fence)
        print("Fences map after deleting:", fences_map, "len:", len(fences_map))
    return area*lines 


toBeDeletedFences = []
def deleteRecursive (y,x, fences_map, check_direction):
    directions=[(0,1), (1,0), (0,-1), (-1,0)]
    for direction in directions:
        new_row = y + direction[0]
        new_column = x + direction[1]
        print(f"check for fence at {new_row}, {new_column} with direction {direction}")
        if (new_row, new_column, check_direction) in fences_map:
            if (new_row, new_column, check_direction) in toBeDeletedFences:
                print(f"already deleted fence at {new_row}, {new_column} with direction {check_direction}")
                continue
            print(f"delete fence at {new_row}, {new_column} with direction {check_direction}")
            # fences_map.remove((new_row, new_column, check_direction))
            toBeDeletedFences.append((new_row, new_column, check_direction))
            deleteRecursive(new_row, new_column, fences_map, check_direction)
        else:
            print(f"no fence at {new_row}, {new_column} with direction {check_direction}")

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
    res= searchNextField(row, column, map[row][column])
    print_map(visited_map)
    print("Plant:", map[row][column], "Area:", area, "Fences:", fences, "res:", res)
    result += res
    print("Result:", result)

print("Result:", result)

