import random
from do.node import Node
from do.frontier import QueueFrontier
from list_implementation.list_search import ListSearch, ListState

from pprint import pprint


def problem(N, seed=None):
    """Creates an instance of the problem"""
    random.seed(seed)
    return [
        list(
            set(
                random.randint(0, N - 1)
                for _ in range(
                    random.randint(
                        N // 5,
                        N // 2,
                    )
                )
            )
        )
        for _ in range(random.randint(N, N * 5))
    ]


def main():
    N = 10
    universe = problem(N, seed=42)
    universe = sorted(universe, key=len, reverse=True)
    goal = ListState(frozenset([]), universe, 0)
    start_state = ListState(frozenset(i for i in range(N)), universe, -1)
    node = Node(start_state, None, None)
    frontier = QueueFrontier()
    searcher = ListSearch(node, frontier, goal)
    searcher.search()
    pprint(vars(searcher))


if __name__ == "__main__":
    main()
