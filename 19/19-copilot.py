def count_ways_to_form_design(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]

    return dp[-1]

def count_total_ways(patterns, designs):
    total_ways = 0
    for design in designs:
        total_ways += count_ways_to_form_design(patterns, design)
    return total_ways

# Read the input.txt file
def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()    
        parts = content.split('\n\n')
        towel_patterns = parts[0].strip().split(',')
        designs = parts[1].split('\n')    

    patterns = [p.strip() for p in towel_patterns]
    return patterns, designs

patterns, designs = read_input('input.txt.large')
print(f"DESIGN {len(designs)}")
print(f"towel_patterns: {patterns}")

# Example usage
# patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
# designs = ["brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb"]

print("Total ways: ", count_total_ways(patterns, designs))  # Output: total number of ways

