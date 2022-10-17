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
	nuc_bigkey= 'nt_counts'
	nt_key ={}
	nt_make = {nuc_bigkey:nt_key}
	print(nuc_bigkey, nt_key)
	for nt in inner_seq:
		if nt in nt_key:
			nt_key[nt]+=1
		else:
			nt_key[nt]=1
		fasta_dict[gene_key]['nt_count']=nt_key
#	gene_key[nt_key]+=nt #this doesn't workt
	print(nt_key)
print(fasta_dict)

#print in proper format
for gene_key in fasta_dict:
	nt_count= fasta_dict[gene_key]['nt_count']
	print(gene_key, nt_count)
				

#########reading frames

#codon_dict[gene_key]=codon_split

#read through each gene sequence in dict
codon_frame1={}
for gene_key in fasta_dict:

	#define sequence to read through, string you can split out 
	seq_input = fasta_dict[gene_key]['seq']
#	print(f'Input sequence: {seq_input}')

	#define dictionary for each gene_key
	codon_list = []
	codon_frame1[gene_key]=codon_list
#	print(f'framework for codon dict: {codon_frame1}')
	
	#for each set of 3 nt, add as obj in codon_list
	for seq in re.finditer(r'(.{3})', seq_input):
#		print(f'codon temp var: {seq}')
		temp_codon=seq.group(0)
#		print(f'defined temp_codon: {temp_codon}')	
		codon_list.append(temp_codon)
	#	print(f'for {gene_key} these are codons in frame1: {codon_list}')

#join list to strings with space seperator
	
	#define codon list 
	temp_codonlist = codon_frame1[gene_key]

	#join
	codon_frame1[gene_key] = '\t'.join(temp_codonlist)

	#print nicely
	print_codons = f'{gene_key} codons in reading frame 1 are: {codon_frame1[gene_key]}'
	print(print_codons)

#print to output file 

#print(codon_frame1)
	





