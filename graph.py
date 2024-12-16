import networkx as nx
import matplotlib.pyplot as plt


def create_graph(family):
    """
    Create a visual graph for the family showing nodes and edges
    param: a family object
    """
    family_graph = nx.MultiDiGraph()
    omit_siblings = len(family_graph.nodes) > 10

    for person in family.family_dict.values():
        # Add everyone in the family dict as a node
        full_name = f"{person.first_name}\n{person.last_name}"
        family_graph.add_node(person.name, label=full_name)
        for relation, relatives in person.relation_dict.items():
            for relative in relatives:
                # If the family tree is large, we omit the sibling connections
                # to make the graph clearer
                if omit_siblings and relation == "sibling":
                    continue
                # Add relationships as edges
                family_graph.add_edge(relative.name, person.name,
                                      relation=f"{shorten_relation(relation)}")

    pos = nx.spring_layout(family_graph, seed=50, k=1)
    labels = nx.get_node_attributes(family_graph, 'label')

    if len(family_graph.nodes) <= 10:
        plt.figure(figsize=(5, 5))
        nx.draw(family_graph, pos, with_labels=True, labels=labels,
                node_size=1000, node_color="skyblue", font_size=8, arrows=True)
    else:
        plt.figure(figsize=(10, 10))
        nx.draw(family_graph, pos, with_labels=True, labels=labels,
                node_size=1500, node_color="skyblue", font_size=8, arrows=True)

    relation_labels = {}
    # Handle edge labels in multi-directed graph
    for u, v, key, data in family_graph.edges(data=True, keys=True):
        new_label = data.get('relation', '')
        if (u, v) in relation_labels:
            relation_labels[(u, v)] += f"| {new_label}"
        else:
            relation_labels[(u, v)] = new_label

    nx.draw_networkx_edge_labels(family_graph, pos,
                                 edge_labels=relation_labels,
                                 font_color="black",
                                 font_size=5, label_pos=0.7)
    plt.title("Family Tree")
    plt.show()


def shorten_relation(relation):
    """
    Return a simplified relation name
    Mother -> Mom, Father -> Dad, Children -> C,
    Sibling -> Sibs, Partner -> P.
    """
    if relation == "mother":
        return "Mom"
    elif relation == "father":
        return "Dad"
    elif relation == "children":
        return "Child"
    elif relation == "sibling":
        return "Sibs"
    elif relation == "partner":
        return "Partner"
    else:
        return "Other"
