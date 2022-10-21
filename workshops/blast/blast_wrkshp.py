#!/usr/bin/env python3

import sys
import pandas as pd
import re
import os

###Blast workshop###

#Define standard inputs



sys.argv = sys.argv[1:]

if (len(sys.argv)== 2):
	aa_input = sys.argv[1]
	matrix_input = sys.argv[2]

	#translate stdinput to filename
	file_path = "./ssearch_files"
	files_all= os.listdir(file_path) #this is a list of file names
	print(file_path,files_all)
	file_name = file_path+'/ss_rand5-'+aa_input+'_v_qfo_'+matrix_input+'.txt'
	print(file_name)

	#Take input, read in associated file
	og_table = pd.read_table(file_name, sep = '\t', comment = '#')
	print(og_table)

	#pull out perc_id and align_len and save to new value
	value_table = og_table.iloc[:,[2,3]]
	value_table.columns = ['Percent ID', 'Alignment Length']
	print(value_table)

### Do this but now with a nice loop to do it for all of them

else:
	aa_input = '*'
	matrix_input = '*'
	print(aa_input, matrix_input)

	#file names 
	file_path = "./ssearch_files"
	files_all= os.listdir(file_path) #this is a list of file names
	print(file_path,files_all)

	list_with_dfs = []
	#for file in list of files, open and read into df
	for file in files_all:
		list_with_dfs = pd.concat(map(pd.read_table,file))
	#	print(f'file is {file}')
	#	temp_df = pd.read_table(file, sep='\t', comment = '#')
	#	list_with_dfs.append(temp_df)
	print(list_with_dfs)

