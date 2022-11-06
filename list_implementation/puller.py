from do.frontier import Frontier
from do.node import Node


class FrontierOrderedByMissingNumbers(Frontier):
    def puller(self) -> tuple[list, Node]:
        frontier = sorted(self.frontier, key=lambda x: len(x.state.value))
        return frontier[1:], frontier[0]
