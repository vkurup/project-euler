#!/usr/bin/env python2

f = open("names.txt")
names = f.read()
f.close()
names = sorted([name.strip('"') for name in names.split(',')])

letters = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'

score = 0
for position_score,name in enumerate(names,1):
    letters_score = sum(letters.index(char) for char in name)
    score += position_score * letters_score
print score
