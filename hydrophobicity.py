#!/usr/bin/env python3

import argparse
import biotools


# Write a program that computes hydrophobicity in a window
# Let the user choose the method (see below)
# https://en.wikipedia.org/wiki/Hydrophilicity_plot
# https://en.wikipedia.org/wiki/Hydrophobicity_scales

parser = argparse.ArgumentParser(
	description='hydrophobicity calculator')
parser.add_argument('--input', required=True, type=str,
	metavar='<path>', help='fasta file')
parser.add_argument('--window', required=False, type=int, default=15,
	metavar='<int>', help='Window size, default [%(default)i]')
parser.add_argument('--method', required=False, type=int, default =0,
	metavar='<int>', help='Calculation Method, KD [0], IS [1], OS, IS+OS, CC, default [%(default)s]')
arg = parser.parse_args()

kdscale = {'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
       'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
       'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
       'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
ISscale = { 'A': 0.17,'R':0.81,'N':0.42,'D': 1.23,'C':-0.24,
        'Q': 0.58,'E':2.02,'G':0.01,'H': 0.96,'I':-0.31,
        'L':-0.56,'K':0.99,'M':-0.23,'F':-1.13,'P':0.45,
        'S': 0.13,'T':0.14,'W':-1.85,'Y':-0.94,'V': 0.07 }

def cal_hydro(aastring, method):
	scale = None
	if method == 0:
		scale = kdscale
	elif method == 1:
		scale = ISscale
	hydro_score = 0
	for aa in aastring:
		if aa in scale:
			hydro_score += scale[aa]
	return hydro_score

for name, aastring in biotools.read_fasta(arg.input):
	aastring = aastring.upper()
	if aastring[-1] == '*':
		aastring = aastring[0:-1]
	for i in range(0, len(aastring) - arg.window + 1):
		win = aastring[i:i+arg.window]		
		print(i, cal_hydro(win,arg.method))
"""
python3 hydrophobicity.py --input proteins.fasta.gz --window 11 --method kd
"""
