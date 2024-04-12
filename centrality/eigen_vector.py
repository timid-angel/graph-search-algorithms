import numpy as np

def eigenVectorCentrality(graph):

    mat = [[0] * len(graph.nodes) for _ in range(len(graph.nodes))]
    for j, n in enumerate(graph.nodes):
        for ed, cost in n.nbs:
            idx = 0
            for i, node in enumerate(graph.nodes):
                if node == ed:
                    idx = i
                    break
            
            mat[j][idx] = cost
    
    lambdas, eigen_vectors = np.linalg.eig(mat) # solve for the eigen values and eigen vectors
    lambdas = np.absolute(lambdas) # make each eigenvalue positive
    max_i = np.argmax(lambdas)
    vectors = eigen_vectors[:, max_i]
    vectors = vectors / np.sum(vectors)

    res = []
    for i in range(len(vectors)):
        res.append((graph.nodes[i], abs(vectors[i].real)))

    return sorted(res, key= lambda x: x[1], reverse=True)