from __future__ import annotations
from typing import TypeVar
import abc

T = TypeVar("T")


class State(abc.ABC):
    value: T

    def __eq__(self, other: State) -> bool:
        return self.value == other.value
