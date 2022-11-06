import random
import itertools
import sys
from do.individual import Individual
from typing import List, Callable


def evolve(
    population: List[Individual],
    N: int,
    fitness_function: Callable[[Individual], int],
    num_generations: int,
    offspring_size: int,
    population_size: int,
) -> List[Individual]:
    for iter in range(num_generations):
        offspring = list()
        for _ in range(offspring_size):
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
            :population_size
        ]
        for i in population:
            print(
                "Population Fitness: ",
                [i.fitness for i in population],
            )
            print(f"N:{N}'")
            if i.fitness == N:
                print(f"Found solution: {i}\n")
                print(f"with lenght {len(i.genome)} at iter {iter}")
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
                individual.genome[point + 1 :],
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
    all_genes,
    fitness_function: Callable[[Individual], int],
    population_size: int,
) -> List[Individual]:
    """Creates a random population"""
    return [
        Individual(
            genome=[random.randint(0, len(all_genes) - 1)],
            fitness_function=fitness_function,
        )
        for _ in range(population_size)
    ]
