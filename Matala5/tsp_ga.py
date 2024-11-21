import random
import math
import numpy as np


def solve(points, pop_size=150, elite_size=12, mutation_rate=0.03, generations=120):
    population = populate(points, pop_size)
    best_distance = float('inf')
    best_individual = None

    for gen in range(generations):
        fitness_arr = [fitness(individual) for individual in population]
        elite_arr = [population[idx] for idx in np.argsort(fitness_arr)[:elite_size]]

        if fitness_arr[0] < best_distance:
            best_distance = fitness_arr[0]
            best_individual = population[0]

        next_gen = elite_arr.copy()
        while len(next_gen) < pop_size:
            parent_a, parent_b = selection(population, fitness_arr)
            child = crossover(parent_a, parent_b)
            mutate(child, mutation_rate)
            next_gen.append(child)

        population = next_gen

    return best_individual


def populate(points, pop_size):
    population = [points.copy() for i in range(pop_size)]
    random.shuffle(population)
    return population


def crossover(parent_a, parent_b):
    child = [None] * len(parent_a)
    start_a = random.randint(0, len(parent_a) - 1)
    end_a = random.randint(start_a, len(parent_a) - 1)
    for i in range(start_a, end_a + 1):
        child[i] = parent_a[i]
    idx = 0
    for i in range(len(parent_b)):
        if parent_b[i] not in child:
            while child[idx] is not None:
                idx += 1
            child[idx] = parent_b[i]
    return child


def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]


def selection(population, fitness_arr):
    # use roulette to select
    total_fitness = sum(fitness_arr)
    selection_probs = [f / total_fitness for f in fitness_arr]
    parent_a_idx = np.random.choice(len(population), p=selection_probs)
    parent_b_idx = np.random.choice(len(population), p=selection_probs)
    while parent_b_idx == parent_a_idx:
        parent_b_idx = np.random.choice(len(population), p=selection_probs)
    return population[parent_a_idx], population[parent_b_idx]


def dist(p1,p2):
    return float(math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))


def fitness(points):
    sum=0
    for i in range(1,len(points)):
        sum+=dist(points[i-1],points[i])
    return sum
