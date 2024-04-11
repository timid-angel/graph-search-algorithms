from search_algorithms.ucs import uniformCostSearch

def betweennessCentrality(graph):
    total_paths = 0
    score = {}

    for i in range(len(graph.nodes)):
        for j in range(len(graph.nodes)):
            total_paths += 1
            path = uniformCostSearch(graph.nodes[i], graph.nodes[j])
            for c in path:
                score[c] = score.get(c, 0) + 1

    arr = []
    for key in score:
        node = None
        for n in graph.nodes:
            if n.val == key:
                node = n
                break
        
        arr.append((node, score[key] / total_paths))
    
    return sorted(arr, key= lambda x: x[1], reverse=True)
