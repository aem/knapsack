"""
Solver for the popular knapsack problem.

USAGE: python knapsack.py '1,2,3,4,5' '5,4,3,2,1' 10
"""
import sys
from itertools import repeat


def print_2d_arr(arr):
    arr.reverse()
    for a in arr:
        s = ""
        for i in a:
            s += str(i) + "\t"
        print s


def solve_grid(g, w):
    ans = []
    cap = len(g) - 1
    item = len(g[0]) - 1

    while item > 0:
        if g[cap][item] != g[cap][item - 1]:
            ans.append(item)
            cap -= w[item - 1]
        item -= 1
    ans.reverse()
    return ans


def solve(values, weights, capacity):
    assert capacity > 0
    assert len(values) == len(weights)

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
                if weights[i - 1] > w or w - weights[i - 1] < 0:
                    grid[w][i] = grid[w][i - 1]
                else:
                    grid[w][i] = max(grid[w][i - 1],
                                     values[i - 1] + grid[w - weights[i - 1]][i - 1])

    solution = solve_grid(grid, weights)

    return solution, grid

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

print "Decision grid:"
print_2d_arr(result[1])
print "Solution:"
print result[0]
