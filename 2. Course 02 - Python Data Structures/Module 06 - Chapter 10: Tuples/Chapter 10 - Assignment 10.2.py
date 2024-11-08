#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#File handling
fname = input("Enter file name: ")
if len(fname)<1:
    fname = 'mbox-short.txt'
hand = open(fname)

# Creating the Counts Dictionary
counts = dict()

# Loop through the Lines
for line in hand:
    if line.startswith('From '):
        wrds = line.split()
        time = wrds[5]
        hours = time.split(':')
        hour = hours[0]
        counts[hour] = counts.get(hour,0)+1

# Sorting and Printing
lst = sorted(counts.items())
for hour,count in lst:
    print (hour, count)
