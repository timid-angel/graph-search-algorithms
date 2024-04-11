from collections import deque
from graph import Node

def breadthFirstSearch(start: Node, destination: Node):

    queue = deque([start])
    visited = set([start])
    path = {start: None}
    goal = None
    
    while True:
        if not queue:
            raise ValueError('Not found')
        
        curr = queue.popleft()
        if curr == destination:
            goal = curr
            break
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                queue.append(nx)
                path[nx] = curr
    
    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    arr.pop()
    return arr[::-1]
