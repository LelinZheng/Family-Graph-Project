

import networkx as nx
import matplotlib.pyplot as plt

# The graph may turn out differently (mess up with the relation labels) for different computer settings
# so please see our graphs in the final report for reference
def create_graph(family):
    """
    param: a family object
    """
    family_graph = nx.MultiDiGraph()

    for person in family.family_dict.values():
        # Add everyone in the family dict as a node
        family_graph.add_node(person.name)

    omit_siblings = len(family_graph.nodes) >10

    for person in family.family_dict.values():
        for relation, relatives in person.relation_dict.items():
            for relative in relatives:
                # If the family tree is large, we omit the sibling connections to make the graph clearer
                if omit_siblings and relation == "sibling":
                    continue
                # Add relationships as edges
                family_graph.add_edge(person.name, relative.name, relation=f"{relation}")

    pos = nx.spring_layout(family_graph, seed = 50)
    labels= {node: node for node in family_graph.nodes()}

    if len(family_graph.nodes) <= 10:
        plt.figure(figsize=(5, 5))
        nx.draw(family_graph, pos, with_labels=True, labels=labels, node_size=1000,
                node_color="skyblue", font_size=8, arrows=True)
    else:
        plt.figure(figsize=(10,10))
        nx.draw(family_graph, pos, with_labels=True, labels = labels, node_size = 1500,
                node_color = "skyblue", font_size = 8, arrows= True)

    relation_labels = {}
    # Handle edge labels in multi-directed graph
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

