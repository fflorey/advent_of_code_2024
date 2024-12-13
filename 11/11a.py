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

def blink(stones, times):
    for i in range(times):
        print(f"blinking {i+1} times")
        stones = transform_stones(stones)
        print(stones)
        # list contains number 125?
    return stones

# Example usage
initial_stones = [814, 1183689, 0, 1, 766231, 4091, 93836, 46]
initial_stones = [125,17]
res=0
for i in initial_stones:
    res+=len(blink([i], 25))
    print(res)
print("Total stones: ", res)
blinks = 25
final_stones = blink(initial_stones, blinks)
print(len(final_stones))



