#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

filename = sys.argv[1]

#hydrophobic region
def hydrphob(seq,w,t):
	for i in range(len(seq) +1 -w):
		sseq = seq[i:i+w]
		if kd(sseq) > t and "P" not in sseq:
			return True
	return False

def kd(seq):
	k = 0
	for aa in seq:
		if aa == "I": k += 4.5
		if aa == "V": k += 4.2
		if aa == "L": k += 3.8
		if aa == "F": k += 2.8
		if aa == "C": k += 2.5
		if aa == "M": k += 1.9
		if aa == "A": k += 1.8
		if aa == "G": k += -0.4
		if aa == "T": k += -0.7
		if aa == "S": k += -0.8
		if aa == "W": k += -0.9
		if aa == "Y": k += -1.3
		if aa == "P": k += -1.6
		if aa == "H": k += -3.2
		if aa == "E": k += -3.5
		if aa == "Q": k += -3.5
		if aa == "D": k += -3.5
		if aa == "N": k += -3.5
		if aa == "K": k += -3.9
		if aa == "R": k += -4.5
	return k / len(seq)

for name, seq in read_fasta(sys.argv[1]):
	nterm = seq[0:30]
	after = seq[30:len(seq)]
	if hydrphob(nterm,8,2.5) and hydrphob(after,11,2.0):
		print(name)


"""
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
