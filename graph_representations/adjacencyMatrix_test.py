from adjacencyMatrix import GraphAdjacencyMatrix


graph = GraphAdjacencyMatrix(5)

graph.add_vertex()
graph.add_vertex()


graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)


print("Edge Exists?--", graph.has_edge(0, 1))
print("Edge Exists?--", graph.has_edge(1, 3))


print("Neighbors of vertex:", graph.neighbors(2))


graph.remove_edge(0, 1)
graph.remove_edge(2, 3)


print("Does edge exist between vertex 0 and 1 after removal?", graph.has_edge(0, 1))
print("Does edge exist between vertex 2 and 3 after removal?", graph.has_edge(2, 3))


graph.remove_vertex(0)
graph.remove_vertex(1)


print("Adjacency matrix after vertex removal:")
for row in graph.adj_matrix:
    print(row)
