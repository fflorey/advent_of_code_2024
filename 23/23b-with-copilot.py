from collections import defaultdict
from itertools import combinations

def read_possible_nodes(filename):
    allnodes=[]
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split(',')
            # strip all nodes
            nodes = [node.strip() for node in nodes]
            if not line:
                break
            allnodes.append(nodes)
    return allnodes

allnodes=read_possible_nodes('./subtrees/input1.txt')

def parse_input(input_lines):
    # print("input_lines:", input_lines)
    graph = defaultdict(set)
    for line in input_lines:
        a, b = line.strip().split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def is_clique(graph, nodes):
    for a, b in combinations(nodes, 2):
        if b not in graph[a]:
            return False
    return True

def find_largest_clique(graph, nodes):
    global allnodes
    max_clique = []
    for size in range(len(nodes), 9, -1):
        for subset in combinations(nodes, size):
            if is_clique(graph, subset):
                print("subset:", subset)
                return sorted(subset)
    return max_clique

def main(input_lines):
    graph = parse_input(input_lines)
    global allnodes
    # nodes = list(graph.keys())
    i=0
    maxlen=0
    max_clique = []
    print("allnodes len:", len(allnodes))
    for nodes in allnodes:
        i+=1
        print("i:", i, " off max:", len(allnodes))
        print("nodes:", nodes)
        largest_clique = find_largest_clique(graph, nodes)
        print("max_clique:", largest_clique)
        if len(largest_clique) > maxlen:
            maxlen=len(largest_clique)
            print("max_clique:", largest_clique)
            max_clique = largest_clique.copy()
            print("i:", i)
        input("return nach max_clique")
    print("maxlen:", maxlen, "clique:", max_clique)
    # sort max_clique and print out
    largest_clique = sorted(max_clique)
    print("largest_clique:", largest_clique)
    return ','.join(largest_clique)

def read_file(filename):
    with open(filename, 'r') as file:
        input_lines = file.read().splitlines()
    # print("input_lines:", input_lines)
    return input_lines

if __name__ == "__main__":
    input_lines = read_file('input.txt')
    print(main(input_lines))
