from .state import State
from .node import Node
from .action import Action
from .frontier import Frontier
import abc


class Search(abc.ABC):
    @abc.abstractmethod
    def neighbors(self, state: State) -> list[tuple[Action, State]]:
        raise NotImplementedError

    def __init__(self, start: Node, frontier: Frontier, goal: State):
        self.start = start
        self.frontier = frontier
        self.goal = goal

    def search(self):
        self.num_explored = 0
        self.frontier.add(self.start)

        while True:
            if self.frontier.is_empty():
                raise Exception("no solution")

            node = self.frontier.pull()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent.action is not self.start.action:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.append(node.action)
                cells.append(node.state)
                actions.reverse()
                cells.reverse()
                self.solution = {"actions": actions, "cells": cells}
                return

            for action, state in self.neighbors(node):
                child = Node(state=state, parent=node, action=action)
                self.frontier.add(child)
