#!/usr/bin/env python2

# find pythagorean triplet where a + b + c = 1000
# return a * b * c

def pythagorean_triplet_1000():
    for a in range(1,1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if a*a + b*b == c*c:
                    if a + b + c == 1000:
                        return a * b * c

print pythagorean_triplet_1000()
