from do.node import Node
from do.search import Search
from do.state import State
from .list_state import ListState
from typing import List


class ListSearch(Search):
    def neighbors(self, node: Node) -> List[tuple[int, State]]:
        lists = node.state.lists
        list_number = node.state.list_number
        for i, list_ in enumerate(
            lists[list_number + 1:],
            start=list_number + 1,
        ):
            new_missing = node.state.value.difference(frozenset(list_))
            # add only if it has missing integers
            if len(new_missing) != len(node.state.value):
                yield i, ListState(
                    new_missing,
                    lists,
                    i,
                )

    def search(self):
        super().search()
        self.solution["lenght"] = len(self.solution["actions"])
