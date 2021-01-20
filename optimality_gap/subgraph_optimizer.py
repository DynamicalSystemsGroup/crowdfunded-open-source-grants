import networkx as nx
import random
from typing import Callable, List
from tqdm.auto import tqdm




def optimize(G, destination_nodes, best_score, utility_function):
    for src, dst, data in tqdm(G.edges(data=True), desc='Sweeping edges'):
        for dst_node in destination_nodes:
            # Create a copy from the original graph for mutation
            temp_subgraph: nx.Graph = G.copy()
            temp_subgraph.remove_edge(src, dst)

            # Add the edge mutation
            temp_edge: tuple = (src, dst_node)
            temp_subgraph.add_edge(*temp_edge, **data)

            # Retrieve score
            score: float = utility_function(temp_subgraph)
            if score > best_score:
                best_subgraph: nx.Graph = temp_subgraph.copy()
                return (best_subgraph, best_score)
    return True


def optimize_graph_connectivity(subgraph: nx.Graph,
                                utility_function: Callable[[nx.Graph], float],
                                destination_key='destination') -> tuple:

    destination_nodes: list = [node
                               for node, value in dict(subgraph.nodes.data('type')).items()
                               if value == destination_key]

    best_subgraph: nx.Graph = subgraph.copy()
    best_score: float = utility_function(best_subgraph)
    i = 0
    previous_best_score = best_score
    while True:
        i += 1
        print(best_score)
        output = optimize(best_subgraph, destination_nodes, best_score, utility_function)
        if output is True or best_score == previous_best_score:
            break
        else:
            (best_subgraph, best_score) = output

        print(best_score)
        

    print("Optimizing subgraph")


    return (best_subgraph, best_score)
