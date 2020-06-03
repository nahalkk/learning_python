#!/usr/bin/env python3

import argparse
import biotools
import gzip
import math

# Write a program that masks areas of low complexity sequence
# Use argparse for command line arguments (see example below)
# Use read_fasta() from biotools.py

parser = argparse.ArgumentParser(
	description='Low complexity sequence masker.')
# required arguments
parser.add_argument('--input', required=True, type=str,
	metavar='<path>', help='fasta file')

# optional arguments with default parameters

parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='optional integer argument [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.1,
	metavar='<float>', help='entropy threshold [%(default)f]')
# switches
parser.add_argument('--lowercase', action='store_true',
	help='report lower case instead of N')
# finalization
arg = parser.parse_args()

def entropy(seq):
	a = 0
	c = 0
	g = 0
	t = 0 
	for nt in seq: 
		if nt == 'A': a += 1
		if nt == 'C': c += 1
		if nt == 'G': g += 1
		if nt == 'T': t += 1
	total = a + c + g + t
	if total == 0:
		return None
	pa = a / total
	pc = c / total
	pg = g / total
	pt = t / total
	h = 0
	if a != 0: h -= pa * math.log2(pa)
	if c != 0: h -= pc * math.log2(pc)
	if g != 0: h -= pg * math.log2(pg)
	if t != 0: h -= pt * math.log2(pt)
	return h

	
for name, seq in biotools.read_fasta(arg.input):
	dna = list(seq)
	for i in range(len(seq)-arg.window+1):
		sseq = seq[i:i+arg.window]
		if entropy(sseq) < arg.threshold: 
			# exchange all letters in the window for N or lowercase letters
			for j in range(i,i + arg.window):
				if arg.lowercase:
					if   dna[j] == 'A': dna[j] = 'a'
					elif dna[j] == 'C': dna[j] = 'c'
					elif dna[j] == 'G': dna[j] = 'G'
					elif dna[j] == 'T': dna[j] = 't'
				else:    dna[j] = 'N'
	print(f'{name}')
	print(''.join(dna))
			
	#join all the letters of the list into a string for output

"""
python3 entropy_filter.py --help
usage: entropy_filter.py [-h] --input <path> [--window <int>]
                         [--threshold <float>] [--lowercase]

Low complexity sequence masker.

optional arguments:
  -h, --help           show this help message and exit
  --input <path>       fasta file
  --window <int>       optional integer argument [15]
  --threshold <float>  entropy threshold [1.100000]
  --lowercase          report lower case instead of N


python3 entropy_filter.py --input genome.fa.gz | head -20
>I
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAAGCCTAA
GCCTAAGCCTAAAAAATTGAGATAAGAAAACATTTTACTTTTTCAAAATTGTTTTCATGC
TAAATTCAAAACNNNNNNNNNNNNNNNAAGCTTCTAGATATTTGGCGGGTACCTCTAATT
TTGCCTGCCTGCCAACCTATATGCTCCTGTGTTTAGGCCTAATACTAAGCCTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAA
GCCTAAGACTAAGCCTAAGACTAAGCCTAATACTAAGCCTAAGCCTAAGACTAAGCCTAA
GCCTAAAAGAATATGGTAGCTACAGAAACGGTAGTACACTCTTCTGNNNNNNNNNNNNNN
NTGCAATTTTTATAGCTAGGGCACTTTTTGTCTGCCCAAATATAGGCAACCAAAAATAAT
TGCCAAGTTTTTAATGATTTGTTGCATATTGAAAAAAACANNNNNNNNNNNNNNNGAAAT
GAATATCGTAGCTACAGAAACGGTTGTGCACTCATCTGAAANNNNNNNNNNNNNNNNNNN
NNGCACTTTGTGCAGAATTCTTGATTCTTGATTCTTGCAGAAATTTGCAAGAAAATTCGC
"""
