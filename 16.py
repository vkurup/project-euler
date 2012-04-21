#!/usr/bin/env python2

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def sum_2_to_n(n):
    "Return sum of digits of result of 2 to nth power"
    return sum([int(digit) for digit in str(2**n)])

print sum_2_to_n(1000)

