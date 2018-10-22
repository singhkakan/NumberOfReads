#!/bin/python/
import fileinput
import re
import sys
count = 0
input = raw_input("\n Input your file ")
f = open('%s.txt' % input, 'r')
y = open('output.txt', 'w')
content = f.read().split()
for line in content:
    read = re.findall('^([ACGNT]{6,})', line)
    if read != []:
        read_length = len(read[0])
        count = count + 1
        y.write("%s\n" % read_length)
f.close()
y.close()

print "There are", count, " reads in the file"
