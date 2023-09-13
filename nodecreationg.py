import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
friends = [("Joshua", "Mario",), ("mother", "father"),("Gozie", "Obinna")]


G2 = nx.Graph()

G.add_edges_from(friends)

nx.draw(G, with_labels=True, node_color = "blue", font_size = 8, bbox=dict(facecolor='red', alpha=0.5), node_size = 100, edge_color = "green", width = 2.0, style = "dashed", alpha = 0.5)

# plt.figure(2)
# nx.draw(G2,node_color = "yellow" ,with_labels=True)

plt.show()

#print(nx.nodes(G))

