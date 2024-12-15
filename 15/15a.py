def read_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split('\n\n')
        print(content)    
    map_part = content[0].split('\n')
    instructions = content[1]
    map_array = [list(line) for line in map_part]
    return map_array, instructions



# Example usage
map_array, instructions = read_input('input.txt')
ROWS=len(map_array[0])
COLS=len(map_array)
print(f"rows: {ROWS}, cols: {COLS}")
print("first 10 instructions:", instructions[:10])

def printMap(map_array):
    for line in map_array:
        print(''.join(line))

def findStartPosition(map_array):
    for y, line in enumerate(map_array):
        for x, cell in enumerate(line):
            if cell == '@':
                return (x, y)
    return None

def storePositionsOfGoods(map_array):
    stones = {}
    for y, line in enumerate(map_array):
        for x, cell in enumerate(line):
            if cell == 'O':
                stones[(x, y)] = True
    return stones

def storePositionsOfWalls(map_array):
    walls = {}
    for y, line in enumerate(map_array):
        for x, cell in enumerate(line):
            if cell == '#':
                walls[(x, y)] = True
    return walls

def isMoveable(map_array, x, y, dx, dy):
    if map_array[y + dy][x + dx] == '.':
        map_array[y + dy][x + dx] = 'O'
        map_array[y][x] = '.'
        return True
    if map_array[y + dy][x + dx] == 'O':
        if isMoveable(map_array, x + dx, y + dy, dx, dy):
            map_array[y + dy][x + dx] = 'O'
            map_array[y][x] = 'O'
            return True
    return False

printMap(map_array)

stones=storePositionsOfGoods(map_array)
posx, posy = findStartPosition(map_array)
print(f"posx: {posx}, posy: {posy} thereis: {map_array[posy][posx]}")
for i in range(len(instructions)):
    if instructions[i] == '\n':
        continue
    directions={'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    print(f"instruction: {instructions[i]}, direction: {directions[instructions[i]]} : ")
    dx, dy = directions[instructions[i]]
    new_posx, new_posy = posx + dx, posy + dy
    print(f"new_posx: {new_posx}, new_posy: {new_posy}")
    if map_array[new_posy][new_posx] == '.':
        map_array[posy][posx] = '.'
        map_array[new_posy][new_posx] = '@'
        posx, posy = new_posx, new_posy
    if map_array[new_posy][new_posx] == '#':
        print("wall")
        continue
    if map_array[new_posy][new_posx] == 'O':
        if isMoveable(map_array, new_posx, new_posy, dx, dy):
            map_array[posy][posx] = '.'
            map_array[new_posy][new_posx] = '@'
            posx, posy = new_posx, new_posy
    # printMap(map_array)
    # print("")
    # input()
    
goods=storePositionsOfGoods(map_array)
# iterate throudh the dictionary and calculate a result by summing up the coordinates where the x coordinate is counted as 1 and the y coordinate is counted as 100
result = sum([x + 100*y for x, y in goods.keys()])
print(result)