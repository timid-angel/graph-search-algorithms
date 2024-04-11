from graph import Graph, Node

from search_algorithms.bfs import breadthFirstSearch
from search_algorithms.dfs import depthFirstSearch
from search_algorithms.ucs import uniformCostSearch
from search_algorithms.greedy import greedySearch
from search_algorithms.bidirectional import bidirectionalSearch
from search_algorithms.iterative_deepening import iterativeDeepening
from search_algorithms.a_star import aStarSearch
from centrality.degree import degreeCentrality
from centrality.closeness import closenessCentrality
from centrality.betweenness import betweennessCentrality
from centrality.katz import katzCentrality

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
graph.addEdge(e, a, 1)


print(katzCentrality(graph))