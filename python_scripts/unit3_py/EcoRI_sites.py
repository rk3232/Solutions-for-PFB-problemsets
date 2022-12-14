#!/usr/bin/env python3
import sys

#CL input
site_input = sys.argv[1]

#make uppercase
og_seq = site_input.upper()

if 'GAATTC' in og_seq:
	print('For your input, EcoRI site is present')
	print(f'EcoRI site starts at position: {og_seq.index("GAATTC")} and ends at position: {og_seq.index("GAATTC") + 6}')
else:
	print('EcoRI site not present in your sample')

#test
seq1 = 'CCCTGTGGAATTCGTCAAG'

if 'GAATTC' in seq1:
	print(f'For {seq1}, EcoRI site is present')
	print(f'EcoRI site starts at position: {seq1.index("GAATTC")} and ends at position: {seq1.index("GAATTC") + 6}') 
else:
	print('EcoRI site not present')

#EcoRI: G AATT C or C TTA G


