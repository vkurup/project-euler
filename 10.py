#!/usr/bin/env python2

# Calculate the sum of primes below 2,000,000
import math

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def sum_primes_below_n(n):
    return sum(filter(is_prime,range(2,n)))

print sum_primes_below_n(2000000)
