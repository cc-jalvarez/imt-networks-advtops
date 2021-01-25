from networks.network import Network
from typing import List, Tuple, Dict


class UndirectedNetwork(Network):
    def __init__(self, edges: List[Tuple[str, str]] = None, nodes: List[str] = None):
        self.nodes = nodes
        self.edges = edges

        self.type = 'undirected', 'static'
        self._complete_info()

        self.adj_mtr = None
        self.adj_lst = None

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

    def get_adj_mtr(self) -> List[List[int]]:

        self.adj_mtr = [[0 for i in range(len(self.nodes))] for j in range(len(self.nodes))]

        for edge in self.edges:
            i0 = self.nodes.index(edge[0])
            i1 = self.nodes.index(edge[1])
            self.adj_mtr[i0][i1] = 1
            self.adj_mtr[i1][i0] = 1

        return self.adj_mtr

    def get_adj_lst(self) -> Dict[str, List[str]]:

        self.adj_lst = dict()

        for node in self.nodes:
            self.adj_lst[node] = list()

        for edge in self.edges:
            i0, i1 = edge[0], edge[1]
            if i1 not in self.adj_lst[i0]:
                self.adj_lst[i0].append(i1)
            if i0 not in self.adj_lst[i1]:
                self.adj_lst[i1].append(i0)

        return self.adj_lst

# todo: add calc_k (here or in concepts folder)
# todo: add function to call centrality measures



if __name__ == '__main__':

    chicago96 = ['Jordan', 'Rodman', 'Pippen', 'Kerr', 'Kukoc']
    test = UndirectedNetwork(nodes=chicago96)
    print(test.nodes)
    print(test.edges)

    mtr = test.get_adj_mtr()
    print(mtr)
    lst = test.get_adj_lst()
    print(lst)


