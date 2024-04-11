def getCount(st):
    stack = [st]
    visited = set([st])

    while stack:
        c = stack.pop()
        for nb, _ in c.nbs:
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)
    
    return len(visited)
