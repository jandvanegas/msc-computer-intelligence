from __future__ import annotations
from do.state import State


class ListState(State):
    value: frozenset[int]
    lists: list[list[int]]
    list_number: int

    def __init__(
        self,
        value: frozenset[int],
        lists: list[list[int]],
        list_number: int,
    ) -> None:
        self.value = value
        self.lists = lists
        self.list_number = list_number

    def __eq__(self, other: ListState) -> bool:
        if not isinstance(other, ListState):
            return False
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)
