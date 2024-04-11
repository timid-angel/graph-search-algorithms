import time
import random

from search_algorithms.bfs import breadthFirstSearch
from search_algorithms.dfs import depthFirstSearch
from search_algorithms.ucs import uniformCostSearch
from search_algorithms.greedy import greedySearch
from search_algorithms.bidirectional import bidirectionalSearch
from search_algorithms.iterative_deepening import iterativeDeepening
from search_algorithms.a_star import aStarSearch
from load_graph_from_file import cities
from load_graph_from_file import nodes

dfs_times = []
for i in range(10):
    sdfs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running DFS - S:{s} D:{d}')
    depthFirstSearch(nodes[s], nodes[d])

    edfs = time.time()
    total = edfs - sdfs
    dfs_times.append(total)

print(dfs_times)

bfs_times = []
for i in range(10):
    sbfs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running BFS - S:{s} D:{d}')
    breadthFirstSearch(nodes[s], nodes[d])

    ebfs = time.time()
    total = ebfs - sbfs
    bfs_times.append(total)

print(bfs_times)

ucs_time = []
for i in range(10):
    sucs = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running UCS - S:{s} D:{d}')
    uniformCostSearch(nodes[s], nodes[d])

    eucs = time.time()
    total = eucs - sucs
    ucs_time.append(total)

print(ucs_time)

greedy_time = []
for i in range(10):
    sgreedy = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running Greedy - S:{s} D:{d}')
    greedySearch(nodes[s], nodes[d])

    egreedy = time.time()
    total = egreedy - sgreedy
    greedy_time.append(total)

print(greedy_time)

bidir_time = []
for i in range(10):
    sbidir = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running bidirectional - S:{s} D:{d}')
    bidirectionalSearch(nodes[s], nodes[d])

    ebidir = time.time()
    total = ebidir - sbidir
    bidir_time.append(total)

print(bidir_time)

iterdep_time = []
for i in range(10):
    siterdep = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running iterative deepening - S:{s} D:{d}')
    iterativeDeepening(nodes[s], nodes[d])

    eiterdep = time.time()
    total = eiterdep - siterdep
    iterdep_time.append(total)

print(iterdep_time)

aStar_time = []
for i in range(10):
    saStar = time.time()
    s = random.choice(cities)
    d = random.choice(cities)
    print(f'Running A* - S:{s} D:{d}')
    aStarSearch(nodes[s], nodes[d])

    eaStar = time.time()
    total = eaStar - saStar
    aStar_time.append(total)

print(aStar_time)