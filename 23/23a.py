import networkx as nx
import matplotlib.pyplot as plt

# Read the order tuples from the input file
tuples = []
printing_rules = []
nodes=set()
# Read order tuples until the first blank line
def read_file (filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            x, y = map(str, line.split('-'))
            nodes.add(x)
            nodes.add(y)
            tuples.append((x, y))


read_file('input.txt')

# Create a  graph
G = nx.Graph()
G.add_edges_from(tuples)

print("tuples:", tuples)
print("nodes:", nodes)

print("Nodes of graph: ", G.nodes())
print("Edges of graph: ", G.edges())    

triangles=[]

for node in nodes:
    for node2 in nodes:
        for node3 in nodes:
            if node != node2 and node2 != node3 and node != node3:
                if G.has_edge(node, node2) and G.has_edge(node2, node3) and G.has_edge(node3, node):
                    tmp=sorted([node, node2, node3])
                    if tmp not in triangles:
                        triangles.append((tmp))


print("len of nodes: ", len(G.nodes()))

# find nodes with max edges:
max_edges=0
max_node=""
        
print("triangles:", triangles)
print("len(triangles):", len(triangles))

# Find triangles with t as the first character of a node
counter=0
for computers in triangles:
    print(computers)
    if computers[0][0] == 't' or computers[1][0] == 't' or computers[2][0] == 't':
        print("found triangle with t:", computers)  
        printing_rules.append(computers)
        counter+=1

print("Counter: ", counter)


# print graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
plt.show()

