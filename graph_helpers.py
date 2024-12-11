# Graphs can stay here or go into helper functions

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("Zeynab", "Sigge", weight="mom-child")
G.add_edge("Sigge", "Simagne", weight="siblings")
G.add_edge("Sigge", "Jedd", weight="dad-child")
G.add_edge("Simagne", "Mimi",weight="mom-child")
G.add_edge("Simagne", "Jedd",weight="dad-child")
#G.add_edge(4, 5)

# explicitly set positions
pos = {"Zeynab": (0, 0), "Sigge": (2, 1), "Simagne": (6, 1),
       "Jedd": (4, 2), "Mimi": (8, 0.00) }

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