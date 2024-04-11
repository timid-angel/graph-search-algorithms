from adjacencyList import Graph, Node

# Create a graph
graph = Graph()

# Create nodes
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

# Add edges
graph.addEdge(a, b, 1)
graph.addEdge(c, d, 2)
graph.addEdge(c, a, 3)
graph.addEdge(d, e, 6)
graph.addEdge(e, d, 2)
graph.addEdge(d, e, 9)
graph.addEdge(f, g, 2)
graph.addEdge(b, a, 4)  
graph.addEdge(d, f, 3)


print("Initial graph:")
print(graph)


graph.removeEdge(a, b, 1)
graph.removeEdge(a, b, 1)  
graph.removeEdge(f, g, 2)


print("\nGraph after removing edges:")
print(graph)


graph.remove_vertex(c)  


print("\nGraph after removing vertex 'c':")
print(graph)


print("\nChecking for existence of edges:")
print("Edge (a, b) exists?--", graph.has_edge(a, b))  
print("Edge (d, e) exists?--", graph.has_edge(d, e))  
print("Edge (f, g) exists?--", graph.has_edge(f, g))  


print("\nFinding neighbors of vertices:")
print("Neighbors of 'a':", graph.neighbors(a))  
print("Neighbors of 'b':", graph.neighbors(b)) 
print("Neighbors of 'f':", graph.neighbors(f)) 
