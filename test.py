from graph import Graph, Node

from search_algorithms.bfs import breadthFirstSearch
from search_algorithms.dfs import depthFirstSearch
from search_algorithms.ucs import uniformCostSearch
from search_algorithms.greedy import greedySearch
from search_algorithms.bidirectional import bidirectionalSearch
from search_algorithms.iterative_deepening import iterativeDeepening
from search_algorithms.a_star import aStarSearch

graph = Graph()
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

graph.addEdge(a, b, 3)
graph.addEdge(b, c, 2)
graph.addEdge(c, d, 2)
graph.addEdge(d, e, 5)
graph.addEdge(a, e, 1)


print(bidirectionalSearch(a, e))