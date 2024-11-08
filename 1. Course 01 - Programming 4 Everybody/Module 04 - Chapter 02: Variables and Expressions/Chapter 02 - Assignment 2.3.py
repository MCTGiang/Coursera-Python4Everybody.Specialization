# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.

# Prompt user for hours and rate per hour
hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")
# Convert inputs to 
hours = float(hours)
rate = float(rate)
# Calculate gross pay 
gross_pay = hours * rate
# Display the result 
print("Pay:", gross_pay)
