import time
import random

from search_algorithms.bfs import breadthFirstSearch
from search_algorithms.dfs import depthFirstSearch
from search_algorithms.ucs import uniformCostSearch
from search_algorithms.greedy import greedySearch
from search_algorithms.bidirectional import bidirectionalSearch
from search_algorithms.iterative_deepening import iterativeDeepening
from search_algorithms.a_star import aStarSearch
from load_graph_from_file import coords
from load_graph_from_file import cities
from load_graph_from_file import nodes

dfs_times = []
dfs_path = []
for i in range(10):
    sdfs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    
    # print(f'Running DFS - S:{s} D:{d}')
    path = depthFirstSearch(nodes[s], nodes[d])

    edfs = time.time()
    total = edfs - sdfs
    dfs_times.append(total)
    dfs_path.append(len(path))

bfs_times = []
bfs_path = []
for i in range(10):
    sbfs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running BFS - S:{s} D:{d}')
    path = breadthFirstSearch(nodes[s], nodes[d])

    ebfs = time.time()
    total = ebfs - sbfs
    bfs_times.append(total)
    bfs_path.append(len(path))

ucs_times = []
ucs_path = []
for i in range(10):
    sucs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running UCS - S:{s} D:{d}')
    path = uniformCostSearch(nodes[s], nodes[d])

    eucs = time.time()
    total = eucs - sucs
    ucs_times.append(total)
    ucs_path.append(len(path))

greedy_times = []
greedy_path = []
for i in range(10):
    sgreedy = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running Greedy - S:{s} D:{d}')
    path = greedySearch(nodes[s], nodes[d])

    egreedy = time.time()
    total = egreedy - sgreedy
    greedy_times.append(total)
    greedy_path.append(len(path))

bidir_times = []
bidir_path = []
for i in range(10):
    sbidir = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running bidirectional - S:{s} D:{d}')
    path = bidirectionalSearch(nodes[s], nodes[d])

    ebidir = time.time()
    total = ebidir - sbidir
    bidir_times.append(total)
    bidir_path.append(len(path))

iterdep_times = []
iterdep_path = []
for i in range(10):
    siterdep = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running iterative deepening - S:{s} D:{d}')
    path = iterativeDeepening(nodes[s], nodes[d])

    eiterdep = time.time()
    total = eiterdep - siterdep
    iterdep_times.append(total)
    iterdep_path.append(len(path))

aStar_times = []
aStar_path = []
for i in range(10):
    saStar = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    # print(f'Running A* - S:{s} D:{d}')
    path = aStarSearch(nodes[s], nodes[d], coords)

    eaStar = time.time()
    total = eaStar - saStar
    aStar_times.append(total)
    aStar_path.append(len(path))
