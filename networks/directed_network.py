from networks.network import Network
from typing import List, Tuple, Dict


class DirectedNetwork(Network):
    def __init__(self, edges: List[Tuple[str, str]], nodes: List[str] = None):
        self.nodes = nodes
        self.edges = edges

        self.type = 'directed', 'static'
        self._complete_info()

        self.adj_mtr = None
        self.adj_lst = None

    def _complete_info(self):
        # we always need the edge list
        if self.edges is None:
            raise Exception("Sorry. You need to provide at least an edges list.")
        elif self.edges and self.nodes is None:
            self.nodes = []
            for (node_i, node_j) in self.edges:
                if node_i not in self.nodes:
                    self.nodes.append(node_i)
                if node_j not in self.nodes:
                    self.nodes.append(node_j)
        # check for edge equivalence: (node_i, node_j) != (node_j, node_i)
        res = set()
        for (a, b) in self.edges:
            if (a, b) and (b, a) not in res:
                res.add((a, b))
        temp_edges = list(res)
        if len(self.edges) != len(temp_edges):
            raise Exception("Sorry. Edges list cannot contain both edges (a, b) and (b, a).")
        else:
            del res, temp_edges

    def get_adj_mtr(self) -> List[List[int]]:

        self.adj_mtr = [[0 for i in range(len(self.nodes))] for j in range(len(self.nodes))]

        for edge in self.edges:
            i0 = self.nodes.index(edge[0])
            i1 = self.nodes.index(edge[1])
            # edge i0 -> i1: from the ith row to the jth column
            self.adj_mtr[i0][i1] = 1

        return self.adj_mtr

    def get_adj_lst(self) -> Dict[str, List[str]]:

        self.adj_lst = dict()

        for node in self.nodes:
            self.adj_lst[node] = list()

        for edge in self.edges:
            i0, i1 = edge[0], edge[1]
            if i1 not in self.adj_lst[i0]:
                self.adj_lst[i0].append(i1)

        return self.adj_lst

# todo: add calc_k_i and calc_k_o (here or in concepts folder)


if __name__ == '__main__':

    chicago96 = ['Jordan', 'Rodman', 'Pippen', 'Kerr', 'Kukoc']
    passes_q1 = [('Jordan', 'Rodman'), ('Jordan', 'Pippen'), ('Jordan', 'Kerr'), ('Kerr', 'Kukoc')]
    test = DirectedNetwork(edges=passes_q1, nodes=chicago96)
    print(test.nodes)
    print(test.edges)

    mtr = test.get_adj_mtr()
    print(mtr)
    lst = test.get_adj_lst()
    print(lst)


