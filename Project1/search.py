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
    visited = []
    
    # distance and prev dicts
    dist = {}
    prev = {}

    

    current = None
    for vertex in adj_list.keys():
        dist[vertex] = float('inf')
        prev[vertex] = None

    dist[S] = 0

    while Q:
        n_iters += 1
        current = find_min(dist, visited)
        # current = heapq.heappop(queue)

        visited.append(current)
        Q.remove(current)

        if current == E:
            break

        for edge in adj_list[current]:
            alt = dist[current] + edge[1]
            if alt < dist[edge[0]]:
                dist[edge[0]] = alt
                prev[edge[0]] = current
    
    # print the shortest path
    seq = []
    if prev[current] != None or current == S:
        while current != None:
            seq.insert(0, current)
            current = prev[current]

    print("Nodes Visited: ", len(visited))
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

    return math.sqrt( ((start_row-end_row)**2) + ((start_col-end_col)**2) )


def a_star(adj_list, S, E, heuristic):
    print("A*\n---------")
    # path to extend
    # f(n) = g(n) + h(n)
    # g(n)  path from start to n
    # h(n) = heuristic

    # the previous node for each node, used to rebuild path
    prev = {}

    # prio queue/heap queue
    heap = []

    # already explored nodes
    closed = []

    # initialize the initial f,g,h vals for each node
    f, g, h= {i:float('inf') for i in range(0, len(adj_list.keys()))}, {i:float('inf') for i in range(0, len(adj_list.keys()))},{i:0 for i in range(0, len(adj_list.keys()))}
    f[S] = heuristic(node_to_block[S], node_to_block[E])
    g[S] = 0

    # use f[S] as key
    heap.append((f[S], S))
    heapq.heapify(heap)    

    n_iters = 0
    while not heap.count == 0:
        n_iters += 1
        
        # extract the minimum 
        _, current = heapq.heappop(heap)
        closed.append(current)


        # if we have found the target node
        if current == E:
            break
        
        # iterate over children of current
        for child in adj_list[current]:
            # see if the tentative(new) score is better than what was already computed
            # if it is, update the values, and add to queue
            tentative = g[current] + child[1] 
            test = heuristic(node_to_block[child[0]], node_to_block[E])
            if tentative + test < g[child[0]]:
                # set g and compute h for child
                g[child[0]] = tentative
                h[child[0]] = heuristic(node_to_block[child[0]], node_to_block[E])

                # previous is the current node
                prev[child[0]] = current

                # dont add to queue if its already explored
                if child[0] in closed: continue

                # compute new f
                f[child[0]] = g[child[0]] + h[child[0]]

                # update values in queue already
                fl = False
                for he in heap:
                    if he[1] == child[0]:
                        heap.remove(he)
                        heapq.heappush(heap, (f[he[1]], he[1]))
                        prev[he[1]] = current
                        fl = True
                
                # dont add it to queue if you just updated it
                if fl: continue

                heapq.heappush(heap, (f[child[0]], child[0]))
            
            

            
            
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
a_star(adj_list, S, E, l1)