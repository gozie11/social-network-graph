
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
import pandas as pd

# Read excel file
file = "social_network_graph_data.xlsx"
book = pd.read_excel(file)

print(book.columns)

# Create list of friends
friends = []
for index, row in book.iterrows():
    friends.append((row['Friend1'], row['Friend2']))

# Draw graph
G = nx.Graph()
G.add_edges_from(friends)
nx.draw(G, with_labels=True, node_color = "blue", font_size = 10, bbox=dict(facecolor='red', alpha=0.5), 
        node_size = 100, edge_color = "green", width = 2.0, alpha = 0.5)
plt.show()


 