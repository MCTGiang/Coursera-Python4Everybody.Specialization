# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and # compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
try:
    # Open the file
    with open(fname, 'r') as file:
        # Counter for the number of matching lines
        count = 0            
        # Accumulator for the total confidence values
        total_confidence = 0  
        # Read through the file line by line
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                # Extract the part of the line after the colon and convert to float
                confidence_value = float(line[line.find(":") + 1:].strip())
                # Accumulate the confidence value and increment the count
                total_confidence += confidence_value
                count += 1
             # Calculate the average confidence value if any lines were found
        if count > 0:
            average_confidence = total_confidence / count
            print("Average spam confidence:", average_confidence)
        else:
            print("No 'X-DSPAM-Confidence' lines found in the file.")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
