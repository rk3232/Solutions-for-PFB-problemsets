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
gene = {}
#fasta_dict= {header:{desc:words, seq= sequence, {A:A_ ntcount,... }}}
description = ''
sequence = ''
desc = 'desc'
seq = 'seq'
with open(fasta_input, 'r') as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		if re.search(r'^>', line):
			for obj in re.finditer(r'^>(\S*)\s(.*)', line):
				gene = obj.group(1)
				description = obj.group(2)
				fasta_dict[gene]={desc:description, seq: sequence}
		else:
			sequence = line
			fasta_dict[gene][seq]+=sequence			
print(fasta_dict)

#for each seq, count and add dictionary to list gene_info.append{nt:nt_count}

#check length of sequences
for gene_key in fasta_dict:
#	print(fasta_dict[key])
	inner_seq = fasta_dict[gene_key]['seq']
	print(len(inner_seq))
	#print(len())

#for each gene in dictionary	
for gene_key in fasta_dict:
	inner_seq = fasta_dict[gene_key]['seq']
	nt_key= {}
	for nt in inner_seq:
		if nt in nt_key:
			nt_key[nt]+=1
		else:
			nt_key[nt]=1
#	gene_key[nt_key]+=nt #this doesn't workt
	print(nt_key)
print(fasta_dict)







