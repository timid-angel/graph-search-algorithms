from load_graph_from_file import graph
from centrality.degree import degreeCentrality
from centrality.closeness import closenessCentrality
from centrality.betweenness import betweennessCentrality
from centrality.eigen_vector import eigenVectorCentrality
from centrality.katz import katzCentrality
from centrality.page_rank import pageRankCentrality


result = {
    "Degree Centrality": degreeCentrality(graph),
    "Closeness Centrality": closenessCentrality(graph),
    "Betweenness Centrality": betweennessCentrality(graph),
    "Katz Centrality": katzCentrality(graph),
    "Eigen-Vector Centrality": eigenVectorCentrality(graph),
    "Page-Rank Centrality": pageRankCentrality(graph),
}
