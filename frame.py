#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

p = 0
n = 0
"""
#single loop
for c in dna:
	print(p, n, c)
	p += 1
	n += 1
	if (n > 2):
		n = 0
"""
#nested loop
for c in dna:	
	while n >= 0:
		print(p, n, c)
		n += 1
		p += 1
		if (n > 2):
			n = 0
		if (p >= 1):
			break
	

"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
