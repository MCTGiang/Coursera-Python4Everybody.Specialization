# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Initialize a count variable
count = 0
# Input file name
fname = 'mbox-short.txt'
try:
    # Open the file
    with open(fname, 'r') as file:
        # Read the file line by line
        for line in file:
            # Check if the line starts with 'From ' and not 'From:'
            if line.startswith("From ") and not line.startswith("From:"):
                # Split the line into words
                words = line.split()
                # Print the second word (email address)
                print(words[1])
                # Increment the count
                count += 1
except FileNotFoundError:
    print(f"File '{fname}' not found.")
# Print the total count of email addresses
print("There were", count, "lines in the file with From as the first word")
