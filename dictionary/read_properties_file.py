import os

# define dictionary
dict={}

# define file
prop_file = 'script.properties'

# open file to be read it
with open(prop_file, 'rt') as file:

    # loop through lines and add to dictionary
    for line in file:
        (key, val) = line.split('=')
        dict[key] = val.strip() # don't forget to strip out the new line characters

# print out all lines in dictionary
for key, val in dict.iteritems():
    print key, '=', val

# get dictionary item by key
print "I think it's way too hot so", dict['KEEP_COOL'], "and don't sweat it."
