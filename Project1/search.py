import math
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


def l1(s, e):
    # Manhattan distance

    start_row = s // 10
    end_row = e // 10

    start_col = s % 10
    end_col = e % 10

    return abs(start_row - end_row) + abs(start_col - end_col)
    

def l2(s, e):
    # Euclidean distance

    start_row = s / 10
    end_row = e / 10

    start_col = s % 10
    end_col = e % 10

    return math.sqrt ( ((start_row-end_row)**2) - ((start_row - end_row)**2) )

def a_star(adj_list, S, E, heuristic):
    # path to extend
    # f(n) = g(n) + h(n)
    # g(n)  path from start to n
    # h(n) = heuristic
    # dist[n] = g(n)
    # f_distance = f(n)

    op =  [S]
    prev = {i for i in range(0, 100)}

    f = {i:float('inf') for i in range(0,100)}
    f[S] = 0

    g = {i:float('inf') for i in range(0,100)}
    g[S] = 0
    
    h = {}
    
    while op:
        curr = min(f, key=f.get)

        if curr == E:
            break

        op.remove(curr)

        for edge in adj_list[curr]:
            t = g[curr] + edge[1]

            if t < g[curr]:
                prev[edge[0]] = curr
                g[edge[0]] = t
                f[edge[0]] = g[edge[0]] + heuristic(edge[0])

                if edge[0] not in op:
                    op.append(edge[0])




    # printing
    path = []
    u = E
    while u != None:
        path.insert(0)
        u = prev[u]
    

            
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


# dijkstra(adj_list, S, E, node_to_block)
a_star(adj_list, S, E, l1)