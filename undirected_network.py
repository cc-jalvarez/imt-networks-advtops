from network import Network
from typing import List, Tuple


class UndirectedNetwork(Network):
    def __init__(self, nodes: List[str] = None, edges: List[Tuple[str, str]] = None):
        self.nodes = nodes
        self.edges = edges

        self._complete_info()

    def _complete_info(self):
        # edges -> nodes, while (when fully connected) nodes
        if self.nodes is None and self.edges is None:
            raise Exception("Sorry. You need to provide at least either a nodes list or an edges list.")
        elif self.nodes is None and self.edges:
            self.nodes = []
            for (node_i, node_j) in self.edges:
                if node_i not in self.nodes:
                    self.nodes.append(node_i)
                if node_j not in self.nodes:
                    self.nodes.append(node_j)
        elif self.nodes and self.edges is None:
            self.edges = []
            print("Deriving the edge list. Assuming a fully connected network.")
            for node_i in self.nodes:
                for node_j in [node for node in self.nodes if node != node_i]:
                    self.edges.append((node_i, node_j))
        # edge equivalence: (node_i, node_j) = (node_j, node_i)
        res = set()
        for (a, b) in self.edges:
            if (a, b) and (b, a) not in res:
                res.add((a, b))
        self.edges = list(res)
        del res

    # TODO: get_adj_matrix(), get_adj_list(); update Networks(ABC)
    # TODO: add centrality topological concepts folder


if __name__ == '__main__':
    test = UndirectedNetwork(nodes=['Jordan', 'Pippen', 'Rodman'])
    print(test.nodes)
    print(test.edges)
