from __future__ import annotations
from dataclasses import dataclass
from .state import State
from .action import Action


@dataclass()
class Node:
    state: State
    parent: Node
    action: Action
