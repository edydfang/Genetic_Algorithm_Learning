import numpy as np

def evaluateOrderthree(vector):
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

def main():
    x = np.array([1,0,0,0,1])
    print(evaluateOrderthree(x[:3]))

if __name__ == "__main__":
    main()