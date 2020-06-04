#!/usr/bin/env python3
import random
import fileinput
import json

puncs =  '.,?!:;-*"_()[]{}<>/1234567890—“”’‘–' # you may need to add more
spaces = ' ' * len(puncs)

first = {}
second = {}
third = {}

for rawline in fileinput.input():

	# convert to lowercase
	lower = rawline.lower()
	
	# convert punctuation to spaces
	table = lower.maketrans(puncs, spaces)
	line = lower.translate(table)
	
	# start work here
	for word in line.split():
		modifyword = word + '*'
		letter = modifyword[0]
		if letter in first: 
			first[letter] += 1
		else:
			first[letter] = 1
		for i in range(1, len(modifyword)):
			a1 = modifyword[i-1]
			a2 = modifyword[i]
			if a1 not in second: 
				second[a1] = {}
			if a2 not in second[a1]: 
				second[a1][a2] = 1
			else: 
				second[a1][a2] += 1
		for i in range(2, len(modifyword)):
			a1 = modifyword[i-2]
			a2 = modifyword[i-1]
			a3 = modifyword[i]
			if a1 not in third:
				third[a1] = {}
			if a2 not in third[a1]:
				third[a1][a2] = {}
			if a3 not in third[a1][a2]:
				third[a1][a2][a3] = 1
			else:
				third[a1][a2][a3] += 1
		#print(word)
#a pool for first letter
pool = []
for letter in first:
	for i in range(first[letter]):
		if first[letter] > 1:
			pool.append(letter)
#a pool for second letter
pool2 = {}
for a1 in second:
	stuff = []
	for a2 in second[a1]:
		for i in range(second[a1][a2]):
			stuff.append(a2)
		pool2[a1] = stuff
#a pool for third letter
pool3 = {}
for a1 in third:
	pool3[a1] = {}
	for a2 in third[a1]:
		stuff = []
		for a3 in third[a1][a2]:
			for i in range(third[a1][a2][a3]):
				stuff.append(a3)
		pool3[a1][a2] = stuff
#choosing letters
while True:
	word = []
	word.append(random.choice(pool))
	word.append(random.choice(pool2[word[0]]))
	if word[1] == '*':
		continue
	i = 2
	while True:
		b2 = word[i-2]
		b1 = word[i-1]
		next = random.choice(pool3[b2][b1])
		i += 1
		if next == '*':
			break
		word.append(next)
	if 12 > len(word) > 3:
		words = ''.join(word)
		print(words.capitalize())		
		




