import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
friends = []

G.add_edges_from(friends)
nx.draw(G, with_labels=True, node_color = "blue", font_size = 8, bbox=dict(facecolor='red', alpha=0.5), 
        node_size = 100, edge_color = "green", width = 2.0, style = "dashed", alpha = 0.5)
plt.show()


