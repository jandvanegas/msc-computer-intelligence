from __future__ import annotations
import abc

from .state import State
from .node import Node


class Frontier(abc.ABC):
    def __init__(self):
        self.frontier = []
        self.visited = set()

    def add(self, node: Node) -> None:
        self.frontier.append(node)
        self.visited.add(node.state)

    @abc.abstractmethod
    def puller(self) -> tuple[list, Node]:
        raise NotImplementedError

    def pull(self) -> Node:
        """
        Pulls a node from the frontier using the puller function.
        """
        self.frontier, node = self.puller()
        return node

    def is_empty(self) -> bool:
        return len(self.frontier) == 0

    def is_visited(self, state: State) -> bool:
        return state in self.visited

    def __len__(self) -> int:
        return len(self.frontier)

    def __str__(self) -> str:
        return str(self.frontier)


class StackFrontier(Frontier):
    def puller(self) -> tuple[list, Node]:
        return self.frontier[:-1], self.frontier[-1]


class QueueFrontier(Frontier):
    def puller(self) -> tuple[list, Node]:
        return self.frontier[1:], self.frontier[0]
