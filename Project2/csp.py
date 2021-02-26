
import sys, os
class Node:
    def __init__(self) -> None:
        self.neighbors = []
        self.color = 0
        self.avail_colors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)


def add_nodes_edges(nodes, edges, colors):
    graph = {}
    for node in nodes:
        graph[node] = Node()
        graph[node].avail_colors = list(range(1, colors+1))

    for edge in edges:
        graph[edge[1]].add_neighbor(edge[0])  
        graph[edge[0]].add_neighbor(edge[1])  

    # sort by number of neighbors! the satisfies the least constraining variable heuristic
    for node in nodes:
        graph[node].neighbors.sort(key=lambda x: len(graph[x].neighbors))
    return graph


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
            # remove the value to be arc consistent leads to fewer sub calls
            G[neighbor].avail_colors.remove(c)
            if not dfs_coloring(G, neighbor, colors):
                # add color back in if the c color for node start fails
                # this is because the child node can now be colored c
                G[neighbor].avail_colors.append(c)
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
    nodes, edges, colors = file_io(inp)
    G = add_nodes_edges(nodes, edges, colors)

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