import heapq

def read_maze(file_path):
    with open(file_path, 'r') as file:
        maze = []
        start = None
        end = None
        for y, line in enumerate(file):
            row = list(line.strip())
            if 'S' in row:
                start = (y, row.index('S'))
            if 'E' in row:
                end = (y, row.index('E'))
            maze.append(row)
    return maze, start, end

# Example usage
file_path = 'input.txt'
maze, start, end = read_maze(file_path)
print("Start:", start)
print("End:", end)

def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()

def find_cheapest_path(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    direction_cost = 1000
    step_cost = 1

    def neighbors(pos, current_direction):
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

        for new_pos, new_direction in neighbors(pos, direction):
            if new_pos not in visited:
                new_cost = cost + step_cost
                if direction != -1 and direction != new_direction:
                    new_cost += direction_cost
                heapq.heappush(pq, (new_cost, new_pos, new_direction))

    return float('inf')  # If no path is found

# Example usage
print_maze(maze)
cheapest_cost = find_cheapest_path(maze, start, end)
print("Cheapest cost:", cheapest_cost)

