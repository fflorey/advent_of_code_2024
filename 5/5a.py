import networkx as nx
import matplotlib.pyplot as plt

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

def is_valid_path(G, path):
    """Check if the sequence of integers in path is a valid path through the directed graph G."""
    nodes = list(map(int, path.split(',')))
    for i in range(len(nodes) - 1):
        if not G.has_edge(nodes[i], nodes[i + 1]):
            return False
    return True

# Example usage of the function
result = 0
for rule in printing_rules:
    if is_valid_path(G, rule):
        print(f"The path {rule} is valid.")
        nodes = list(map(int, rule.split(',')))
        mid_node = nodes[len(nodes) // 2]
        print(f"The middle node is {mid_node}.")
        result += mid_node

    else:
        print(f"The path {rule} is not valid.")

print(f"Result: {result}")

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.show()
