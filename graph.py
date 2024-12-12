from cProfile import label

import networkx as nx
import matplotlib.pyplot as plt

def create_graph(family):
    """
    param: a family object
    """
    family_graph = nx.MultiDiGraph()

    for person in family.family_dict.values():
        # Add everyone in the family dict as a node
        family_graph.add_node(person.name)
        for relation, relatives in person.relation_dict.items():
            for relative in relatives:
                # Add every relationship of the person as an edge
                if relation != "sibling":
                    family_graph.add_edge(person.name, relative.name, relation=f"{relation}")

    pos = nx.kamada_kawai_layout(family_graph)
    labels= {node: node for node in family_graph.nodes()}
    plt.figure(figsize=(10,10))
    nx.draw(family_graph, pos, with_labels=True, labels = labels, node_size = 2000,
            node_color = "skyblue", font_size = 8, arrows= True)

    relation_labels = {}
    for u,v,key,data in family_graph.edges(data=True, keys= True):
        new_label = data.get('relation','')
        if (u,v) in relation_labels:
            relation_labels[(u,v)] += f"| {new_label}"
        else:
            relation_labels[(u,v)] = new_label

    nx.draw_networkx_edge_labels(family_graph,pos, edge_labels = relation_labels,
                                 font_color="black", font_size=5, label_pos= 0.7)
    plt.title("Family Tree")
    plt.show()



