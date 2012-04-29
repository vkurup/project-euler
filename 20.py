#!/usr/bin/env python2

# sum of digits in 100!
import math

s = str(math.factorial(100))
print sum(int(char) for char in s)
