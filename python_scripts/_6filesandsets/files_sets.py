#!/usr/bin/env python3

#### File input/output and sets

#Make a set two ways
#with set()
set1 = set('ACGCGCTA') #this one only kept unique character as separate strings
set2 = {'ACGCGCTA'} #this one made a set with one unchanged string bc this isn't making a set with individual elements, it thinks this string is a whole unique element

print(f'set1={set1},set2= {set2}')

#Find the intersection, difference, union, symmetrical difference btwn two sets:

setAlist = ('3 14 15 9 26 5 35 9')
setBlist = ('60 22 14 0 9')
setA= set(setAlist.split()) #split string by white space and make a set
setB=set(setBlist.split())

print(setA, setB)

#Find setA/B intersection
print(setA & setB)

#difference, in setA, not setB
print(setA - setB)

#union, all of them, unique
print(setA|setB)

#symmetrical difference, not shared
print(setA^setB)

### DNA set
#make set with DNA seq
dna_set = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC')
print(f'dna_set: {dna_set}')

###nucleotide composition
#determine unique chars
og_seq = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'

unique_seq = set(og_seq)
print(f'Unique chars in {og_seq} are {unique_seq}')

#iterate over each unique and count number in seq
#store each count in dictionary
#calculate and report nucleotide comp and gc content
seq_comp = {}
for chars in unique_seq:
	seq_comp[chars] = og_seq.count(chars)

print(seq_comp)

#calculate and report nucleotide comp and gc content
GC_comp = seq_comp['G'] + seq_comp['C']
total_len = len(og_seq)

print(f'GC content is {GC_comp/total_len}')

######Read/write to file#####

#for file Python_06.txt
#open and read contents
#make each line uppercase
#print each line to stdout (print())

with open("Python_06.txt", "r") as txt_file: #open and read
	read_txt = txt_file.read()

print(read_txt) 

#make upper
read_txt_upper = read_txt.upper()
print(read_txt_upper)
petty_upper = open("lyrics_upper.txt", "w")
petty_upper.write(read_txt_upper)
petty_upper.close()
print('wrote lyrics uppercase to lyrics_upper.txt')

###Seq file:
# open, print reverse comp, 
#format: seqName\tsequence\n
#print: <seqName \n reverse complement: \n sequence
#capture stdout into outputfile

#test first
#make a test file
test_seq = 'ATTACGTCCTG'
test_outfile= open('test_seq.txt', 'w') #make a writing file
test_outfile.write(test_seq)
test_outfile.close()
print('wrote sample to test_seq.txt')

#read to check
with open('test_seq.txt', 'r') as test_check:
	test_read = test_check.read()
print(test_read)

#make reverse complement of test_read w/ format
#complement 
test_Aa = test_read.replace('A', 'a')
test_TA = test_Aa.replace('T', 'A')
test_aT = test_TA.replace('a', 'T')
test_Gg = test_aT.replace('G', 'g')
test_CG = test_Gg.replace('C', 'G')
test_gC = test_CG.replace('g', 'C')

test_revcomp = test_gC[::-1] #reverse the list

#make test_read a dictionary
test_dict= {}
test_dict={'seq1':test_seq, 'seq2':'AGAGATTC', 'seq3':'GCTCAGT'}
print(f'start dictionary: {test_dict}')

#make the values in a dictionary lowercase
small_seq = {}
for gene in test_dict:
	seq=test_dict[gene]
	small_seq[gene] = seq.lower()
print(f'lower case dictionary: {small_seq}')

#make dictionary of complements
comp_seq = {}
for gene in small_seq:
	#print(gene)
	seq = small_seq[gene]
	#print(seq) < this really helps be sure I'm defining things well!!!
	comp_seq[gene]=seq.replace('a', 'T').replace('t','A').replace('g','C').replace('c', 'G')
	print(comp_seq[gene])
print(comp_seq)

revcomp_seq = {}
for gene in comp_seq:
	seq = comp_seq[gene]
	revcomp_seq[gene] = seq[::-1]
print(revcomp_seq)

##for real!
#open/read Python_06.seq.txt into a dictionary 
seq_dict= {}
with open('Python_06.seq.txt', 'r') as seq_object:
	for line in seq_object:
		line = line.rstrip()
		gene_id,seq = line.split()
		seq_dict[gene_id] = seq
#print(seq_dict)

# make lowercase and replace with complement
full_comp_seq = {}
for gene in seq_dict:
#	print(gene)
	seq = seq_dict[gene]
#	print(f'this is seq {seq}')
	full_comp_seq[gene] = seq.lower().replace('a','T').replace('t', 'A').replace('g','C').replace('c','G')
print(full_comp_seq)

#make reverse
full_revcomp_seq={}
for gene in full_comp_seq:
	seq=full_comp_seq[gene]
	full_revcomp_seq[gene] = seq[::-1]
print(full_revcomp_seq)
 
#print as fasta format
for k,v in full_revcomp_seq.items():
	print('>' + k + '\n' + v)

		


 












