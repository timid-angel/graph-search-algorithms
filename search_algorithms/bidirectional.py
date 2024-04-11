from collections import deque
from graph import Node

def bidirectionalSearch(start: Node, destination: Node):

    s_queue = deque([start])
    d_queue = deque([destination])
    s_visited = set([start])
    d_visited = set([destination])
    # path = {start: None}
    # goal = None
    
    while True:
        if not s_queue and not d_queue:
            raise ValueError('Not found')
        
        if s_queue:
            cs = s_queue.popleft()
            if cs in d_visited:
                break
                
            for nb in cs.nbs:
                nx, _ = nb
                if nx not in s_visited:
                    s_visited.add(nx)
                    s_queue.append(nx)
        
        if d_queue:
            cd = d_queue.popleft()
            if cd in s_visited:
                break
            
            for nb in cd.nbs:
                nx, _ = nb
                if nx not in d_visited:
                    d_visited.add(nx)
                    d_queue.append(nx)
    
    # arr = []
    # while goal:
    #     if goal is None: break
    #     arr.append(goal.val)
    #     goal = path[goal]
    
    # arr.pop()
    # return arr[::-1]
