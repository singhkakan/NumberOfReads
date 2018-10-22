#!/bin/python/

# Importing the libraries
import fileinput
import re
import sys

# Initializing the count variable to count number of reads in a file
count = 0

# User will give the filename of the txt file that will be read
input = raw_input("\n Input your file ")

# File will be opened in read mode in variable f
f = open('%s.txt' % input, 'r')

# An empty text file is opened in write mode in variable y
y = open('output.txt', 'w')

# This block will read every second line with a step of 4 lines & save in variable read
content = f.readlines()
read = content[1::4]

# This loop will count the length of the string in each line of variable read (length of a read)
# The loop also creates a text file with the lengths of the reads (separated by new lines)
for line in read:
    count = count+1
    read_length = len(line)
    y.write("%s\n" % read_length)


f.close()
y.close()
print(type(line))
print "There are", count, " reads in the file"
