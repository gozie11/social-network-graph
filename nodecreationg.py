import networkx as nx
import matplotlib.pyplot as plt
import xlrd

file = open("social_network_graph_data.xlsx")

G = nx.Graph()
friends = []

xlrd.open_workbook("social network graph data.xlsx")
sheet = file.sheet_by_index(0)

for row in range(sheet.nrows):
    friends.append(((sheet.cell_value(row, 0), sheet.cell_value(row, 1))))

print(friends)
G.add_edges_from(friends)
nx.draw(G, with_labels=True, node_color = "blue", font_size = 8, bbox=dict(facecolor='red', alpha=0.5), 
        node_size = 100, edge_color = "green", width = 2.0, style = "dashed", alpha = 0.5)
plt.show()


