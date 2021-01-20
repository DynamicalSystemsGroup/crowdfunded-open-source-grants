import random
import networkx as nx
from typing import Callable, List
from quadratic_match import *
from subgraph_optimizer import *

def create_test_graph(n: int, seed: int) -> nx.Graph:
    internet: nx.Graph = nx.random_internet_as_graph(n, seed=seed)
    node_types: List[str] = ['grant', 'collaborator']

    for i in range(n):
        internet.add_node(i,
                          type=random.choice(node_types))

    for n in internet.edges:
        internet.edges[n]['amount_per_period_usdt'] = random.random() * 100

    return internet


def test_quadratic_match():
    G = create_test_graph(1000, 42)
    score = total_quadratic_match(G, 0.3)
    print(score)
    return True



def utility(g):
    return total_quadratic_match(g, 0.3)

def test_optimize_quadratic_match():
    G = create_test_graph(30, 42)
    utility = lambda g: total_quadratic_match(g, 0.3)
    score_real = total_quadratic_match(G, 0.3)
    score_opt = optimize_graph_connectivity(G, utility)[1]
    assert score_opt >= score_real
    print(score_real / score_opt)
    return True


if __name__ == '__main__':
    #print(test_quadratic_match())
    print(test_optimize_quadratic_match())
