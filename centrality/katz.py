"""
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
"""

import numpy as np

def katzCentrality(graph):
    mat = [[0] * len(graph.nodes) for _ in range(len(graph.nodes))]
    for j, n in enumerate(graph.nodes):
        for ed, cost in n.nbs:
            idx = 0
            for i, node in enumerate(graph.nodes):
                if node == ed:
                    idx = i
                    break
            
            mat[j][idx] = cost

    alpha = 1

    node_count = len(mat)
    alt = np.eye(node_count)
    lambdas, eigen_vectors = np.linalg.eig(alt - alpha * mat)
    max_eigen = max(abs(lambdas))
    sum_across = eigen_vectors.sum(axis=0)

    results = np.linalg.solve(max_eigen * np.eye(node_count) - lambdas, sum_across)

    res = []
    for i in range(len(results)):
        res.append((graph.nodes[i], abs(results[i].real)))

    return sorted(res, key= lambda x: x[1], reverse=True)