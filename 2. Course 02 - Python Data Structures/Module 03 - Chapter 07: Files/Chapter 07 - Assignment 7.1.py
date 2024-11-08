# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name

fname = input("Enter file name: ")
try:
    # Open the file
    with open(fname, 'r') as file:
        # Read through the file line by line
        for line in file:
            # Print each line in uppercase
            print(line.upper().strip())
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
