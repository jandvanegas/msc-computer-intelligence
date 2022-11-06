from __future__ import annotations
from dataclasses import dataclass
from typing import List, Callable


@dataclass
class Individual:
    "The genotype is the individual organism's unique set of all the genes."
    genome: List[int]
    fitness_function: Callable[[Individual], int]
    fitness: int = 0

    def __post_init__(self):
        self.fitness = self.fitness_function(self)
