# pylint: disable=no-member
import numpy as np

t = 1
D = 50
mu = 20
# Algorithm 2: The initialization procedure of the population
P = list()
for i in range(mu):
    P.append(np.random.choice(np.array([0,1]),(1,D)))

terminate = False

def evaluate(individual):
    pass


