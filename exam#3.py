import networkx as nx


G = nx.Graph()

G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('F', 'G'), ('A', 'E')])


num_components = nx.number_connected_components(G)

print(num_components)

