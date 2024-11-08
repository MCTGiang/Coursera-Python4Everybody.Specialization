# Open the file romeo.txt and read it line by line
# For each line, split the line into a list of words using the split() method. The program should build a list of words.
# For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Initialize an empty list to store unique words
unique_words = []
# Input file name
fname = input("Enter file name: ")
try:
    # Open the file
    with open(fname, 'r') as file:
        for line in file:
            # Split the line into words
            words = line.split()
            # Check each word in the line
            for word in words:
                # If the word is not already in the list, append it
                if word not in unique_words:
                    unique_words.append(word)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
# Sort the list of unique words
unique_words.sort()
# Print the sorted unique words
print(unique_words)
