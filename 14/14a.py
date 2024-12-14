def read_input_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            x, y = map(int, parts[0][2:].split(','))
            vx, vy = map(int, parts[1][2:].split(','))
            data.append(((x, y), (vx, vy)))
    return data

data = read_input_file('input.txt.small')
print(f"read_input_file('input.txt') = {data}")
# data=[((2,4),(2,-3))]


ROWS=7
COLS=11
steps=0
for i in range(10):
    final_list=[]
    for robot in data:
        print("r",robot, robot[1][0], robot[1][1])
        final_x=(robot[0][0]+steps*robot[1][0])%COLS
        final_y=(robot[0][1]+steps*robot[1][1])%ROWS
        final_list.append((final_x,final_y))
        steps+=7*11

    print("fl: ",final_list)
    # visualize the final list in a ROWS x COLS grid
    grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
    for x,y in final_list:
        grid[y][x] = '#'

    for row in grid:
        print(''.join(row))
    input()

# count all robots in the four quadrants of the map. The middle lines do not count
# as part of the quadrants.
quadrants = [0, 0, 0, 0]
for x, y in final_list:
    print (x,y, "M: ",COLS//2, ROWS//2)
    if y == ROWS//2 or x == COLS//2:
        continue
    if y < ROWS // 2:
        if x < COLS // 2:
            quadrants[0] += 1
        else:
            quadrants[1] += 1
    else:
        if x < COLS // 2:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

print("quadrants: ",quadrants)
# multiply all the quadrants to get the result
result = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print("result: ",result)