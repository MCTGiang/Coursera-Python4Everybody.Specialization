# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Dic to store:
email = {}
# Input file name:
fname = input("Enter file:")
try:
    # Open the file
    fhand=open(fname, 'r')
    with fhand as file:
        # Read the file line by line
        for line in file:
            # Check if the line starts with 'From ' and not 'From:'
            if line.startswith("From "):
                # Split the line into words
                words = line.split()
                # Increment the count
                sender = words[1]
                # Update the count for this sender
                email[sender] = email.get(sender, 0) + 1
except FileNotFoundError:
    print(f"File '{fname}' not found.")
# Close the file
fhand.close()
# Variables to track the most prolific committer
most_prolific_sender = None
highest_count = 0
# Find the sender with the highest message count
for sender, count in email.items():
    if count > highest_count:
        highest_count = count
        most_prolific_sender = sender
# Print the result
print(most_prolific_sender, highest_count)
