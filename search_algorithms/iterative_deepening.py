def iterativeDeepening(source, destination, maxDepth=20):
    for i in range(maxDepth + 1):
        res = dfsLimited(source, destination, i)
        if res:
            return res
    
    raise ValueError('Not Found')


def dfsLimited(source, destination, depth):

    stack = [(source, depth)]
    visited = set([source])
    path = {source : None}
    goal = None

    while stack:
        c, d = stack.pop()
        if c == destination:
            goal = c
            break
        if d == 0:
            continue

        for nb in c.nbs:
            nx, _ = nb
            if nx not in visited:
                visited.add(nx)
                stack.append((nx, d - 1))
                path[nx] = c
    
    if not goal:
        return False

    arr = []
    while goal:
        if goal is None: break
        arr.append(goal.val)
        goal = path[goal]
    
    return arr[::-1]