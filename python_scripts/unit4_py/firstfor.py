#!/usr/bin/env python3

#use a for loop to iterate through and print only even values
randonums = [101,2,15,22,95,33,2,27,72,15,52]
randonums_iter = iter(randonums)

evennums=[]
for nums in randonums_iter:
	if nums%2 == 0:
		evennums.append(nums)
print(f'From {randonums}, {evennums} are even')

#sort all
sortnums= randonums.copy()
sortnums.sort()
print(sortnums)

#print all individually
for x in sortnums:
	print(x)

#sum of even nums
evensum = sum(evennums)
print(f'Sum of {evennums} is {evensum}')

#odd nums
oddnums = []
for nums in sortnums:
	if nums%2 != 0:
		oddnums.append(nums)
print(f'These {oddnums} are odd')

oddsum = sum(oddnums)
print(f'sum of {oddnums} is {oddsum}')

####
#range + for loop for list of 0 to 99
bignums99 = list(range(100))
print(bignums99)

#for range from 0-99
for nums in range(100):
	print(nums)

#for range from 1 to 100
for nums in range(100):
	print(nums + 1)

####

#list comprehension to print range to 100
numsto100= [num for num in range(101)]

#remove 0
numsto100.pop(0) 

#convert to string for join
to100_str = [str(num) for num in numsto100]

#join with enter between
joinnums100 = '\n'.join(to100_str)



print(joinnums100)



