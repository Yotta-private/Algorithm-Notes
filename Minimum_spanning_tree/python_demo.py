# minimum_spanning_tree(G, weight='weight')

""" Return a minimum spanning tree or forest of an undirected weighted graph.
A minimum spanning tree is a subgraph of the graph (a tree) with the minimum sum of edge weights.
If the graph is not connected a spanning forest is constructed. A spanning forest is a union of the spanning trees for each connected component of the graph.


Parameters:	
G (NetworkX Graph) –
weight (string) – Edge data key to use for weight (default ‘weight’).
Returns:	
G – A minimum spanning tree or forest.


Return type:	
NetworkX Graph """


# Examples: ### Uses Kruskal’s algorithm

G=nx.cycle_graph(4) # 生成一个4个顶点的环状图
G.add_edge(0,3,weight=2) # assign weight 2 to edge 0-3
T=nx.minimum_spanning_tree(G) # 寻找最小生成树
print(sorted(T.edges(data=True)))
[(0, 1, {}), (1, 2, {}), (2, 3, {})]

### If the graph edges do not have a weight attribute a default weight of 1 will be used.
