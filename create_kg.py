from kgn_pathfinding import *


#Edges from harder to easier topics
nodes = [(1, {"labelV":"C", "path_to_excel":"DTL_Knowledge_Graph_Test.xlsx"}), 
        (2, {"labelV":"C++", "path_to_excel":"DTL_Knowledge_Graph_Test.xlsx"}),
        (3, {"labelV":"DataStructures", "path_to_excel":"DTL_Knowledge_Graph_Test.xlsx"}),
        (4, {"labelV":"Algorithms", "path_to_excel":"DTL_Knowledge_Graph_Test.xlsx"}),
        (5, {"labelV":"AdvancedAlgorithms", "path_to_excel":"DTL_Knowledge_Graph_Test.xlsx"})]
edges = [(2, 1),(3, 1),(3, 2),(4, 3),(5, 4)]

G2 = nx.DiGraph()
G2.add_nodes_from(nodes)
G2.add_edges_from(edges)
nx.write_graphml(G2, "KG.graphml")