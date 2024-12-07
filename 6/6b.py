# Read the file and store lines in a 2-dimensional array
with open("input.txt", "r") as file:
    map_data = [list(line.strip()) for line in file]

# Find the position point '^' and store its position
def find_position(map_data):
    for i, row in enumerate(map_data):
        for j, char in enumerate(row):
            if char == '^':
                return (i, j)
    return None

def print_map(map_data):
    for row in map_data:
        print("".join(row))
    print()

position = find_position(map_data)
# find dimensions of the map_data array
rows = len(map_data)
cols = len(map_data[0])

# copy the map_data array to orig_map_data
orig_map_data = [list(r) for r in map_data]

# travel through the map until we are leaving the map
print(f"dimensions: {rows} x {cols}")
possible_blocks = 0
# place a '#' in the map_data array from top left to bottom right
for i in range(rows):
    for j in range(cols):        
        map_data = [list(r) for r in orig_map_data]
        position = find_position(map_data)
        if map_data[i][j] == '.':
            map_data[i][j] = '#'
            orig_map_data[i][j] = '#'
            print(f"try number {i*cols+j+1} of {rows*cols}")
            # print("Los gehts...")
            # print_map(map_data)
            # print("orig_map_data")
            # print_map(orig_map_data)
            steps = 0
            while steps < rows*cols+1 and (0 < position[0] < rows and 0 < position[1] < cols):
                row, col = position
                if row - 1 >= 0 and map_data[row - 1][col] != '#':
                    map_data[row][col] = 'X'
                    position = (row - 1, col)
                    row, col = position
                    map_data[row][col] = '^'
                # if the target position is an '#', turn the map by 90 degrees to the left        
                elif col - 1 >= 0 and map_data[row-1][col] == '#':
                    map_data = list(zip(*map_data))[::-1]
                    map_data = [list(y) for y in map_data]
                    position = find_position(map_data)
                    # exchange rows and cols
                    rows, cols = cols, rows
                steps += 1

            # print(f"steps: {steps}")
            if steps == rows*cols+1:
                print("Pos Found. Endless loop")
                possible_blocks += 1
                
            orig_map_data[i][j] = '.'
        

print(f"Possible blocks: {possible_blocks}")

# print map
print_map(map_data)
# count all 'X' in the map_data array
result = sum(row.count('X') for row in map_data)
print(f"Result: {result+1}")
