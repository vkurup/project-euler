#!/usr/bin/env python2

# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n). 
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable
# pair and each of a and b are called amicable numbers. 

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
#22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
#284 are 1, 2, 4, 71 and 142; so d(284) = 220. 

# Evaluate the sum of all the amicable numbers under 10000.
import math

def d(n):
    return sum(divisors(n)) - n

def divisors(n):
    "Return proper divisors of n"
    divisors = []
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
    return sorted(divisors)

def sum_amicable_below_n(n):
    "Return sum of all amicable numbers below n"
    amicable = []
    for i in range(1,10000):
        if d(d(i)) == i and i != d(i):
            amicable.append(i)
    return sum(amicable)

print sum_amicable_below_n(10001)
        

