import networkx as nx
import matplotlib.pyplot as plt


def create_graph(family):
    """
    param: a family object
    """
    corresponding_relation_dict = {"mother":"children","father":"children","partner":"partner"}

    family_graph = nx.DiGraph()
    for person in family.family_dict.values():
        # Add everyone in the family dict as a node
        family_graph.add_node(person.name)
        for relation, relatives in person.relation_dict.items():
            for relative in relatives:
                # Add every relationship of the person as an edge
                if relation != "sibling":
                    corresponding_relation = corresponding_relation_dict.get(relation,"related")
                    if relation == "partner":
                        family_graph.add_edge(person.name,
                                              relative.name,
                                              weight= 1,
                                              relation=f"{relation}-{corresponding_relation}")
                    else:
                        family_graph.add_edge(person.name,
                                              relative.name,
                                              weight = 2,
                                              relation= f"{relation}-{corresponding_relation}")

    pos = nx.kamada_kawai_layout(family_graph)
    labels= {node: node for node in family_graph.nodes()}
    plt.figure(figsize=(10,10))
    nx.draw(family_graph, pos, with_labels=True, labels = labels, node_size = 2000,
            node_color = "skyblue", font_size = 8, arrows= True)
    relationship_labels = nx.get_edge_attributes(family_graph, "relation")
    nx.draw_networkx_edge_labels(family_graph,pos,edge_labels = relationship_labels,
                                 font_color="black", font_size=5, label_pos= 0.5)
    plt.title("Family Tree")
    plt.show()



