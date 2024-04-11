from graph import Node

def depthFirstSearch(start: Node, destination: Node):

    stack = [start]
    visited = set([start])
    path = {start: None}
    goal = None
    
    while True:
        if not stack:
            raise ValueError('Not found')
        
        curr = stack.pop()
        if curr == destination:
            goal = curr
            break
            
        for nb in curr.nbs:
            nx, cost = nb
            if nx not in visited:
                visited.add(nx)
                stack.append(nx)
                path[nx] = curr
    
    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    arr.pop()
    return arr[::-1]
