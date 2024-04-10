import math
from graph import Graph
from graph import Node

def getDistance(city1, city2, coords):
    x1, x2 = coords[city1][1], coords[city2][1]
    y1, y2 = coords[city1][0], coords[city2][0]

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


file = open("./data.txt", "r")
coords = {} # map city -> coordinates
nodes = {} # map city names -> node objects

line = file.readline()
while line:
    line = file.readline()
    if line.strip():
        entry = line.split("    ")
        city, lat, long = entry[0], float(entry[1].strip()), float(entry[2].strip())
        
        if city not in nodes:
            nodes[city] = Node(city)

        coords[nodes[city]] = (lat, long)

file.close()

graph = Graph()

file = open("./connections.txt", "r")
line = file.readline()
while line:
    res = line.split(" ")
    c1, c2 = res[0].strip(), res[1].strip()

    d = getDistance(nodes[c1], nodes[c2], coords)
    d = round(d, 4)
    graph.addEdge(nodes[c1], nodes[c2], d)
    graph.addEdge(nodes[c2], nodes[c1], d)
    
    line = file.readline()

file.close()
