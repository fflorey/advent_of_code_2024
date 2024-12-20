import heapq

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
                maze[row][col] = '.'
                path.append((row, col))
            elif maze[row][col] == 'E':
                end = (row, col)
                maze[row][col] = '.'
            elif maze[row][col] == '.':
                path.append((row, col))

    return start, end, walls, path

# from 16a
def find_cheapest_path(maze, start, end):
    global ROWS, COLS
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_cost = 0
    step_cost = 1

    def neighbors(pos):
        for i, (dy, dx) in enumerate(directions):
            new_pos = (pos[0] + dy, pos[1] + dx)
            if 0 < new_pos[0] < ROWS and 0 < new_pos[1] < COLS and  maze[new_pos[0]][new_pos[1]] != '#':
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


def remove_walls_within_radius(maze, point, radius):
    rows, cols = len(maze), len(maze[0])
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == '#':
                distance = abs(row - point[0]) + abs(col - point[1])
                if distance <= radius:
                    maze[row][col] = '.'
    return maze


def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()

# Example usage
file_path = 'input.txt.small'  
maze = read_maze(file_path)
COLS=len(maze[0])
ROWS=len(maze)
start, end, walls, path = find_positions(maze)


print("Start:", start)
print("End:", end)
# print("Walls:", walls)


normal_time=find_cheapest_path(maze, start, end)
print("Picoseconds to exit: ", normal_time)
print("Len of Path:", len(path))
savings=[]
saved_time=0
max_saved_time=0
counter=0

import copy

# i need a deep and full copy of the maze, which contains lists of lists
orig_maze = copy.deepcopy(maze)

for point in path:
    print("Block number: ", point)
    print("find way from start to point")
    time=find_cheapest_path(maze, start, point)
    print("Picoseconds to go from start to point: ", time)
    # make a deep copy of the maze
    maze = remove_walls_within_radius(maze, point, 20)
    print_maze(orig_maze)
    maze[point[0]][point[1]]='X'
    maze[end[0]][end[1]]='E'
    print_maze(maze)
    
    time2=find_cheapest_path(maze, point, end)
    time+=time2
    print("Picoseconds to exit with block removed: ", time)
    input()
    counter+=1
    saved_time=normal_time-time
    # print("Picoseconds to exit with block removed: ", time)
    if saved_time>max_saved_time:
        max_saved_time=saved_time
    if saved_time>=50:
        savings.append(saved_time)

    maze = copy.deepcopy(orig_maze)
    # print_maze(maze)


print("Max time saved: ", max_saved_time)
print("Savings: ", savings, "Len: ", len(savings))
