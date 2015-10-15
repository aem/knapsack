"""
Solver for the popular knapsack problem.
"""
import sys


def print_2d_arr(arr):
    for a in arr:
        for i in a:
            print str(i) + "\t"
        print "\n"


def solve(values, weights, capacity):
    assert capacity > 0
    assert len(values) == len(weights)

    result = []

    # if the total weights are less than the capacity
    # then return the whole list
    if sum(weights) < capacity:
        return values

result = []
v = None
w = None
c = None

if len(sys.argv) > 1:
    v = sys.argv[1]
    w = sys.argv[2]
    c = sys.argv[3]

if v is not None and w is not None and c is not None:
    result = solve(v, w, c)

print result

print_2d_arr([[1, 2, 3],
              [2, 3, 4],
              [3, 4, 5]])
