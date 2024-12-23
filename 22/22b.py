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
    sequence = []
    for _ in range(n):
        secret = next_secret(secret)
        sequence.append(secret)
    return sequence

def get_prices(secret_sequence):
    return [secret % 10 for secret in secret_sequence]

def get_price_changes(prices):
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]

def read_integers_from_file(filename):
    integers = []
    with open(filename, 'r') as file:
        for line in file:
            integers.append(int(line.strip()))
    return integers

def find_best_sequence(initial_secrets, n):
    all_price_changes = []
    for secret in initial_secrets:
        secret_sequence = generate_secret_sequence(secret, n)
        prices = get_prices(secret_sequence)
        price_changes = get_price_changes(prices)
        print(f"Len of price changes for secret {secret}:", len(price_changes))
        print("first 10 price changes:", price_changes[:10])
        all_price_changes.append(price_changes)

    print("Len of all price changes:", len(all_price_changes))
    best_sequence = None
    max_bananas = 0

    for i in range(len(all_price_changes[0]) - 3):
        sequence = tuple(all_price_changes[0][i:i + 4])
        total_bananas = 0

        for price_changes in all_price_changes:
            for j in range(len(price_changes) - 3):
                if tuple(price_changes[j:j + 4]) == sequence:
                    total_bananas += prices[j + 4]
                    break

        if total_bananas > max_bananas:
            max_bananas = total_bananas
            best_sequence = sequence

    return best_sequence, max_bananas

# Read the initial secret numbers from the input file
initial_secrets = read_integers_from_file('input.txt')

# Find the best sequence and the maximum number of bananas
n = 2000
best_sequence, max_bananas = find_best_sequence(initial_secrets, n)

print("Best Sequence:", best_sequence)
print("Max Bananas:", max_bananas)
