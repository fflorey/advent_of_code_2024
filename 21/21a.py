import heapq
from itertools import product

def read_codes(filename):
    with open(filename) as f:
        return [line.strip() for line in f]

numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['#', '0', 'A']
]

directional_keypad = [
    ['#', '^', 'A'],
    ['<', 'v', '>']
]

movements = {
    '<': (-1, 0, 1),
    '>': (1, 0, 1),
    '^': (0, -1, 1),
    'v': (0, 1, 1)
}

ROTATION_COST = 0

def a_star_all_paths(start, end):
    global movements, ROTATION_COST, maze
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
                best_paths = [path + [(x, y, 'A')]]
            elif cost == best_cost:
                best_paths.append(path + [(x, y, 'A')])
            continue

        for new_direction, (dx, dy, move_cost) in movements.items():
            new_cost = cost + move_cost
            if new_direction != direction:
                new_cost += ROTATION_COST

            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] != '#':
                if ((nx, ny), new_direction) not in costs or new_cost <= costs[((nx, ny), new_direction)]:
                    costs[((nx, ny), new_direction)] = new_cost
                    priority = new_cost
                    heapq.heappush(pq, (priority, (nx, ny), new_direction, path + [(x, y, new_direction)]))

    return best_cost, best_paths



# find pos on numeric keypad
def find_pos_on_keypad(keypad, char):
    for y, row in enumerate(keypad):
        for x, cell in enumerate(row):
            if cell == char:
                return (x, y)
    return None

def build_type_sequence(path):
    sequence = ""
    for i in range(len(path)):   
        sequence += path[i][2]     
    return sequence

def find_codes(sequence, keyboard_type=numeric_keypad):
    codes=[]
    code = []
    sequence = "A"+sequence
    for i in range(len(sequence) - 1):
        start = find_pos_on_keypad(keyboard_type, sequence[i])
        end = find_pos_on_keypad(keyboard_type, sequence[i+1])
        cost, paths = a_star_all_paths(start, end)
        for path in paths:
            code.append(build_type_sequence(path))
        codes.append(code)
        code=[]
    return codes

# make all possible combinations from codes, but the order of the codes is important
# the result must be a list of strings, not a list of lists
def make_combinations(codes):
    return [''.join(combination) for combination in product(*codes)]

maze=directional_keypad

def find_all_codes(combinations, keypad):
    all_codes=[]
    for sequence in combinations:
        codes=find_codes(sequence, keypad)
        all_codes.append(make_combinations(codes))
    return [item for sublist in all_codes for item in sublist]


def get_digit_from_code(code):
    return int(code[:-1])

def get_n_shortest_strings(combinations, n):
    return sorted(combinations, key=len)[:n]

def get_minimum_for_code(codes):
    global maze
    result=0
    for sequence in codes:
        maze=numeric_keypad
        print(find_codes(sequence))  # ['R', 'D', 'L']
        codes=find_codes(sequence)
        combinations=make_combinations(codes)
        # ok, now we have all combinations, now we are going to find all ways to get them
        # working with directional keypad
        maze=directional_keypad
        combinations=find_all_codes(combinations.copy(), directional_keypad)
        # combinations=get_n_shortest_strings(combinations, 30)
        combinations=find_all_codes(combinations.copy(), directional_keypad)

        min_len=float('inf')
        for code in combinations:
            if len(code)<min_len:
                min_len=len(code)
                min_code=code
        print("MIN CODE: ",min_code, min_len)
        result+=min_len*get_digit_from_code(sequence)
    return result

codes=read_codes("input.txt")
print("Codes:",codes)

print("Result:",get_minimum_for_code(codes))
