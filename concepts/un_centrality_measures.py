from networks.undirected_network import UndirectedNetwork
from typing import Dict


def calc_centrality_degrees(network: UndirectedNetwork) -> Dict[str, float]:

    cent_deg = {}

    if network.adj_mtr is None:
        network.get_adj_mtr()

    n_edges = len(network.edges)

    for i in range(len(network.nodes)):
        cent_deg[network.nodes[i]] = sum(network.adj_mtr[i]) / n_edges

    return cent_deg


def calc_centrality_closeness(network: UndirectedNetwork) -> Dict[str, float]:

    cent_cls = {}

    return cent_cls


def calc_centrality_betweenness(network: UndirectedNetwork) -> Dict[str, float]:

    cent_btw = {}

    return cent_btw


# todo: add distance calculator
# todo: finish measures
