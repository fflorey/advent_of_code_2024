import math
from functools import reduce

def read_input_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            x, y = map(int, parts[0][2:].split(','))
            vx, vy = map(int, parts[1][2:].split(','))
            data.append(((x, y), (vx, vy)))
    return data

data = read_input_file('input.txt')
# print(f"read_input_file('input.txt') = {data}")
# data=[((4,4),(2,-3))]

# for all robots, find the number of steps needed to reach the middle of the map in x direction
ROWS=103
COLS=101

# try all possible solution, not more than COLS*ROWS, otherwise it repeats
# the same solution

steps=0
for i in range(COLS*ROWS):
    final_list=[]
    row_checker={}
    for robot in data:
        # check how many robots are in one line 
        final_y=(robot[0][1]+steps*robot[1][1])%ROWS
        final_x=(robot[0][0]+steps*robot[1][0])%COLS
        final_list.append((final_x,final_y))
        if final_y in row_checker:
            row_checker[final_y]+=1
        else:
            row_checker[final_y]=1
    for rc in row_checker:
        if row_checker[rc]>20:
            print(f"row_checker: {row_checker} rc: {rc}, row_checker[rc]: {row_checker[rc]}") 
            # find all robots, which are in the row rc (y == rc)
            all_robots_in_row_rc=[ (robot[0]) for robot in final_list if robot[1]==rc]
            all_robots_in_row_rc.sort()
            print(f"all_robots_in_row_rc: {all_robots_in_row_rc}")
            max_continuesly_robots=0
            continuesly_robots=0
            last_found=1
            for i in range(COLS):
                y=rc
                # if i in all_robots_in_row_rc:
                #    print(f"i: {i}, max_continuesly_robots: {max_continuesly_robots} continuesly_robots: {continuesly_robots}")
                if last_found>=1 and (i in all_robots_in_row_rc):
                    continuesly_robots+=1
                elif last_found==0 and (i in all_robots_in_row_rc):
                    continuesly_robots=1
                    last_found=1
                elif not (i in all_robots_in_row_rc):
                    last_found=0
                    max_continuesly_robots=max(max_continuesly_robots,continuesly_robots)
                    continuesly_robots=0
            print(f"max_continuesly_robots: {max_continuesly_robots}")
            if max_continuesly_robots<20:
                break
            for robot in data:
                # check how many robots are in one line 
                final_y=(robot[0][1]+steps*robot[1][1])%ROWS
                final_x=(robot[0][0]+steps*robot[1][0])%COLS
                final_list.append((final_x,final_y))

            print(f"WOW! more than 10 in one row! SHOW ME! steps: {steps} ")
            grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
            for x,y in final_list:
                grid[y][x] = '#'

            for row in grid:
                print(''.join(row))
            input()
            break
            
    steps+=1

# count all robots in the four quadrants of the map. The middle lines do not count
# as part of the quadrants.
quadrants = [0, 0, 0, 0]
for x, y in final_list:
    # print (x,y, "M: ",COLS//2, ROWS//2)
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

# print("quadrants: ",quadrants)
# multiply all the quadrants to get the result
result = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
print("result: ",result)