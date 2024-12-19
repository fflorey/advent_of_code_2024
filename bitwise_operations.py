def mod_8(number):
    return number % 8

def mask_lowest_3_bits(number):
    return number & 0b111

# Example usage:
number = 29  # Binary: 11101
mod_result = mod_8(number)
mask_result = mask_lowest_3_bits(number)

print(f"Number: {number}")
print(f"Modulo 8 result: {mod_result}")  # Output will be 5
print(f"Masking lowest 3 bits result: {mask_result}")  # Output will be 5
