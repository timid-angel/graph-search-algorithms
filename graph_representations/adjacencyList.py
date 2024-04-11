class Node:
    def __init__(self, val):
        self.val = val
        self.nbs = []  # Space complexity: O(1)

class Graph:
    def __init__(self):
        self.nodes = []  # Space complexity: O(1)
    
    # Time complexity: O(V), where V is the number of vertices
    def addEdge(self, source: Node, destination: Node, cost: int):
        found_source = False
        found_destination = False
        for i in range(len(self.nodes)):  # Iterates over all nodes once
            if not found_source and self.nodes[i].val == source.val:
                found_source = self.nodes[i]
            
            if not found_destination and self.nodes[i].val == destination.val:
                found_destination = self.nodes[i]
                
        if not found_source:
            self.nodes.append(source)  # Adds a new node if not found
            found_source = self.nodes[-1]
        
        if not found_destination:
            self.nodes.append(destination)  # Adds a new node if not found
            found_destination = self.nodes[-1]
        
        found_source.nbs.append((found_destination, cost))  # Appends neighbor to source node

    # Time complexity: O(V), where V is the number of vertices
    # Space complexity: O(1)
    def removeEdge(self, source: Node, destination: Node, cost: int):
        found = False
        for i in range(len(self.nodes)):  # Iterates over all nodes once
            if self.nodes[i].val == source.val:
                found = self.nodes[i]
                break
        
        if not found:
            return

        for j in range(len(found.nbs)):  # Iterates over neighbors of source node
            if found.nbs[j] == (destination, cost):
                return found.nbs.pop(j)  # Removes edge if found

    # Time complexity: O(V), where V is the number of vertices
    # Space complexity: O(1)
    def remove_vertex(self, vertex):
        found = False
        for i in range(len(self.nodes)):
            if self.nodes[i].val == vertex.val:
                found = self.nodes[i]
                break

        if not found:
            return

        self.nodes.remove(found)

        # Remove edges related to the vertex
        for node in self.nodes:
            node.nbs = [(n, w) for n, w in node.nbs if n != found]

    # Time complexity: O(V), where V is the number of vertices
    # Space complexity: O(1)
    def remove_edge(self, source, destination):
        if not (0 <= source < self.vertex_count and 0 <= destination < self.vertex_count):
            raise ValueError("Invalid vertex indices")
        self.adj_matrix[source][destination] = 0

    # Time complexity: O(V), where V is the number of vertices
    # Space complexity: O(1)
    def has_edge(self, source, destination):
        for node in self.nodes:
            if node.val == source.val:
                for n, _ in node.nbs:
                    if n.val == destination.val:
                        return True
        return False
    # Time complexity: O(V), where V is the number of vertices
    # Space complexity: O(1)
    def neighbors(self, vertex):
        for node in self.nodes:
            if node.val == vertex.val:
                return [n.val for n, _ in node.nbs]
        return []

    # Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
    # Space complexity: O(V + E)
    def __str__(self):
        s = "\n"
        for n in self.nodes:  # Iterates over all nodes once
            nodes = "[ "
            for nb in n.nbs:  # Iterates over neighbors of each node
                nodes += f"({nb[0].val}, {nb[1]}) "
            nodes += "]"
            s += f"{n.val} : {nodes}\n"

        return s
