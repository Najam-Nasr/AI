
import random

def f(x):
    return -x**2 + 6*x

def hill_climbing():
    x = random.randint(0, 6)
    print("Initial x = " + str(x) + ", f(" + str(x) + ") = " + str(f(x)))

    step = 1
    while True:
        current = f(x)
        neighbors = []

        if x - 1 >= 0:
            neighbors.append(x - 1)
        if x + 1 <= 6:
            neighbors.append(x + 1)

        best = max(neighbors, key=lambda n: f(n))

        if f(best) > current:
            print("Step " + str(step) + ": x = " + str(x) + " -> " + str(best) + ", f(" + str(best) + ") = " + str(f(best)))
            x = best
            step += 1
        else:
            print("Stopped. No better neighbor found.")
            print("Optimal x = " + str(x) + ", f(" + str(x) + ") = " + str(f(x)))
            break

hill_climbing()
