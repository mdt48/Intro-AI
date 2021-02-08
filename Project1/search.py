import operator
def dijkstra(adj_list, S, E, node_to_block):
    # all nodes unvisited
    Q = {i for i in range(0, 100)}

    #visited list
    sp = []

    # distance and prev dicts
    dist = {}
    prev = {}

    u = None
    for vertex in adj_list.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None

    dist[S] = 0

    while Q:
        u = max(dist, key=dist.get); m = dist[u]
        for k in dist.keys():
            if dist[k] < m and k not in sp:
                m = dist[k]
                u = k

        print(sp)
        sp.append(u)
        Q.remove(u)

        if u == E:
            break

        for edge in adj_list[u]:
            alt = dist[u] + edge[1]
            if alt < dist[edge[0]]:
                dist[edge[0]] = alt
                prev[edge[0]] = u
    
    # print the shortest path
    seq = []
    if prev[u] != None or u == S:
        while u != None:
            seq.insert(0, u)
            u = prev[u]
    print("Nodes Visited: ", sp)
    print("Path:", seq)
    print("Length: {}".format(dist[E]))
            
file = "./p1_graph.txt"
section = 0 # 0: nodes, 1: edges, 2: SE
adj_list = {}
node_to_block = {}
S, E = None, None 


# Read in data
with open(file, "r") as graph:
    for f in graph:
        if f.startswith("#"): continue 
        if f == "\n": 
            section += 1
            continue

        data = f.split(",")

        if section == 0: 
            node_to_block[int(data[0])] = int(data[1])
            adj_list[int(data[0])] = []

        if section == 1: 
            # undirected, add both ways
            adj_list[int(data[0])].append( (int(data[1]), int(data[2])) )
            adj_list[int(data[1])].append( (int(data[0]), int(data[2])) )

        if section == 2:
            if data[0] == "S":
                S = int(data[1])
            else:
                E = int(data[1])


dijkstra(adj_list, S, E, node_to_block)
