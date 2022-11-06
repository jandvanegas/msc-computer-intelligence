import random
import sys
from evolution_utils import fitness, random_population, evolve

POPULATION_SIZE = 5
OFFSPRING_SIZE = 3
NUM_GENERATIONS = 1000


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
    all_genes = problem(N, seed=42)
    fitness_function = fitness(all_genes)
    population = random_population(
        all_genes,
        fitness_function,
        POPULATION_SIZE,
    )
    evolve(
        population,
        N,
        fitness_function,
        num_generations=NUM_GENERATIONS,
        offspring_size=OFFSPRING_SIZE,
        population_size=POPULATION_SIZE,
    )


if __name__ == "__main__":
    main(N=int(sys.argv[1]))
