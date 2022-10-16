#!/usr/bin/env python3

import re

#### read in file Python_07_nobody.txt and find every occurance of 'Nobody'
#read file
with open('Python_07_nobody.txt', 'r') as nobody_read:
	for line in nobody_read:
		nobody_str=nobody_read.read()

print(nobody_str)

#to find and report position use re.finditer(r'regex', var)
start_end = [] #makes a list for start and end positions
for hit in re.finditer(r'Nobody', nobody_str):
	start_end.append((hit.start(0),hit.end(0)))
print(f' Character positions of "Nobody": {start_end}')


#replace 'Nobody' with 'Lola'
thanks_Lola = re.sub(r'Nobody', 'Lola', nobody_str)
print(thanks_Lola)

######FASTA REGEX######

#read in fasta file Python_07.fasta
#read in file
gene_ID_header = ''
fasta_strings = {}
with open('Python_07.fasta', 'r') as read_fasta:
	for line in read_fasta:
		line = line.rstrip().strip()
		if re.search(r'^>(.*)', line):
			for obj in re.finditer(r'^>(\S*)\s(.+)', line):
				header = obj.group(1)
				print(header)
				description = obj.group(2)	
		else:
			fasta_strings[header]+=sequence
	
print(fasta_strings)

#to make this generalized to genomes, + seq strings together into a list then make a dictionary of lists




fasta_dict = {}
header = ''
sequence = ''
with open(fasta_input, 'r') as fasta_read:
	for line in fasta_read:
		line = line.rstrip()
		if re.search(r'^>', line):
			for obj in re.finditer(r'^>(\S*)\s', line):
        header = obj.group(1)
        fasta_dict[header]=sequence       
     else:
       sequence = line
       fasta_dict[header]+=sequence
 print(fasta_dict)




