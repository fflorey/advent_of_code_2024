def transform_stones(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left = int(str(stone)[:mid])
            right = int(str(stone)[mid:])
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    return new_stones

def blink(mystones):
    stones = {}
    for key in mystones.keys():
#        print("key is: ",key, "number of key: ", mystones[key])
        tmp_stones=transform_stones( [key])
#        print("tmp_stones: ",tmp_stones)
        for i in tmp_stones:
            if i in stones:
                stones[i]+=mystones[key]
            else:
                stones[i]=mystones[key]
        # add all key + values from stones hashmap to my_new_stones
    print("tmp_stones: ", stones)
    for key in stones:
        print("key is: ",key, "number of key: ", stones[key])
    # return the sum of all values in my_new_stones
    return stones


# Example usage
initial_stones = [814, 1183689, 0, 1, 766231, 4091, 93836, 46]
# initial_stones = [125,17]
# create a hashmap of unique elements and the number, how many times they occur in the list (result is a hashmap)
mystones = {}
for i in initial_stones:
    if i in mystones:
        mystones[i]+=1
    else:
        mystones[i]=1
# how many keys are in mystones?
print("Reduced in map: ",len(mystones))
print("Original length: ",len(initial_stones))
input()

blinks=75
res=0
for i in range(blinks):
    print(f"blinking {i+1} times")
    mystones=blink(mystones)
    # print the sum of all values in mystones
    res=sum(mystones.values())
    print("Total stones: ", res)
   

print(f"Blinking blinks times: {blinks}, result is: {res}")



