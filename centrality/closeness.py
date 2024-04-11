from queue import PriorityQueue
from random import random
from graph import Node

def closenessCentrality(graph):
    arr = []
    for i in range(len(graph.nodes)):
        total = 0 
        for j in range(len(graph.nodes)):
            total += getCostUCS(graph.nodes[i], graph.nodes[j])
        
        val = 1 / total if total != 0 else float('inf')
        arr.append((graph.nodes[i], val))
    
    return sorted(arr, key= lambda x: x[1], reverse=True)
            

def getCostUCS(start: Node, destination: Node):
    queue = PriorityQueue()
    queue.put((0, random(), start))
    visited = set([start])
    
    while queue:
        if queue.empty():
            break

        r_cost, _, curr = queue.get()
        if curr == destination:
            return r_cost
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                queue.put((r_cost + cost, random(), nx))

    return 0