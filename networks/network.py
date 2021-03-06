from abc import ABC, abstractmethod
from typing import List


class Network(ABC):
    # def __init__(self, nodes: List[str], edges: List[(str, str)]):
    #     self.nodes = nodes
    #     self.edges = edges

    @abstractmethod
    def _complete_info(self):
        pass

    @abstractmethod
    def get_adj_mtr(self):
        pass

    @abstractmethod
    def get_adj_lst(self):
        pass


