#!/usr/bin/env python
# pylint: disable=no-member
import numpy as np
import functools

def evaluateOrderOne(vector):
    return np.sum(vector)

def evaluateOrderThree(vector):
    tmp = np.sum(vector)
    if tmp == 3:
        return 30
    elif tmp == 2:
        return 0
    elif tmp == 0:
        return 28
    else:
        if vector[0]==1 :
            return 14
        elif vector[1] == 1:
            return 22
        elif vector[2] == 1:
            return 26


def bitflip_mutation(bit, probability):
    if np.random.rand() < probability:
        if bit == 1:
            return 0.
        else:
            return 1.
    else:
        return bit


def uniform_crossover(P,D,i1,i2):
    u = np.empty((D,))
    for i in range(D):
        # print(P[i1][i],P[i2][i])
        u[i] = np.random.choice(np.array([P[i1][i],P[i2][i]]))
    return u

def geAlgorithm():
 
    n = 0
    t = 1
    D = 24
    mu = 20
    pm = 1/D # mutation rate
    lambda_ = 30
    evaluate = evaluateOrderOne
    # Algorithm 2: The initialization procedure of the population
    P = list()
    result = list()
    for i in range(mu):
        P.append(np.random.choice(np.array([0,1]),(D,)))

    terminate = False
    x_bsf = None
    value_bsf = 0

    for v in P:
        value = evaluate(v)
        result.append(evaluate(v))
        if(value>value_bsf):
            value_bsf = value
            x_bsf = v
    
    while(not terminate):
        Q = list()
        for i in range(lambda_):
            # Step1: Mating selection: generate two distinct random number
            r = np.arange(len(P))
            np.random.shuffle(r)
            selected = r[:2]
            #print(selected)
            # Step2: Variation operator : Crossover
            u = uniform_crossover(P,D, selected[0],selected[1])
            # print(u)
            # Step3: Variation operator2: Mutation
            vfunc = np.vectorize(functools.partial(bitflip_mutation, probability=pm))
            u = vfunc(u)
            # print(u)
            # Step4: Evaluate
            newvalue = evaluate(u)
            # print("New value:" + str(newvalue))
            n += 1
            new_value = evaluate(u)
            
            # Step5: Update bsf solution
            
            if(new_value >value_bsf):
                value_bsf = value
                x_bsf = u
            # Step6: Environment Selection
            selected = np.random.randint(0,mu)
            if(result[selected]<new_value):
                P[selected] = u
                result[selected] = new_value
        t += 1
        if(new_value == 30):
            terminate = True

    print("# of generation:", t)
    return t

if __name__ == "__main__":
    count = list()
    totaltimes = 1
    for i in range(totaltimes):
        count.append(geAlgorithm())
    print("Average # of generations %f" % (sum(count)/float(totaltimes)))

## Result average: 449.25