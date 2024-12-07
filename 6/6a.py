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
position = find_position(map_data)
# find dimensions of the map_data array
rows = len(map_data)
cols = len(map_data[0])

# travel through the map until we are leaving the map
while 0 < position[0] < rows and 0 < position[1] < cols:
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

# print map
for row in map_data:
    print("".join(row))
print()
# count all 'X' in the map_data array
result = sum(row.count('X') for row in map_data)
print(f"Result: {result+1}")
