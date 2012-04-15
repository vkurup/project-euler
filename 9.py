#!/usr/bin/env python2

# find pythagorean triplet where a + b + c = 1000
# return a * b * c

# 1. a2 + b2 = c2
# 2. a + b + c = 1000
#   substitute 1 into 2
# a + b + sqrt(a2 + b2) = 1000
# sqrt(a2 + b2) = 1000 - a - b
#   square both sides
# a2 + b2 = (1000 - a - b) (1000 - a - b)
# a2 + b2 = 1000 * 1000 - 1000a - 1000b - (1000a - a2 - ab) - (1000b - ab - b2)
# a2 + b2 = 1000 * 1000 - 1000a - 1000b - 1000a + a2 + ab - 1000b + ab + b2
# 0 = 1000 * 1000 - 2000a - 2000b + 2ab
# 2000a + 2000b - 2ab = 1000000
# 1000a + 1000b - ab = 500000

import math

def pythagorean_triplet_1000():
    for a in range(1,1000):
        for b in range(1,1000):
            if 1000*a + 1000*b - a*b == 500000:
                c = int(math.sqrt(a*a + b*b))
                return a * b * c

print pythagorean_triplet_1000()
