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


def find_removable_blocks(maze, path):
    removable_blocks = []

    for (row, col) in path:
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (row + direction[0], col + direction[1])
            next_neighbor = (row + 2 * direction[0], col + 2 * direction[1])
            if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and
                maze[neighbor[0]][neighbor[1]] == '#' and
                0 <= next_neighbor[0] < len(maze) and 0 <= next_neighbor[1] < len(maze[0]) and
                maze[next_neighbor[0]][next_neighbor[1]] == '.'):
                if (neighbor) not in removable_blocks:
                    removable_blocks.append(neighbor)

    return removable_blocks



# Example usage
file_path = 'input.txt'  
maze = read_maze(file_path)
start, end, walls, path = find_positions(maze)


print("Start:", start)
print("End:", end)
# print("Walls:", walls)
# print("Path:", path)

normal_time=find_cheapest_path(maze, start, end)
print("Picoseconds to exit: ", normal_time)

savings=[]
saved_time=0
max_saved_time=0
removeable_blocks=find_removable_blocks(maze, path)
counter=1
print("Number of all remoable bblocks:", len(removeable_blocks))
for block in removeable_blocks:
    print("Block number: ", counter)
    counter+=1
    maze[block[0]][block[1]] = '.'
    time=find_cheapest_path(maze, start, end)
    saved_time=normal_time-time
    # print("Picoseconds to exit with block removed: ", time)
    if saved_time>max_saved_time:
        max_saved_time=saved_time
    if saved_time>=100:
        savings.append(saved_time)
    maze[block[0]][block[1]] = '#'

print("Max time saved: ", max_saved_time)
print("Savings: ", savings, "Len: ", len(savings))
