import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Zeynab", "Alice", weight="mom-child")
G.add_edge("Alice", "Grace", weight="siblings")
G.add_edge("Alice", "Peter", weight="dad-child")
G.add_edge("Grace", "Lucy",weight="mom-child")
G.add_edge("Grace", "Peter",weight="dad-child")
#G.add_edge(4, 5)

# explicitly set positions
pos = {"Zeynab": (0, 0), "Alice": (2, 1), "Grace": (6, 1), "Peter": (4, 2), "Lucy": (8, 0.00) }

options = {
    "font_size": 12,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)
# edge weight labels
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()