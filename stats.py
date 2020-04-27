#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

scores = []
for line in fileinput.input():
	if line.startswith('#'): continue
	scores.append(float(line))
	mean = sum(scores) / len(scores)
	count = len(scores)
	val = sum([(i - mean) ** 2 for i in scores]) / len(scores)
	stddev = sqrt(val)
scores.sort()
minimum = scores[0]
maximum = scores[-1]
if len(scores) % 2 == 0:
	median1 = scores[len(scores) // 2]
	median2 = scores[len(scores) // 2 - 1]
	median = (median1 + median2 ) / 2
else:
	median = scores[len(scores) // 2]
		

#ouput
print(f'Count: {count}')
print(f'Minimum: {minimum}')
print(f'Maximum: {maximum}')
print(f'Mean: {mean}')
print(f'Std. dev: {stddev:.3f}')
print(f'Median: {median}')


"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
