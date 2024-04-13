import numpy as np

def pageRankCentrality(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):

    # Construct the transition matrix
    num_nodes = len(graph.nodes)
    transition_matrix = np.zeros((num_nodes, num_nodes))
    for j, node in enumerate(graph.nodes):
        if node.nbs:
            for nb, cost in node.nbs:
                i = graph.nodes.index(nb)
                transition_matrix[i, j] = 1 / len(node.nbs)

    # Initialize PageRank vector
    pagerank_vector = np.ones(num_nodes) / num_nodes

    # Iteratively update PageRank vector
    for _ in range(max_iterations):
        new_pagerank_vector = (1 - damping_factor) / num_nodes + damping_factor * transition_matrix.dot(pagerank_vector)
        if np.linalg.norm(new_pagerank_vector - pagerank_vector, ord=1) < tolerance:
            break
        pagerank_vector = new_pagerank_vector

    # Sort nodes by PageRank scores
    pagerank_scores = list(zip(graph.nodes, pagerank_vector))
    pagerank_scores.sort(key=lambda x: x[1], reverse=True)
    
    return pagerank_scores
