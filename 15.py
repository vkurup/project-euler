#!/usr/bin/env python2

# How many routes through a 20x20 grid?
# Start at top left
# go only right or down.

# 2x2 grid. Will take 4 moves to get from [0,0] to [2,2]
# Two moves right and two moves down. All correct routes will be 4
# moves, consisting of 2 rights and 2 downs, but in different orders.
# So, if there were 4 independent choices, all combinations of those 4
# choices would be 4! (4 factorial). But that would include some
# routes which are duplicates (where an R and another R are
# transposed). So, we have to divide that result by the product of the
# 'redundant' choices, so the final answer is:
#
# 4! / (2! * 2!), or more generally, for an NxN grid:
# (N*2)! / (N! * N!)
import math

def route_count(n):
    """Return number of possible routes in n-by-n grid, starting at
    top left, ending at bottom right, going only right or down (no
    backtracking)"""
    return math.factorial(n*2) / (math.factorial(n)*math.factorial(n))

print route_count(20)

