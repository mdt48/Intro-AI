# CSP Graph Coloring

## Documentation

- **To Run**

    - ```python csp.py <path to data file>```


## Report
In this project, I designed an algorithm to solve the k graph coloring algorithm. This is a form of a Constraint Satisfaction Problem, the constraints in this case is that no two adjacent nodes can share a color, and that we must only use k colors. To do this, I initially used a modified DFS to travel to each node and assign a color. If the color was invalid for a given node, then the color is left unset and we backtrack, trying to color the other nodes. If any nodes is left uncolored, then there is not a valid k coloring. 

This solution can be improved using the least constraining value heuristic and constraint propagation. The least constraining variable heuristic means that we must choose a value that rules out the smallest number of other values connected to the current value. In the graph coloring problem this means that at any node, we first explore the neighbor of said node that has the lowest number of neighbors. Using this least constraining variable heuristic allows for the algorithm to be more flexible and find a proper coloring if one exists. 

Constraint propagation is helpful in terms of optimizing the efficiency of the algorithm. This can be applied to graph coloring by removing unavailable colors from the pallette available to the node. This means we do not have to check certain colors and eliminate whole subtrees of searching.