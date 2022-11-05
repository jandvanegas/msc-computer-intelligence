from do.node import Node
from do.search import Search
from do.state import State
from .list_state import ListState
from typing import List


class ListSearch(Search):
    def neighbors(self, node: Node) -> List[tuple[int, State]]:
        lists = node.state.lists
        list_number = node.state.list_number
        for i, list_ in enumerate(lists[list_number + 1:]):
            yield list_number + i, ListState(
                node.state.value.difference(frozenset(list_)),
                lists,
                list_number + i,
            )
