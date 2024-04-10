from graph import Graph, Node

# testing graph class
graph = Graph()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

graph.addEdge(a, b, 1)
graph.addEdge(c, d, 2)
graph.addEdge(c, a, 3)
graph.addEdge(d, e, 6)
graph.addEdge(e, d, 2)
graph.addEdge(d, e, 9)
graph.addEdge(f, g, 2)

print(graph)

graph.removeEdge(a, b, 1)
graph.removeEdge(a, b, 1)
graph.removeEdge(f, g, 2)
graph.removeEdge(d, e, 2)
graph.removeEdge(d, e, 6)
graph.removeEdge(e, d, 2)

print(graph)
