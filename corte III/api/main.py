import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

G.add_node("Yaneth")
G.add_node("Juan")
G.add_node("Alberto")
G.add_node("Lola Mento")
G.add_node("Marco de la puerta")

G.add_edges_from(
    [("Yaneth", "Alberto"), ("Juan", "Marco de la puerta"), ("Juan", "Lola Mento")]
)
nx.draw(G, with_labels = True)
plt.show()