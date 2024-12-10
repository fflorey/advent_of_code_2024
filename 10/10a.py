# ...existing code...

filename="input.txt.large"
# filename="input.txt.small"

with open(filename, "r") as file:
    data = [[int(char) for char in line.strip()] for line in file]

ROWS = len(data)
COLUMNS = len(data[0]) if ROWS > 0 else 0
print(f"Loaded {ROWS}x{COLUMNS} grid from {filename}")

# ...existing code...
# find all 0 in the grid and store them in a list
zeros = []
for i in range(ROWS):
    for j in range(COLUMNS):
        if data[i][j] == 0:
            zeros.append((i, j))

# print the list of 0
print(zeros)
print(data)

# recursive function to find all ways to reach a nine
# from the position 
def getAllWaysToNine(row, columns, value, direction, way):
    global data
    global WAYS
    way.append((row,columns))
    if data[row][columns] == 9:
        if (row,columns) not in WAYS:
            WAYS.append((row,columns))
        print("!FOUND WAY TO NINE!", way, "WAYS: ",WAYS)
        return
    # find next step 
    for dir in directions:
        r = row+dir[0]
        c = columns+dir[1]
        if r<0 or r>=ROWS or c<0 or c>=COLUMNS:
            continue
        target = data[r][c]
        if target==value+1:
            # print(f"target pos=",row+r, columns+c,"target:",target, "value:",value)
            getAllWaysToNine(r, c, target, direction, way.copy())

        

directions=[(-1,0), (0,1), (1,0), (0,-1) ]
direction=0
trailhead=0
for z in zeros:
    way=[]
    WAYS=[]
    getAllWaysToNine(z[0], z[1], 0, direction, way)
    print("WAYS",WAYS, "LEN:",len(WAYS))
    trailhead+=len(WAYS)

print(f"getAllWaysToNine: {WAYS} All possible ways to reach 9 from 0", len(WAYS), "trailhead:",trailhead)
