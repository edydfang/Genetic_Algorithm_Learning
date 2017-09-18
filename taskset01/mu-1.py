# pylint: disable=no-member
import numpy as np

def evaluate(individual):
    return np.sum(individual)

def uniform_crossover(i1,i2):
    u = np.empty((D,))
    for i in range(D):
        # print(P[i1][i],P[i2][i])
        u[i] = np.random.choice(np.array([P[i1][i],P[i2][i]]))
    return u 

t = 1
D = 50
mu = 20

# Algorithm 2: The initialization procedure of the population
P = list()
result = list()
for i in range(mu):
    P.append(np.random.choice(np.array([0,1]),(D,)))

terminate = False

for v in P:
    result.append(evaluate(v))

while(not terminate):
    # Step1: Mating selection: generate two distinct random number
    r = np.arange(mu)
    np.random.shuffle(r)
    selected = r[:2]
    # Step2: Variation operator : Crossover
    print(uniform_crossover(selected[0],selected[1]))
    terminate = True



        