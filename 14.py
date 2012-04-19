#!/usr/bin/env python2

# For Collatz problem, which starting num under 1 million produces
# longest chain?

# even: n -> n/2
# odd : n -> 3n + 1
# 13: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

def next_collatz_number(n):
    if n%2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def collatz_chain(n, memo={}):
    "Return number of items in chain from n to 1, using collatz equation"
    if n == 1:
        return 1
    else:
        next = next_collatz_number(n)
        if next not in memo:
            memo[next] = collatz_chain(next, memo)
        return 1 + memo[next]

chains = [collatz_chain(i) for i in range(1,1000000)]
print chains.index(max(chains)) + 1

