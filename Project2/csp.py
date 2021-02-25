from collections import defaultdict


class Node:
    def __init__(self) -> None:
        self.neighbors = set()
        self.color = 0

    def add_neighbor(self, node):
        self.neighbors.add(node)

    def is_safe(self, color):
        for n in self.neighbors:
            if n.color == color:
                return False
        return True

def add_edges(nodes, edges):
    node_map = {}
    for node in nodes:
        node_map[node] = Node()

    for edge in edges:
        node_map[edge[1]].add_neighbor(node_map[edge[0]])  # add start node to pred of end node
        node_map[edge[0]].add_neighbor(node_map[edge[1]])  # add end node to succ of start node

    return node_map

def csp(G, node, end, colors):
    for color in range(1, colors+1):
        if G[node].is_safe(color):
            G[node].color = color
            
            if G[node+1] == G[end]:
                return True
                
            if csp(G, node+1, end, colors):
                return True
            G[node].color = 0

    return False



def main():
    colors = None
    nodes = set()
    edges = set()
    with open("data/test1.txt", "r") as txt_file:
        section = 0
        for idx,line in enumerate(txt_file):
            if idx == 0: continue
            if line.startswith("#"): 
                section += 1
                continue

            if section == 1:
                colors = int(line.split(" ")[-1])
            elif section == 2:
                e = line.strip("\n").split(",")
                e[0], e[1] = int(e[0]), int(e[1])

                nodes.add(e[0])
                nodes.add(e[1])
                edges.add(tuple(e))

    G = add_edges(nodes, edges)
    if csp(G, min(G.keys()), max(G.keys()), colors):
        print("There is a {} coloring".format(colors))
    else:
        print("There is not a {} coloring".format(colors))

if __name__ == "__main__":
    main()