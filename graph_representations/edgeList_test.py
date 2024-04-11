from edgeList import GraphEdgeList

# Create a graph
graph = GraphEdgeList()

# Insert vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

#  vertices after insertion
print("Vertices after insertion:", graph.vertices)

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')

# edges after addition
print("Edges after addition:")
for edge in graph.edges:
    print(edge)

# Checks existence of edges
print("Existence of edges:")
print("'A'-'B' exists:", graph.has_edge('A', 'B'))
print("'B'-'C' exists:", graph.has_edge('B', 'C'))
print("'C'-'A' exists:", graph.has_edge('C', 'A'))

# Checks neighbors
print("Neighbors:")
print("Neighbors of 'A':", graph.neighbors('A'))
print("Neighbors of 'B':", graph.neighbors('B'))
print("Neighbors of 'C':", graph.neighbors('C'))

# Remove edges
graph.remove_edge('A', 'B')
print("After removing 'A'-'B':")
print("'A'-'B' exists:", graph.has_edge('A', 'B'))

# Remove vertices
graph.remove_vertex('C')
print("After removing vertex 'C':")
print("Vertices:", graph.vertices)
print("Edges:")
for edge in graph.edges:
    print(edge)
print("'B' neighbors:", graph.neighbors('B'))
