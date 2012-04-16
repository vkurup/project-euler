#!/usr/bin/env python2

# Calculate the sum of primes below 2,000,000

def sum_primes_below(n):
    sum = 0
    possibles = range(2,n)
    while len(possibles) > 0:
        next_prime = possibles[0]
        sum += next_prime
        possibles = [i for i in possibles if i%next_prime != 0]
    return sum

print sum_primes_below(10)
print sum_primes_below(2000000)



