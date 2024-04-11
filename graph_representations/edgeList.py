class GraphEdgeList:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if vertex in self.vertices:
            raise ValueError("Vertex already exists")
        self.vertices.add(vertex)

    def add_edge(self, source, destination):
        """
        Adds an edge between two vertices.
        
        Time complexity: O(1)
        Space complexity: O(1)
        """
        if source not in self.vertices or destination not in self.vertices:
            raise ValueError("Vertices must exist in the graph")
        self.edges.append((source, destination))

    def remove_vertex(self, vertex):
        """
        Removes a vertex and all incident edges from the graph.
        
        Time complexity: O(E) where E is the number of edges
        Space complexity: O(E)
        """
        if vertex not in self.vertices:
            raise ValueError("Vertex does not exist")
        self.vertices.remove(vertex)
        self.edges = [(src, dest) for src, dest in self.edges if src != vertex and dest != vertex]

    def remove_edge(self, source, destination):
        """
        Removes an edge between two vertices.
        
        Time complexity: O(E) where E is the number of edges
        Space complexity: O(1)
        """
        if (source, destination) not in self.edges:
            raise ValueError("Edge does not exist")
        self.edges = [(src, dest) for src, dest in self.edges if (src, dest) != (source, destination)]

    def has_edge(self, source, destination):
        """
        Checks if an edge exists between two vertices.
        
        Time complexity: O(E) where E is the number of edges
        Space complexity: O(1)
        """
        return (source, destination) in self.edges

    def neighbors(self, vertex):
        """
        Finds all neighbors of a vertex.
        
        Time complexity: O(E) where E is the number of edges
        Space complexity: O(V) where V is the number of vertices
        """
        if vertex not in self.vertices:
            raise ValueError("Vertex does not exist")
        return [dest for src, dest in self.edges if src == vertex]
