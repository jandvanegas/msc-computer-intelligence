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
        self.explored = set()

        while True:
            if self.frontier.is_empty():
                raise Exception("no solution")

            node = self.frontier.pull()
            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not self.start:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node):
                not_visited = not self.frontier.is_visited(state)
                not_explored = state not in self.explored
                if not_visited and not_explored:
                    child = Node(state=state, parent=node, action=action)
                    self.frontier.add(child)
