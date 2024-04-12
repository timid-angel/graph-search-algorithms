import math
import time
from random import random, choice
from graph import Graph, Node

from search_algorithms.bfs import breadthFirstSearch
from search_algorithms.dfs import depthFirstSearch
from search_algorithms.ucs import uniformCostSearch
from search_algorithms.greedy import greedySearch
from search_algorithms.bidirectional import bidirectionalSearch
from search_algorithms.iterative_deepening import iterativeDeepening
from search_algorithms.a_star import aStarSearch

def getDistance(n1, n2):
    return math.sqrt(math.floor((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2))


# generates a graph given the number of nodes and the probability of edges
def generateGraph(n, p):
    graph = Graph()
    coords = {}
    for i in range(n):
        x, y = math.floor((random() * 100)), math.floor((random() * 100))
        node = Node(i)
        graph.addNode(node)
        coords[node] = (x, y)

    for i in range(n):
        for j in range(n):
            if i != j and random() < p:
                n1 = graph.nodes[i]
                n2 = graph.nodes[j]
                graph.addEdge(n1, n2, getDistance(n1, n2))
    
    return graph, coords


# tests the provided graph with the functions provided
# the number of tests to be conducted are provided through test_count
# returns an array containing the average time and average length path for each function
def testWithGraph(graph, functions, coords, test_count):

    res = [(0, 0) for _ in range(len(functions))] 
    tests = [0] * len(functions)
    i = 0
    
    while i < test_count:
        try:
            s, d = choice(graph.nodes), choice(graph.nodes)
            for j, search in enumerate(functions):
                
                st = time.time()
                path = None
                if j < len(functions) - 1: 
                    path = search(s, d)
                else:
                    path = search(s, d, coords)
                en = time.time()
                res[j] = (res[j][0] + (en - st), res[j][1] + len(path))
                tests[j] += 1

            i += 1
            
        except ValueError:
            continue
        
    for i in range(len(tests)):
        res[i] = (res[i][0] / test_count, res[i][1] / test_count)
    
    return res


functions = [depthFirstSearch, breadthFirstSearch, uniformCostSearch, greedySearch, bidirectionalSearch, iterativeDeepening, aStarSearch]
node_counts = [10, 20, 30, 40]
edge_possibilites = [0.2, 0.4, 0.6, 0.8]
test_count = 6

variations = []
for c in node_counts:
    for p in edge_possibilites:
        variations.append((c, p))

results = []
for c, p in variations:
    graph, coords = generateGraph(c, p)
    results.append(testWithGraph(graph, functions, coords, test_count)) 
