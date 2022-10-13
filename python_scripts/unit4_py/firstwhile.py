#!/usr/bin/env python3

import math
import sys
### while loops###

#print 1: 100
num = 0
while num < 101:
	print(num)
	num+=1
print('done')



#test
n=0
mathlist5 = ['']
#print 5!
while n < 4:
	k=(5-n)
	mathlist5.append(k)
	print(mathlist5)
	n+=1	
print(mathlist5)

mathlist5.pop(0)
print(mathlist5)
fact5 = math.prod(mathlist5)
print(f'the factorial of 5 is {fact5}')

#1000!
factorial = 1000
multiplier = factorial - 1

while multiplier > 0:
	factorial = (factorial * multiplier)
	multiplier-=1
print(factorial)
