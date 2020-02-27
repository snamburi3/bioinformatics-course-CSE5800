#!/usr/bin/python
from collections import Counter
import sys

"""
Given: A multiset L containing (n2) positive integers for some positive integer n.

Return: A set X containing n nonnegative integers such that ΔX=L.
"""

# read the file
filepath = sys.argv[1]
with open(filepath) as fp:
   input_line = fp.readline().strip()

multiset_L = list(map(int,input_line.split(" ")))

# set X as 0
X = [0]

# find distance between y and X
def dist_y_X(y, X):
    all_dists = []
    for ele in X:
        all_dists.append(abs(y-ele))
    return (all_dists)

def delete_elements(l1, l2):
    c1 = Counter(l1)
    c2 = Counter(l2)

    diff = c1-c2
    x = list(diff.elements())
    return x

def place(L):

    explored_branches = []
    possible_solutions = []

    while(L):

        branches = list(set(L) - set(explored_branches))

        if not L:
            possible_solutions.append(X)

        if not branches:
            break

        # find the largest element, which is the width
        y = max(branches)
        explored_branches.append(y) 

        X.append(y)
        dist_y =  dist_y_X(y,X)

        # check subset of list  
        flag = 0
        if(set(dist_y).issubset(set(multiset_L + [0]))): 
            flag = 1
            L = delete_elements(L, dist_y)
            if not L:
                possible_solutions.append(X)
        else:
            X.remove(y)
    return possible_solutions


for solution in place(multiset_L):
    solution.sort()
    print(" ".join(map(str, solution)))
    

