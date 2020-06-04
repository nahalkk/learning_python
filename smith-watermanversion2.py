#!/usr/bin/env python3

import argparse
import biotools
import random

# Smith-Waterman algorithm for local alignment 

parser = argparse.ArgumentParser(
	description='computes alignment score between nucleotide sequences')
# required arguments
parser.add_argument('--input', required=True, type=str,
	metavar='<str>', help='fasta file')

# optional arguments with default parameters
parser.add_argument('--match', required=False, type=int, default=1,
	metavar='<int>', help='match score [%(default)i]')
parser.add_argument('--mismatch', required=False, type=int, default=-1,
	metavar='<int>', help='mismatch score [%(default)i]')
parser.add_argument('--gap', required=False, type=int, default=-1,
	metavar='<int>', help='gap score [%(default)i]')


seq = "GCGAGGTTATATGATGCTGTGAT"
seq2 = "CGCTCCAATAGAATAC"

def calc(matrix, x, y):
	if seq[x - 1] == seq2[y - 1]:
		score = arg.match
	else:
		score = arg.mismatch
	diagonal = matrix[x - 1][y - 1]
	up = matrix[x-1][y] +arg.gap
	left = matrix[x][y-1]+arg.gap
	return (0, diagonal, up, left)

def score_matrix(rows, columns):
	matrix_score = [[0 for column in range(columns)] for row in range(rows)]
	maxscore = 0
	maxposition = None
	for i in range(1, rows):
		for j in range(1, columns):
			sscore = calc(thescore_matrix, i, j)
			if sscore > maxscore:
				maxscore = sscore
				maxposition = (i,j)
			thescore_matrix[i][j] = sscore
	assert(maxposition is not None)
	return matrix_score, maxposition

stp = 0
diagonal2 = 1
up2 = 1
left2 = 2

def align_trace(matrix_score, startingpos):
	align1 = []
	align2 = []
	x,y = startingpos
	m = move(matrix_score, x,y)
	while m != stp:
		if m == diagonal2:
			align1.append(seq[x-1])
			align2.append(seq2[y-1])
			x -= 1
			y -= 1
		elif m == up2:
			align1.append(seq[x-1])
			align2.append(seq2[y-1])
			x -= 1
		else:
			align1.append('-')
			align2.append('-')
			y -= 1
	align1.append(seq[x-1])
	align2.append(seq2[y-1])
	return x-1, ''.join(reversed(align1)), y-1, ''.join(reversed(align2))
			
def move(matrix_score, x,y):
	diagonal = matrix_score[x-1][y-1]
	up = matrix_score[x-1][y]
	left = matrix_score[x][y-1]
	if diagonal >= up and diagonal >= left:
		if diagonal != 0:
			return diagonal1
	if up > diagonal and up >= left:
		if up != 0:
			return up2
	else:
		if left != 0:
			return left2
		else: return stop			

def alignment(align1, align2):
	identicals = 0
	mismatches = 0
	gaps = 0
	alignment_str = []
	for i in range(len(align1)):
		nt = align1[i]
		nt2 = align2[i]
		if nt == nt2:
			alignment_str.append('|')
			identicals += 1
		elif nt == '-' or nt2 == '-':
			alignment_str.append('')
			gaps += 1
		else:
			alignment_str.append(':')
			mistmatches += 1
	return ''.join(alignment_str), identicals, mismatches, gaps

seq == None
for name, seq2 in biotools.read_fasta(arg.input):
	dna1 = list(seq2)
	
	if seq == None:
		seq == seq2
		#print(seq2)
		continue 
	
	#matrix_score, startingpos = score_matrix(rows, columns)
	
	p1, align1, p2, align2 = align_trace(matrix_score, startingpos)
	align, identicals, gaps, mismatches = alignment(align1, align2)
	
	print(f'Score = {(identicals * arg.match)+(mismatches * arg.mismatch) +(gaps * arg.gap)}')	

		