import random
import sys
from do.node import Node
from list_implementation.puller import FrontierOrderedByMissingNumbers
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


def main(N):
    universe = problem(N, seed=42)
    universe = sorted(universe, key=len, reverse=True)
    goal = ListState(frozenset([]), universe, -1)
    start_state = ListState(frozenset(i for i in range(N)), universe, -1)
    node = Node(start_state, None, -1)
    frontier = FrontierOrderedByMissingNumbers()
    searcher = ListSearch(node, frontier, goal)
    searcher.search()
    pprint(vars(searcher))
    found = [j for i in searcher.solution["actions"] for j in universe[i]]
    assert (
        len(frozenset(i for i in range(N)) - frozenset(found)) == 0
    ), "Not all numbers found"


if __name__ == "__main__":
    main(N=int(sys.argv[1]))
