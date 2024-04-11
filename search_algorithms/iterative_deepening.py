def iterativeDeepening(source, destination, maxDepth=20):
    for i in range(maxDepth + 1):
        if dfsLimited(source, destination, i):
            return True
    
    return False


def dfsLimited(source, destination, depth):

    stack = [(source, depth)]
    visited = set([source])

    while stack:
        c, d = stack.pop()
        if c == destination:
            return True
        if d == 0:
            continue

        for nb in c.nbs:
            nx, _ = nb
            if nx not in visited:
                visited.add(nx)
                stack.append((nx, d - 1))
    
    return False