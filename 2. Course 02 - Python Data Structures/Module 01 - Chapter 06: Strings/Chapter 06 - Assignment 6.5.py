# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
 # Find the position of the colon
pos = text.find(':')
# Slice from the position after the colon to the end and strip any extra spaces
number_str = text[pos+1:].strip()  
# Convert the extracted string to a floating-point number
number = float(number_str)
print(number)
