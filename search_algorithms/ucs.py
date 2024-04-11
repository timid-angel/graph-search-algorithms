from queue import PriorityQueue
from graph import Node

def uniformCostSearch(start: Node, destination: Node):

    queue = PriorityQueue()
    queue.put((0, start))
    visited = set([start])
    path = {start: None}
    goal = None
    
    while True:
        if not queue:
            raise ValueError('Not found')
        
        r_cost, curr = queue.get()
        if curr == destination:
            goal = curr
            break
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                queue.put((r_cost + cost, nx))
                path[nx] = curr
    
    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    arr.pop()
    return arr[::-1]
