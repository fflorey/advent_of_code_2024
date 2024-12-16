import heapq


def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze_str=file.read()
    return maze_str


def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()

# Directions: (dx, dy, cost)
DIRECTIONS = {
    'E': (1, 0, 1),
    'W': (-1, 0, 1),
    'N': (0, -1, 1),
    'S': (0, 1, 1)
}

# Rotation costs
ROTATION_COST = 1000

def parse_maze(maze_str):
    return [list(line) for line in maze_str.strip().split('\n')]

def find_start_end(maze):
    start, end = None, None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_all_paths(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    pq = [(0, start, 'E', [])]  # (cost, (x, y), direction, path)
    costs = {(start, 'E'): 0}
    best_cost = float('inf')
    best_paths = []

    while pq:
        cost, (x, y), direction, path = heapq.heappop(pq)

        if (x, y) == end:
            if cost < best_cost:
                best_cost = cost
                best_paths = [path + [(x, y)]]
            elif cost == best_cost:
                best_paths.append(path + [(x, y)])
            continue

        for new_direction, (dx, dy, move_cost) in DIRECTIONS.items():
            new_cost = cost + move_cost
            if new_direction != direction:
                new_cost += ROTATION_COST

            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#':
                if ((nx, ny), new_direction) not in costs or new_cost <= costs[((nx, ny), new_direction)]:
                    costs[((nx, ny), new_direction)] = new_cost
                    priority = new_cost
                    heapq.heappush(pq, (priority, (nx, ny), new_direction, path + [(x, y)]))

    return best_cost, best_paths

def mark_best_paths(maze, paths):
    result=0
    for path in paths:
        for x, y in path:
            if maze[y][x] not in 'SE':
                if maze[y][x] == '.':
                    maze[y][x] = 'O'                
                    result+=1
    print("Result: ",result+2)

def solve_maze_all_paths(maze_str):
    maze = parse_maze(maze_str)
    start, end = find_start_end(maze)
    cost, paths = a_star_all_paths(maze, start, end)
    mark_best_paths(maze, paths)
    return cost, maze, paths

# Example maze
maze_str = read_maze('input.txt')

cost, solved_maze, paths = solve_maze_all_paths(maze_str)
for row in solved_maze:
    print(''.join(row))
print(f"Lowest score: {cost}")
print(f"Number of best paths: {len(paths)}")