class GraphAdjacencyMatrix:
    def __init__(self, vertex_count):
        """
        Time complexity: O(V^2) where V is the number of vertices
        Space complexity: O(V^2)
        """
        if vertex_count < 0:
            raise ValueError("Vertex count must be non-negative")
        self.vertex_count = vertex_count
        self.adj_matrix = [[0] * vertex_count for _ in range(vertex_count)]

    def add_vertex(self):
        """
        Time complexity: O(V^2) where V is the number of vertices
       
        """
        self.vertex_count += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.vertex_count)

    def add_edge(self, source, destination):
        """
        Time complexity: O(1)
       
        """
        if not (0 <= source < self.vertex_count and 0 <= destination < self.vertex_count):
            raise ValueError("Invalid vertex indices")
        self.adj_matrix[source][destination] = 1

    def remove_vertex(self, vertex):
        """
        Time complexity: O(V^2) where V is the number of vertices
    
        """
        if not (0 <= vertex < self.vertex_count):
            raise ValueError("Invalid vertex index")
        del self.adj_matrix[vertex]
        self.vertex_count -= 1
        for row in self.adj_matrix:
            del row[vertex]

    def remove_edge(self, source, destination):
        """
        Time complexity: O(1)
      
        """
        if not (0 <= source < self.vertex_count and 0 <= destination < self.vertex_count):
            raise ValueError("Invalid vertex indices")
        self.adj_matrix[source][destination] = 0

    def has_edge(self, source, destination):
        """
        Time complexity: O(1)
    
        """
        if not (0 <= source < self.vertex_count and 0 <= destination < self.vertex_count):
            raise ValueError("Invalid vertex indices")
        return self.adj_matrix[source][destination] != 0

    def neighbors(self, vertex):
        """
        Time complexity: O(V) where V is the number of vertices
     
        """
        if not (0 <= vertex < self.vertex_count):
            raise ValueError("Invalid vertex index")
        return [i for i in range(self.vertex_count) if self.adj_matrix[vertex][i] != 0]
