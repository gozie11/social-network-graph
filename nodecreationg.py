import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
friends = [("Joshua", "Mario", "Gozie"), ("mother", "father"),("Gozie", "Obinna")]
professions = ["Cook", "Programmer", "Engineer", "Doctor"]

for friend in friends:
    G.add_node(friend)

G2 = nx.Graph()

G.add_edges_from(friends)
for profession in professions:
    G2.add_node(profession) 

G.add_edge("Gozie", "Joshua")
G.add_edge("Gozie", "Mario")
G.add_edge("Gozie", "Obinna")
G.add_edge("Joshua", "Mario")
G.add_edge("Joshua", "Obinna")


plt.figure(1)
nx.draw(G, with_labels=True, node_color = "yellow")
#nx.draw(G2,node_color = "yellow" ,with_labels=True)

# plt.figure(2)
# nx.draw(G2,node_color = "yellow" ,with_labels=True)

plt.show()

#print(nx.nodes(G))