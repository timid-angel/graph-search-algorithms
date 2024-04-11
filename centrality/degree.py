from centrality.node_count import getCount

def degreeCentrality(graph):
    n = getCount(graph.nodes[0])
    arr = []
    for node in graph.nodes:
        arr.append((node, len(node.nbs) / (n - 1)))
    
    return sorted(arr, key= lambda x: x[1], reverse=True)