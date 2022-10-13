#!/usr/bin/env python3

#make a script for inputing start and end values and printing from start to end

import sys

start_input = int(sys.argv[1])
end_input = int(sys.argv[2])


#make a list from start to end using command inputs with range()
trunc_list = list(range(start_input,(end_input+1)))
print(f'Numbers from {start_input} to {end_input}:')
for num in trunc_list:
	print(num)
print('end')

#only print if odd number
all_nums = trunc_list.copy()
odd_nums = []

#move odd nums into new list
for num in all_nums:
	if num%2 != 0:
		odd_nums.append(num)

#convert list to string for printing
odd_to_str = [str(num) for num in odd_nums]
odd_nums_join = ','.join(odd_to_str)
print(f'These are odd numbers from {start_input} to {end_input}:')
print(odd_nums_join)
	

###

#create list of and iterate through to print each obj
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for obj in dna_list:
	print(obj)

#print length \t sequence for each
for obj in dna_list:
	print(f'{len(obj)}\t{obj}')

###create a list of tuples with list comprehension from dna_list

#make tuples with len(obj) and obj
tuple_list = [(len(obj), obj) for obj in dna_list]
print(tuple_list)

#make tuple list print with index position
for obj in tuple_list:
	print(tuple_list.index(obj),'\t',obj, sep = '')

#same as above with f'string print
print('Index:\tlength:\tsequence:')
for obj in tuple_list:
		print(f' {tuple_list.index(obj)}\t{obj}')





