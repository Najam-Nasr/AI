import random

def f(x):
    return x**2 + 2*x

def to_binary(x):
    return format(x, '05b')

def to_decimal(b):
    return int(b, 2)

def fitness(b):
    return f(to_decimal(b))

def selection(population):
    population.sort(key=lambda b: fitness(b), reverse=True)
    return population[:2]

def crossover(p1, p2):
    point = random.randint(1, 4)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2

def mutate(b):
    b = list(b)
    i = random.randint(0, 4)
    b[i] = '1' if b[i] == '0' else '0'
    return ''.join(b)

population = [to_binary(random.randint(0, 31)) for _ in range(4)]

for gen in range(15):
    parents = selection(population)
    c1, c2 = crossover(parents[0], parents[1])
    c1 = mutate(c1)
    c2 = mutate(c2)
    population = parents + [c1, c2]

best = max(population, key=lambda b: fitness(b))
x = to_decimal(best)

print("Best chromosome: " + best)
print("Best x: " + str(x))
print("Best fitness: " + str(f(x)))
