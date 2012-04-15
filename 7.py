#!/usr/bin/env python2

# What is the 10001st prime
import math

def nth_prime(n):
    i = 1
    prime_count = 0
    while prime_count < n:
        i += 1
        if is_prime(i):
            prime_count += 1
    return i

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print nth_prime(10001)

