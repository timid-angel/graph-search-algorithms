import math
from queue import PriorityQueue

from load_graph_from_file import coords
from graph import Node

def heuristic(node, destination):
    x1, y1 = coords[node]
    x2, y2 = coords[destination]
    return math.floor((x2 - x1) ** 2 + (y2 - y1) ** 2)


def aStarSearch(start: Node, destination: Node):

    queue = PriorityQueue()
    queue.put((heuristic(start, destination), start, 0))
    visited = set([start])
    path = {start: None}
    goal = None
    
    while True:
        if not queue:
            raise ValueError('Not found')
        
        _, curr, r_cost = queue.get()
        if curr == destination:
            goal = curr
            break
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                queue.put((heuristic(nx, destination) + r_cost + cost, nx, r_cost + cost))
                path[nx] = curr
    
    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    arr.pop()
    return arr[::-1]
