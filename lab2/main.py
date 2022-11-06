import random
import itertools
import sys
from do.individual import Individual
from typing import List, Callable

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
    population = random_population(all_genes, fitness_function)
    evolve(population, N, fitness_function)


def evolve(
    population: List[Individual],
    N: int,
    fitness_function: Callable[[Individual], int],
) -> List[Individual]:
    for iter in range(NUM_GENERATIONS):
        offspring = list()
        for _ in range(OFFSPRING_SIZE):
            if random.random() < 0.5:
                individual = tournament(population)
                o = mutation(individual, N, fitness_function)
            else:
                i1 = tournament(population)
                i2 = tournament(population)
                o = cross_over(i1, i2, fitness_function)
            offspring.append(o)
        population += offspring
        population = sorted(population, key=lambda i: i.fitness, reverse=True)[
            :POPULATION_SIZE
        ]
        for i in population:
            print(
                "Population Fitness: ",
                [i.fitness for i in population],
            )
            print(f"N:{N}'")
            if i.fitness == N:
                print(f"Found solution: {i}\n")
                print("with lenght {len(i.genome)} at iter {iter}")
                sys.exit(0)


def tournament(population: List[Individual], tournament_size=2) -> Individual:
    return max(
        random.choices(population, k=tournament_size),
        key=lambda i: i.fitness,
    )


def cross_over(
    i1: Individual,
    i2: Individual,
    fitness_function: Callable[[Individual], int],
) -> Individual:
    """Cross over two individuals"""
    new_genome = list(
        itertools.chain(
            i1.genome,
            i2.genome,
        )
    )
    random.shuffle(new_genome)
    genome_size = len(new_genome) // 2
    if random.random() < 1:
        genome_size = genome_size + 1
    elif genome_size > 2:
        genome_size = genome_size - 1

    return Individual(
        genome=new_genome[0:genome_size],
        fitness_function=fitness_function,
    )


def mutation(
    individual: Individual,
    N: int,
    fitness_function: Callable[[Individual], int],
) -> Individual:
    point = random.randint(0, len(individual.genome) - 1)
    new_gene = random.randint(0, N - 1)
    while new_gene in individual.genome:
        new_gene = random.randint(0, N - 1)
    return Individual(
        genome=list(
            itertools.chain(
                individual.genome[:point],
                [new_gene],
                individual.genome[point + 1:],
            )
        ),
        fitness_function=fitness_function,
    )


def fitness(all_genes: List[int]) -> Callable[[Individual], int]:
    """Return fitness evaluation function"""

    def fitness_of_genome(individual: Individual) -> int:
        found = [j for i in individual.genome for j in all_genes[i]]
        return len(frozenset(found))

    return fitness_of_genome


def random_population(
    all_genes, fitness_function: Callable[[Individual], int]
) -> List[Individual]:
    """Creates a random population"""
    return [
        Individual(
            genome=[random.randint(0, len(all_genes) - 1)],
            fitness_function=fitness_function,
        )
        for _ in range(POPULATION_SIZE)
    ]


if __name__ == "__main__":
    main(N=int(sys.argv[1]))
