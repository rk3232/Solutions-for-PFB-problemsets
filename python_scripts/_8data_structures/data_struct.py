#!/usr/bin/env python3

import sys
import re

### Data structures###


#PS1: take multi-FASTA Python_08.fasta from usr.input and calc. nt composition into data structure
#print seq\tA_count\tT_count\tG_count\tC_count

#input fasta file from usr input
fasta_input = sys.argv[1]
print('User provided file: ',fasta_input)

###
#test with Python_07.fasta (smaller file)
###

#First load fasta into fasta dictionary

#fasta_dictionary with header:sequence
#gene_ID dictionary with header:description
fasta_dict = {}
header = ''
description = ''
gene_info = [] 
sequence = ''
with open(fasta_input, 'r') as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		if re.search(r'^>', line):
			for obj in re.finditer(r'^>(\S*)\s(.*)', line):
				header = obj.group(1)
				description=obj.group(2)
				gene_info = [description, sequence]
				fasta_dict[header]=gene_info
		else:
			sequence = line
			fasta_dict[header][1]+=sequence			
print(fasta_dict)

#for each seq, count and add dictionary to list gene_info.append{nt:nt_count}

#seq nt nt_count:
#define nt and nt_count
#nt_dict[nt] = nt_count
nt= ''
nt_count = []

for seq in fasta_dict[header][1]:
	print(seq)	
	

#ultra_fasta = {}





