#!/usr/bin/env python3
import sys

num_input = int(sys.argv[1])
even_num = num_input%2 
divide_3 = num_input%3

if num_input > 0 :
	if num_input < 50:
		if even_num == 0 :
			print(num_input, 'is less than 50 and is even')
	elif num_input > 50:
		if divide_3 == 0:
			print(num_input, 'is greater than 50 and divisible by 3')
	elif num_input == 50:
		print(num_input, 'is 50')
elif num_input < 0 :
	print('negative')
else:
	print('is 0')
