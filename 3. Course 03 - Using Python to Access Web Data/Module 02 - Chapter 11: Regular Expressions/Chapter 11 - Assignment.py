# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

#Open the file
fname = input("Enter file name: ")
if len(fname)<1:
    fname = '11.3.txt'
hand = open(fname)

#Initialize Total Variable
tnum = 0

#Import regular expressions
import re

#Look for integers using the re.findall()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    #converting the extracted strings to integers and summing up
    for num in stuff:
        fnum = int (num)
        tnum = tnum + fnum
print (tnum)
