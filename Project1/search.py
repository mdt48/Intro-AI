import math
import heapq

def find_min(d, check):
    u = max(d, key=d.get); m = d[u]
    for k in d.keys():
        if d[k] < m and k not in check:
            m = d[k]
            u = k
    return u

def dijkstra(adj_list, S, E, node_to_block):
    print("Dijstra's\n---------")
    n_iters = 0
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
        n_iters += 1
        u = find_min(dist, sp)

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

    print("Nodes Visited: ", len(sp))
    print("N_iters={}".format(n_iters))

    print("Path:", seq)
    print("Length: {}".format(dist[E]))
    print("\n----------\n")

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
    print("A*\n---------")
    # path to extend
    # f(n) = g(n) + h(n)
    # g(n)  path from start to n
    # h(n) = heuristic

    prev = {}

    heap = []
    closed = set()

    f, g = {i:float('inf') for i in range(0, len(adj_list.keys()))}, {i:float('inf') for i in range(0, len(adj_list.keys()))}
    f[S] = heuristic(node_to_block[S], node_to_block[E])
    g[S] = 0

    heap.append((f[S], S))
    heapq.heapify(heap)    

    n_iters = 0
    while not heap.count == 0:
        n_iters += 1
        _, u = heapq.heappop(heap)
        heapq.heappush(heap, (_, u))

        if u == E:
            break
        closed.add(u)

        for successor in adj_list[u]:
            tentative = g[u] + successor[1]
            if (tentative + heuristic(node_to_block[successor[0]], node_to_block[E])) < f[successor[0]] and successor[0] not in closed:
                prev[successor[0]] = u
                g[successor[0]] = tentative
                f[successor[0]] = g[successor[0]] + heuristic(node_to_block[successor[0]], node_to_block[E])
                if successor not in heap:
                    heapq.heappush(heap, (f[successor[0]], successor[0]))
                    
        heapq.heappop(heap)


    # printing
    path = []
    u = E
    while u != S:
        path.insert(0,u)
        u = prev[u]
    path.insert(0, S)    
    print("Nodes Visited: ", len(closed))
    print("N_iters={}".format(n_iters))

    print("Path:", path)
    print("Length: {}\n\n".format(f[E]))

    

            
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
a_star(adj_list, S, E, l2)