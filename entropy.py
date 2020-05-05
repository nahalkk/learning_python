#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math

p = []
sum = 0
for line in fileinput.input():
	if line.startswith('#'): continue
	vals = line.split()
	v = float(vals[1]) 
	assert(v >= 0 and v <= 1)
	sum += v
	p.append(v)
assert(math.isclose(sum, 1))

h = 0
for i in range(len(p)):
	h -= p[i] * math.log2(p[i])
print('%.3f' % (h))

"""
python3 entropy.py nucleotides.txt
1.846
"""
