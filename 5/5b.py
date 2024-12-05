import networkx as nx
# import matplotlib.pyplot as plt

# Read the order tuples from the input file
order_tuples = []
printing_rules = []
with open("input.txt", "r") as file:
	lines = file.readlines()
	
# Read order tuples until the first blank line
for line in lines:
	line = line.strip()
	if not line:
		break
	x, y = map(int, line.split('|'))
	order_tuples.append((x, y))

# Read the remaining lines into printing_rules
printing_rules = [line.strip() for line in lines[len(order_tuples) + 1:] if line.strip()]
	
# Print the printing rules
print("Printing rules:", printing_rules)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from(order_tuples)


def is_valid_path2(G, nodes):
    for i in range(len(nodes) - 1):
        if not G.has_edge(nodes[i], nodes[i + 1]):
            return False
    return True    

def correct_path(G, nodes):
    """Correct the sequence of integers in path to form a valid path through the directed graph G."""
    corrected_path = nodes
    while not is_valid_path2(G,corrected_path):
        check_path = corrected_path
        for i in range(len(check_path)-1):
            if not G.has_edge(check_path[i], check_path[i + 1]):
                # exchange the node at pos i with i+1 in check_path
                temp = check_path[i]
                check_path[i] = check_path[i+1]
                check_path[i+1] = temp
                corrected_path = check_path
    return corrected_path

# Example usage of the function
result = 0
for rule in printing_rules:
    nodes = list(map(int, rule.split(',')))
    if not is_valid_path2(G, nodes):
        print(f"The path {nodes} is not valid. Correcting...")
        corrected_path = correct_path(G, nodes)
        mid_node = corrected_path[len(corrected_path) // 2]
        result += mid_node

print(f"Result: {result}")

# Draw the graph (at end of program as it blocks further execution)
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
# plt.show()
