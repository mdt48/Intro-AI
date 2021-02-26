
import sys, os
class Node:
    def __init__(self) -> None:
        self.neighbors = []
        self.color = 0

    def add_neighbor(self, node):
        self.neighbors.append(node)


def add_nodes_edges(nodes, edges):
    node_map = {}
    for node in nodes:
        node_map[node] = Node()

    for edge in edges:
        node_map[edge[1]].add_neighbor(edge[0])  # add start node to pred of end node
        node_map[edge[0]].add_neighbor(edge[1])  # add end node to succ of start node

    # sort by number of neighbors! the satisfies the least constraining variable heuristic
    for node in nodes:
        node_map[node].neighbors.sort(key=lambda x: len(node_map[x].neighbors))
    return node_map


def dfs_coloring(G, start, colors):
    adj_colors = [G[i].color for i in G[start].neighbors]
    for c in colors:
        if c not in adj_colors:
            G[start].color = c
            break
    if G[start].color == 0:
        return False
    
    for neighbor in G[start].neighbors:
        if G[neighbor].color == 0:
            if not dfs_coloring(G, neighbor, colors):
                return False
    return True

def file_io(file):
    colors = None
    nodes = set()
    edges = set()
    with open(file, "r") as txt_file:
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
    return nodes, edges, colors

def main(inp):
    print(inp)
    nodes, edges, colors = file_io("data/test1.txt")
    G = add_nodes_edges(nodes, edges)

    if dfs_coloring(G, min(G.keys()), list(range(1, colors+1))):
        print("There is a {} coloring".format(colors))
    else:
        print("There is not a {} coloring".format(colors))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please enter an input file")
    else:
        if not os.path.isfile(sys.argv[1]):
            print("please enter a valid file")
        else: main(sys.argv[1])