

class Good:
    def __init__(self, x, y):
        self.x = x*2
        self.y = y
        self.positions=[]
        self.positions.append((self.x, self.y))
        self.positions.append((self.x+1,self.y))    

    def isHit(self, x, y):
        if (x, y) in self.positions:
            return True
        return False
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.positions=[]
        self.positions.append((self.x, self.y))
        self.positions.append((self.x+1,self.y))

    def isInMoveables(self):
        global MOVEABLES
        for g in MOVEABLES:
            if g == self:
                return True
        return False
    
    def isMoveable(self, dx, dy):
        global FINAL_MAP, MOVEABLES
        # check if there is a wall on the new position
        if FINAL_MAP[self.y+dy][self.x+dx] == '#' or FINAL_MAP[self.y+dy][self.x+dx+1] == '#':
            # print("wall found, so no move")
            return False
        # can be moved, so add it to the MOVEABLES list
        if not self.isInMoveables():
            MOVEABLES.append(self)
        moveable=True
        for pos in self.positions:
            global GOODS
            if not noGoodAtPosition(pos[0]+dx, pos[1]+dy):
                g=getGoodAtPosition(pos[0]+dx, pos[1]+dy)
                if g == self:
                    continue
                if not g.isMoveable(dx, dy):
                    moveable=False
        return moveable

    def printPositions(self):
        print(self.positions)

    def __str__(self):
        return f"Good at {self.x}, {self.y}"
    
class Player:
        def __init__(self, x, y):
            self.x = x*2
            self.y = y
    
        def move(self, dx, dy):
            self.x += dx
            self.y += dy
    
        def __str__(self):
            return f"Player at {self.x}, {self.y}"


def read_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split('\n\n')
    
    map_part = content[0].split('\n')
    instructions = content[1]
    
    map_array = [list(line) for line in map_part]
    
    return map_array, instructions


# expand map in x-direction by 2. Only walls and empty spaces will be in final map
# Each Good ('O') will be created as an object in the global GOODS list

MOVEABLES=[]
GOODS=[]
FINAL_MAP=[] 
PLAYER=None
def createExpandedMap(map_array):
    global PLAYER
    global GOODS
    map=[]
    y=0
    for line in map_array:
        string=""
        for i in range(len(line)):
            if line[i] == '#':
                string=string + '##'
            else:
                string=string + '..'
            if line[i] == 'O':
                GOODS.append(Good(i, y))
            if line[i] == '@':
                PLAYER = Player(i, y)
        map.append(string)
        y += 1
    map = [list(line) for line in map]
    return map

def printMap(map_array, withAdditions=False):
    global GOODS, PLAYER
    # make a deep copy of the map_array
    print_array=[line.copy() for line in map_array]
    if withAdditions:
        for good in GOODS:
            for pos in good.positions:
                print_array[pos[1]][pos[0]]='O'
        print_array[PLAYER.y][PLAYER.x]='@'
    for line in print_array:
        print(''.join(line))    

def noGoodAtPosition(x, y):
    global GOODS
    for good in GOODS:
        if good.isHit(x, y):
            return False
    return True

def getGoodAtPosition(x, y):
    global GOODS
    for good in GOODS:
        if good.isHit(x, y):
            return good
    return None

map_array, instructions = read_input('input.txt')
FINAL_MAP=createExpandedMap(map_array)
ROWS=len(FINAL_MAP[0])
COLS=len(FINAL_MAP)
print(f"rows: {ROWS}, cols: {COLS}")
print("Player: ", PLAYER)
printMap(FINAL_MAP, True)
print()

for i in range(len(instructions)):
    posx, posy = PLAYER.x, PLAYER.y
    # printMap(FINAL_MAP,True) 
    if instructions[i] == '\n':
        continue
    directions={'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    dx, dy = directions[instructions[i]]
    new_posx, new_posy = posx + dx, posy + dy
    if FINAL_MAP[new_posy][new_posx] == '.' and noGoodAtPosition(new_posx, new_posy):
        # print("free, so move")
        PLAYER.move(dx, dy)
        continue
    if FINAL_MAP[new_posy][new_posx] == '#':
        # print("wall")
        continue
    if noGoodAtPosition(new_posx, new_posy) == False:
        # print("good in the way - check if we can move it")
        # print all goods
        # for good in GOODS: print(f"good at {good.positions} - {good}")
        g=getGoodAtPosition(new_posx, new_posy)
        MOVEABLES=[]
        if g.isMoveable(dx, dy):
            for good in MOVEABLES:
                good.move(dx, dy)
            PLAYER.move(dx, dy)

    
# iterate throudh the dictionary and calculate a result by summing up the coordinates where the x coordinate is counted as 1 and the y coordinate is counted as 100
# result = sum([x + 100*y for x, y in goods.keys()])
printMap(FINAL_MAP, True)
result=0
print(f"Number of goods: {len(GOODS)}")
for good in GOODS:
    result += good.x + 100*good.y
print(result)