#!/usr/bin/env python3

###Dictionaries and sets problem set 5###

#construct a dictionary of things
favethings_dict = {'color':'orange', 'tea':'oolong', 'flower':'sunflower'}
print(favethings_dict)

#print fave color
print(f'Favorite color: {favethings_dict["color"]}')

#print fave color with substitute variable
fave_color = 'color'
print(f'Favorite {fave_color} is {favethings_dict["color"]}')

#print fave tea
print(f'Favorite tea is {favethings_dict["tea"]}')

#add fave animal to dictionary
fave_animal = 'oppossum'
favethings_dict['animal'] = fave_animal
print(f"Fave animal is {favethings_dict['animal']}")

#take input from command line for favorite number
ask_fave_num = input("What is your favorite number? ") #input stops and asks for standard input, writes to variable
favethings_dict['number'] = ask_fave_num
print(f'Your favorite number is {favethings_dict["number"]}')

#change animal
favethings_dict['animal'] = 'elephant'

#ask for favorite animal
ask_animal = input("What is your favorite animal? ")
favethings_dict['animal'] = ask_animal

#print all key:values
print(f'These are your favorite things:')
for thing in favethings_dict:
	print(f'{thing}: {favethings_dict[thing]}')









