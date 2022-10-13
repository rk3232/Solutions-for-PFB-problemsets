#!/usr/bin/env python3

### splitting strings into a list ###

#define OG string
taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)

print(taxa[1])

#split string into species
species = taxa.split(', ')
print(species)
print(species[1])
print(f'This {type(species)} is the type of data/variable')

#sort alphabetically
sort_species = sorted(species)
print(sort_species)

#sort by word length
len_species = sorted(species, key=len)
print(len_species)


