#!/usr/bin/env python2

# Calculate the sum of primes below 2,000,000
import math

def sum_primes_below(n):
    prime = [True] * n
    next = 3
    sum = 2
    while next < n:
        if prime[next]:
            sum += next
            # amazing how much difference step makes
            for i in range(next,n,next):
                prime[i] = False
        next += 2
    return sum

print sum_primes_below(2000000)
