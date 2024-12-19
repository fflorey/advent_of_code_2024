import heapq

# Read the input.txt file
def read_input(filename):
    blocks = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split(','))
            blocks.append((x, y))
    return blocks

blocks=read_input('input.txt')
# print("input: ",   blocks)

# print ("blocks: ", len(blocks))

COLS=71
ROWS=71


def print_map(map):
    for row in map:
        print("".join(row))
    print()

def print_blockmap(blocks):
    global ROWS, COLS
    newmap=[]
    for y in range(0,ROWS):
        row=[]
        for x in range(0,COLS):
            if (x,y) in blocks:
                # print("#", end="")
                row.append("#")
            else:
                # print(".", end="")
                row.append(".")
        # print()
        newmap.append(row)
    return newmap

map = print_blockmap(blocks)
print("Now the tranformed map:")
# print_map(map)

print("ROWS:", ROWS, "COLS:", COLS)

maze = map
start = (0, 0)
end = (COLS-1,ROWS-1)
print("Start:", start)
print("End:", end)

def find_cheapest_path(maze, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, up
    direction_cost = 0
    step_cost = 1

    def neighbors(pos, current_direction):
        for i, (dx, dy) in enumerate(directions):
            new_pos = (pos[0] + dx, pos[1] + dy)
            x = new_pos[0]
            y = new_pos[1]
            if  0 <= x < COLS and 0 <= y < ROWS and  maze[new_pos[0]][new_pos[1]] != '#':
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

    exit(1)
    return float('inf')  # If no path is found

# Example usage
# print_map(maze)
cheapest_cost = find_cheapest_path(maze, start, end)
print("steps:", cheapest_cost)
exit(0)

