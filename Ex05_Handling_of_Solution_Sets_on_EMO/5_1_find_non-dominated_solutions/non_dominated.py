#! /usr/bin/env python3

'''
This programe is to find all non-dominated result generated from
the solution set of multi-objective optimizations for EA.abs

Sort in all components and get the rank for each solution

A better algorithm should sort and then filter and have a
Time Complexity: O(dnlogn) where d is the dimension of solutions and
n is the number of solutions
'''

import sys
import numpy as np

def filter_solutions(solution_set):
    '''
    filter the non-dominated solutions
    dominated: there is one solution larger than it in every component
    '''
    tmp_set = solution_set.copy()
    is_efficient = np.ones(tmp_set.shape[0], dtype=bool)
    for idx, vector in enumerate(tmp_set):
        intermid = np.all(tmp_set > vector, axis=1)
        is_efficient[idx] = not np.any(intermid)
        #tmp_set = np.delete(tmp_set, np.where(intermid), axis=0)
    return is_efficient

def output_nondominated(filename):
    '''
    function to process
    '''
    file = open(filename, mode='r')
    data = file.readlines()
    data_num = list()
    for rec in data:
        tmp = rec.split(',')
        vec = list()
        for str_tmp in tmp:
            vec.append(float(str_tmp.strip()))
        data_num.append(vec)
    file.close()
    data_num = np.matrix(data_num)
    result = filter_solutions(data_num)
    idxs = np.where(result)[0]
    for idx in idxs:
        print(data[idx], end='')
    print("count:", len(data_num[result]))

def main():
    '''
    entrance
    '''
    # print(sys.argv)
    if len(sys.argv) > 1:
        filenames = sys.argv[1:]
    for filename in filenames:
        output_nondominated(filename)

if __name__ == '__main__':
    '''
    Just run ./non_dominated.py dtlz*.dat
    '''
    main()
