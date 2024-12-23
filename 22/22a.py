# This file contains functions to read integers from a file and generate secret sequences.

def mix(secret, value):
    return secret ^ value

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, secret // 32)
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)
    return secret

def generate_secret_sequence(initial_secret, n):
    secret = initial_secret
    for _ in range(n):
        secret = next_secret(secret)
    return secret

def read_integers_from_file(filename):
    integers = []
    with open(filename, 'r') as file:
        for line in file:
            integers.append(int(line.strip()))
    return integers

# Read the initial secret numbers from the input file
initial_secrets = read_integers_from_file('input.txt')

# Generate the 2000th secret number for each buyer
n = 2000
final_secrets = [generate_secret_sequence(secret, n) for secret in initial_secrets]

# Sum the 2000th secret numbers
total_sum = sum(final_secrets)

print("Total Sum:", total_sum)
