from networks.undirected_network import UndirectedNetwork
from typing import Dict, List, Tuple


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

    for node_i in network.nodes:

        for node_j in [n for n in network.nodes if n != node_i]:

            sum_dist = []

            # find all paths from i to j
            a_paths = find_all_paths(adj_lst=network.adj_lst, start=node_i, goal=node_j)

            # find all shortest paths and distance from i to j
            s_paths = find_shortest_path(all_paths=a_paths, start=node_i, goal=node_j)
            # sum their distances
            for s_path in s_paths:
                sum_dist.append(s_path[1])

        cent_cls[node_i] = len(network.nodes) / sum(sum_dist)

    return cent_cls


def calc_centrality_betweenness(network: UndirectedNetwork) -> Dict[str, float]:

    cent_btw = {}

    return cent_btw


# ----- misc. functions

# Find all paths from i (start) to j (goal)
def find_all_paths(adj_lst: dict, start: str, goal: str) -> List[List[str]]:
    
    all_paths = []

    explored = []
    queue = [[start]]  # set queue as a list of lists

    # loop over until queue is empty (i.e. no longer True): exhaustive search
    while queue:
        # get path to explore and remove from queue
        path = queue.pop(0)
        # start from the last node on current path (where you left off)
        node = path[-1]

        if node not in explored:
            neighbours = adj_lst[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                # unless at the goal, add new path to queue to explore further in next iteration
                if neighbour == goal:
                    all_paths.append(new_path)
                else:
                    queue.append(new_path)

        # go back to the queue after exploring node's neighbourhood
        explored.append(node)

    return all_paths


# Find shortest path from i (start) to j (goal)
def find_shortest_path(all_paths, start: str, goal: str, adj_mat_weighted=None) -> List[Tuple[List[str], int]]:

    shortest_paths = []

    if adj_mat_weighted:
        pass  # TODO
    else:
        # using equal weights for all edges (steps of 1's)
        min_d = min([len(l) for l in all_paths])
        for (idx, d) in [(idx, d) for (idx, d) in enumerate([len(l) for l in all_paths])]:
            if d == min_d:
                shortest_paths.append((all_paths[idx], d - 1))  # d - 1 steps is the 'real' distance here

    return shortest_paths


