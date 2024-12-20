import heapq
from collections import Counter


def clear_screen():
    print("\033[H\033[J", end='')

def home_screen():
    print("\033[H", end='')

def pos_screen(pos):   
    print(f"\033[{pos[0]};{pos[1]}H",end='')


def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def find_positions(maze):
    start = None
    end = None
    walls = []
    path = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == '#':
                walls.append((row, col))
            elif maze[row][col] == 'S':
                start = (row, col)
                path.append((row, col))
                maze[row][col] = '.'
            elif maze[row][col] == 'E':
                end = (row, col)
                maze[row][col] = '.'
            elif maze[row][col] == '.':
                path.append((row, col))
    return start, end, walls, path

# from 16a
def find_cheapest_path(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_cost = 0
    step_cost = 1

    def neighbors(pos):
        for i, (dy, dx) in enumerate(directions):
            new_pos = (pos[0] + dy, pos[1] + dx)
            if  maze[new_pos[0]][new_pos[1]] != '#':
                yield new_pos, i

    pq = [(0, start, -1)]  # cost, position, direction
    visited = set()

    while pq:
        cost, pos, direction = heapq.heappop(pq)
        if pos in visited:
            continue
        visited.add(pos)

        if pos == end:
            return cost

        for new_pos, new_direction in neighbors(pos):
            if new_pos not in visited:
                new_cost = cost + step_cost
                if direction != -1 and direction != new_direction:
                    new_cost += direction_cost
                heapq.heappush(pq, (new_cost, new_pos, new_direction))

    return float('inf')  # If no path is found


# this def find the possible jump points. These are all point within the manhatten radius of 
# "radius" from the point "point", and which are not a wall
def find_possible_jumps(maze, pos, radius):
    possible_jumps = []
    for r in range(-radius, radius + 1):
        for c in range(-radius, radius + 1):
            if abs(r) + abs(c) <= radius:
                new_r, new_c = pos[0] + r, pos[1] + c
                if 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]) and maze[new_r][new_c] != '#':
                    possible_jumps.append((new_r, new_c))
    return possible_jumps

##############################################################################
# Main

file_path = 'input.txt.small'  
maze = read_maze(file_path)
start, end, walls, path = find_positions(maze)

MINIMUM_SAVING_TIME=10
RADIUS=2


normal_time=find_cheapest_path(maze, start, end)
time_map={}
time_map[start]=normal_time
time_map[end]=0
clear_screen()
print("INITIAL TIME MAP! (len:   ", len(path), ")     ")
counter=0
for pos in path:
    time_map[pos]=find_cheapest_path(maze, pos, end)
    home_screen()
    print(f"    counter: {counter}   - time from point {pos} to end: ", time_map[pos])
    counter +=1

print("Picoseconds to exit: ", normal_time)

savings=[]
saved_time=0
max_saved_time=0
counter=1
clear_screen()
for pos in path:
    print(pos)
    time=find_cheapest_path(maze, start, pos)
    possible_jumps=find_possible_jumps(maze, pos,RADIUS)
    home_screen()
    print(f"Counter:    ",counter,  "        \tof: ", len(path))  
    print("Len Possible jumps: ", len(possible_jumps))
    for jump in possible_jumps:
        jump_time=0
        rest_time=0
        # jumptime is manhatten distance
        jumptime=abs(jump[0]-pos[0])+abs(jump[1]-pos[1])
        rest_time=time_map[jump]
        counter+=1
        saved_time=normal_time-(time+jumptime+rest_time)
        if saved_time>max_saved_time:
            max_saved_time=saved_time
        if saved_time>=MINIMUM_SAVING_TIME:
            savings.append(saved_time)    

# Group savings by their occurrences
savings_counter = Counter(savings)
for saving, count in sorted(savings_counter.items()):
     print(f"{count} occurrences with savings: {saving}")

print("Max time saved: ", max_saved_time)
print("Total number of savings (and result): ", len(savings))