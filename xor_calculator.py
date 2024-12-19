def xor_with_3(number):
    return number ^ 3

# Example usage:
# result = xor_with_3(5)
# print(result)  # Output will be 6 because 5 XOR 3 is 6

def xor_3_then_1(number):
    return number ^ 3 ^ 1

# Example usage:
result = xor_3_then_1(9)
print(result)  # Output will be 7 because (5 XOR 3) XOR 1 is 7
result = 9 ^2 
print(result)

def demonstrate_xor_with_3():
    test_numbers = [1, 2, 10, 100, 1000, 10000, 100000, 1000000]
    results = {num: xor_with_3(num) for num in test_numbers}
    return results

# Example usage:
results = demonstrate_xor_with_3()
print(results)

def xor_with_2(number):
    return number ^ 2

# Example usage:
# result = xor_with_2(5)
# print(result)  # Output will be 7 because 5 XOR 2 is 7

def demonstrate_xor_with_2():
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {num: xor_with_2(num) for num in test_numbers}
    return results

# Example usage:
results = demonstrate_xor_with_2()
print(results)

def demonstrate_xor(a, b):
    return a ^ b

# Example usage:
a = 5
b = 3
result = demonstrate_xor(a, b)
print(f"{a} XOR {b} = {result}")  # Output will be 6 because 5 XOR 3 is 6

def invert_xor_with_3(number):
    return number ^ 3

# Example usage:
original = 5
xor_result = original ^ 3
inverted_result = invert_xor_with_3(xor_result)

print(f"Original: {original}")  # Output will be 5
print(f"After XOR with 3: {xor_result}")  # Output will be 6
print(f"After inverting XOR with 3: {inverted_result}")  # Output will be 5
