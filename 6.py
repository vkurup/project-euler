#!/usr/bin/env python2

# find difference between sum of squares of the first 100 natural
# numbers and the square of the sum of those numbers

def sum_squares(n):
    result = 0
    for i in range(1,n+1):
        result += i*i
    return result

def square_of_sums(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result * result

def difference(n):
    return square_of_sums(n) - sum_squares(n)

print difference(100)

