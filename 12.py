#!/usr/bin/env python2

# triangle numbers: 1, 3, 6, 10, 15, 21, 28, 36, 45
# What is the value of the first triangle number to have over 500
# divisors?
import math

def divisors(n):
    "Return all factors of n"
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sorted(set(divisors))

def odd(n):
    return n%2 != 0

def first_triangle_with_n_divisors(n):
    "Return first triangle number with greater than n divisors"
    length = 0
    i = 1
    next_triangle = 1
    while length <= n:
        i += 1
        next_triangle += i
        if odd(next_triangle): continue
        length = len(divisors(next_triangle))
    return next_triangle

print "answer = ", first_triangle_with_n_divisors(500)



