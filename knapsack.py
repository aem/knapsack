"""
Solver for the popular knapsack problem.

USAGE: python knapsack.py '1,2,3,4,5' '5,4,3,2,1' 10
"""
import sys
from itertools import repeat


def print_2d_arr(arr):
    for a in arr:
        s = ""
        for i in a:
            s += str(i) + "\t"
        print s


def solve(values, weights, capacity):
    assert capacity > 0
    assert len(values) == len(weights)

    result = []
    n = len(values)

    # if the total weights are less than the capacity
    # then return the whole list
    if sum(weights) < capacity:
        return values

    # initialize the grid with zeroes to start
    grid = list(repeat([], capacity + 1))
    for arr in range(capacity + 1):
        grid[arr] = list(repeat(0, len(values) + 1))

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                grid[w][i] = 0
            else:
                # if weights[i] > w:
                    grid[w][i] = 1
    print_2d_arr(grid)

result = []
vs = None
ws = None
c = None

if len(sys.argv) > 1:
    vs = [int(x) for x in sys.argv[1].split(',')]
    ws = [int(x) for x in sys.argv[2].split(',')]
    c = int(sys.argv[3])

if vs is not None and ws is not None and c is not None:
    result = solve(vs, ws, c)

print result
