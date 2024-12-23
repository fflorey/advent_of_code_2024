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

def get_prices(initial_secret, secret_sequence):
    secret_sequence.insert(0, initial_secret)
    return [secret % 10 for secret in secret_sequence]

def get_price_changes(prices):
    return [prices[i] - prices[i - 1] for i in range(1, len(prices))]

def read_integers_from_file(filename):
    integers = []
    with open(filename, 'r') as file:
        for line in file:
            integers.append(int(line.strip()))
    return integers

ALL_SEQUENCES={}
def find_all_sequences(price_changes, prices, buyer_id):
    global ALL_SEQUENCES
    sequences = set()
    for i in range(len(price_changes) - 3):
        sequence = tuple(price_changes[i:i + 4])
        sequences.add(sequence)
        key = sequence
        if key not in ALL_SEQUENCES:
            ALL_SEQUENCES[key] = [(buyer_id, i, prices[i + 4])]
        else:
            current = ALL_SEQUENCES[key]
            if current[-1][0] == buyer_id:
                # print(f"sequence {key} for user {buyer_id} already exists, skipping")
                continue
            else:
                ALL_SEQUENCES[key].append((buyer_id, i, prices[i + 4]))
    # print("Last sequence:", sequence)


    return sequences

def find_best_sequence(initial_secrets, n):
    all_price_changes = []
    for secret in initial_secrets:
        secret_sequence = generate_secret_sequence(secret, n)
        prices = get_prices(secret,secret_sequence)
        price_changes = get_price_changes(prices)
        # print first 10 price changes
        print(f"Len of price changes for secret {secret}:", len(price_changes))
        print("first 10 price changes:", price_changes[:10])
        all_price_changes.append((prices, price_changes))

    # Find all sequences for all buyers
    for i in range(len(all_price_changes)):
        # print("Buyer", i)
        prices, price_changes = all_price_changes[i]
        find_all_sequences(price_changes, prices, i)
        # print("Number of Sequences:", len(ALL_SEQUENCES.keys()))

    # iterate throuh ALL_SEQUENNCES, sum the prices for each sequence and store the result in a new dictionary
    sequences_sum = {}
    max_sum = 0
    best_sequence = None
    for sequence in ALL_SEQUENCES:
        sum_prices = 0
        for buyer_id, i, price in ALL_SEQUENCES[sequence]:
            if len(ALL_SEQUENCES[sequence]) > 300:
                print("user,price: ", buyer_id, " ", price, "sequence: ", sequence)
            sum_prices += price
        sequences_sum[sequence] = sum_prices
        if sum_prices > max_sum:
            max_sum = sum_prices
            best_sequence = sequence
        if ( sum_prices > 2000 ):
            print("Sequence:", sequence, "Number of Buyers:", len(ALL_SEQUENCES[sequence]))        
            print("Sum of Prices:", sum_prices)
    
    print("fertig!, sequence: ", best_sequence, "sum: ", max_sum)
    
    return best_sequence, max_sum


# Read the initial secret numbers from the input file
initial_secrets = read_integers_from_file('input.txt')

# Find the best sequence and the maximum number of bananas
n = 2000
best_sequence, max_bananas = find_best_sequence(initial_secrets, n)

print("Best Sequence:", best_sequence)
print("Max Bananas:", max_bananas)
