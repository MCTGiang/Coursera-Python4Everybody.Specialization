# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number

# Initialize variables for tracking the largest and smallest numbers
largest = None
smallest = None
while True:
    # Prompt the user for input
    num = input("Enter a number: ")
    # Check if the user wants to finish
    if num.lower() == "done":
        break
    # Try to convert the input to an integer
    try:
        num = int(num)
        # Update largest and smallest numbers
        if largest is None or num > largest:
            largest = num
        if smallest is None or num < smallest:
            smallest = num
    except ValueError:
        print("Invalid input")
# After the loop, print the results
if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers were entered.")
