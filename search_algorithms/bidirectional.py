from collections import deque
from graph import Node

def bidirectionalSearch(start: Node, destination: Node):

    s_queue = deque([start])
    d_queue = deque([destination])
    s_visited = set([start])
    d_visited = set([destination])
    sPath = {start: None}
    dPath = {destination: None}
    goal = None
    
    while True:
        if not s_queue and not d_queue:
            raise ValueError('Not found')
        
        if s_queue:
            cs = s_queue.popleft()
            if cs in d_visited:
                goal = cs
                break
                
            for nb in cs.nbs:
                nx, _ = nb
                if nx not in s_visited:
                    s_visited.add(nx)
                    s_queue.append(nx)
                    sPath[nx] = cs
        
        if d_queue:
            cd = d_queue.popleft()
            if cd in s_visited:
                goal = cd
                break
            
            for nb in cd.nbs:
                nx, _ = nb
                if nx not in d_visited:
                    d_visited.add(nx)
                    d_queue.append(nx)
                    dPath[nx] = cd
    
    curr = goal
    sArr = []
    while curr:
        if curr is None: break
        sArr.append(curr.val)
        curr = sPath[curr]
    
    dArr = []
    while goal:
        if goal is None: break
        dArr.append(goal.val)
        goal = dPath[goal]
    
    dArr.pop()
    
    return sArr[::-1] + dArr
