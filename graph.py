class Node:
    def __init__(self, val):
        self.val = val
        self.nbs = []

class Graph:
    def __init__(self):
        self.nodes = []
    

    def addEdge(self, source: Node, destination: Node, cost: int):
        found_source = False
        found_destination = False
        for i in range(len(self.nodes)):
            if not found_source and self.nodes[i].val == source.val:
                found_source = self.nodes[i]
            
            if not found_destination and self.nodes[i].val == destination.val:
                found_destination = self.nodes[i]
                
        if not found_source:
            self.nodes.append(source)
            found_source = self.nodes[-1]
        
        if not found_destination:
            self.nodes.append(destination)
            found_destination = self.nodes[-1]
        
        found_source.nbs.append((found_destination, cost))
    

    def removeEdge(self, source: Node, destination: Node, cost: int):
        found = False
        for i in range(len(self.nodes)):
            if self.nodes[i].val == source.val:
                found = self.nodes[i]
                break
        
        if not found:
            return

        for j in range(len(found.nbs)):
            if found.nbs[j] == (destination, cost):
                return found.nbs.pop(j)
        

    def __str__(self):
        s = "\n"
        for n in self.nodes:
            nodes = "[ "
            for nb in n.nbs:
                nodes += f"({nb[0].val}, {nb[1]}) "
            nodes += "]"
            s += f"{n.val} : {nodes}\n"

        return s

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
