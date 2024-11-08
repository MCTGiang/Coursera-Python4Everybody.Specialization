### 1.	How are Python dictionaries different from Python lists?
    A. Python dictionaries are a collection and lists are not a collection
    B. Python lists store multiple values and dictionaries store a single value
    C. Python lists are indexed using integers and dictionaries can use strings as indexes
    D. Python lists can store strings and dictionaries can only store words
_Answer is C. Python lists are indexed using integers and dictionaries can use strings as indexes_
### 2.	What is a term commonly used to describe the Python dictionary feature in other programming languages?
    A. Closures
    B. Associative arrays
    C. Sequences
    D. Lambdas
_Answer is B. Associative arrays_
### 3.	What would the following Python code print out?
    stuff = dict()
    print(stuff['candy'])
Choose the correct answer:

    A. The program would fail with a traceback
    B. 0
    C. -1
    D. candy
_Answer is A. The program would fail with a traceback_
### 4.	What would the following Python code print out?
    stuff = dict()
    print(stuff.get('candy',-1))
Choose the correct answer:

    A. The program would fail with a traceback
    B. 0
    C. 'candy'
    D. -1
_Answer is D. -1_
### 5.	What is a common use of Python dictionaries in a program?
    A. Splitting a line of input into words using a space as a delimiter
    B. Sorting a list of names into alphabetical order
    C. Building a histogram counting the occurrences of various strings in a file
    D. Computing an average of a set of numbers
_Answer is C. Building a histogram counting the occurrences of various strings in a file_
### 6.	Which of the following lines of Python is equivalent to the following sequence of statements assuming that counts is a dictionary?
    if key in counts:
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1
Choose the correct answer:

    A. counts[key] = (counts[key] * 1) + 1
    B. counts[key] = (key in counts) + 1
    C. counts[key] = counts.get(key,0) + 1
    D. counts[key] = key + 1
    E. counts[key] = counts.get(key,-1) + 1
_Answer is B. counts[key] = (key in counts) + 1_
### 7.	In the following Python, what does the for loop iterate through?
    x = dict()
    ...
    for y in x :
         ...
Choose the correct answer:

    A. It loops through the keys in the dictionary
    B. It loops through the integers in the range from zero through the length of the dictionary
    C. It loops through the values in the dictionary
    D. It loops through all of the dictionaries in the program
_Answer is A. It loops through the keys in the dictionary_
### 8.	Which method in a dictionary object gives you a list of the values in the dictionary?
    A. items()
    B. values()
    C. all()
    D. keys()
    E. each()
_Answer is B. values()_
### 9.	What is the purpose of the second parameter of the get() method for Python dictionaries?
    A. The value to retrieve
    B. To provide a default value if the key is not found
    C. The key to retrieve
    D. An alternate key to use if the first key cannot be found
_Answer is B. To provide a default value if the key is not found_
