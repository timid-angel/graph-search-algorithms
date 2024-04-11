import math
from queue import PriorityQueue
from random import random

from graph import Node

def heuristic(node, destination, coords):
    x1, y1 = coords[node]
    x2, y2 = coords[destination]
    return math.floor((x2 - x1) ** 2 + (y2 - y1) ** 2)


def aStarSearch(start: Node, destination: Node, coords):

    queue = PriorityQueue()
    queue.put((0, random(), start, 0))
    visited = set([start])
    path = {start: None}
    goal = None
    
    while True:
        if not queue:
            raise ValueError('Not found')
        
        _, _, curr, r_cost = queue.get()
        if curr == destination:
            goal = curr
            break
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                h = heuristic(nx, destination, coords)
                queue.put((h + r_cost + cost, random(), nx, r_cost + cost))
                path[nx] = curr
    
    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    return arr[::-1]
