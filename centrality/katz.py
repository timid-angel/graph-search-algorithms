from collections import deque

def katzCentrality(graph):
    alpha = 0.5
    arr = []
    for n in graph.nodes:
        arr.append((n, alphaBFS(n, alpha)))
    
    return sorted(arr, key= lambda x: x[1], reverse=True)


def alphaBFS(node, alpha):
    queue = deque([node])
    visited = set([node])
    lvl = 0
    score = 0
    while queue:
        for _ in range(len(queue)):
            if lvl != 0:
                score += alpha ** lvl

            curr = queue.popleft()
            for nb, cost in curr.nbs:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        
        lvl += 1

    return score