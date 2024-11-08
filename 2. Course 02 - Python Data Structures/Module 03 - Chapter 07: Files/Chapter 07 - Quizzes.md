### 1.	Given the architecture and terminology we introduced in Chapter 1, where are files stored?
    A. Secondary memory
    B. Central Processor
    C. Main Memory
    D. Motherboard
_Answer is A. Secondary memory_
### 2.	What is stored in a "file handle" that is returned from a successful open() call?
    A. The handle is a connection to the file's data
    B. All the data from the file is read into memory and stored in the handle
    C. The handle has a list of all of the files in a particular folder on the hard drive
    D. The handle contains the first 10 lines of a file
_Answer is A. The handle is a connection to the file's data_
### 3.	What do we use the second parameter of the open() call to indicate?
    A. The list of folders to be searched to find the file we want to open
    B. Whether we want to read data from the file or write data to the file
    C. What disk drive the file is stored on
    D. How large we expect the file to be
_Answer is B. Whether we want to read data from the file or write data to the file_
### 4.	What Python function would you use if you wanted to prompt the user for a file name to open?
    A. gets()
    B. input()
    C. alert()
    D. file_input()
_Answer is B. input()_
### 5.	What is the purpose of the newline character in text files?
    A. It indicates the end of one line of text and the beginning of another line of text
    B. It enables random movement throughout the file 
    C. It adds a new network connection to retrieve files from the network
    D. It allows us to open more than one files and read them in a synchronized manner
_Answer is A. It indicates the end of one line of text and the beginning of another line of text_
### 6.	If we open a file as follows: xfile = open('mbox.txt'). What statement would we use to read the file one line at a time?
    A. while ( getline (xfile,line) ) {
    B. READ (xfile,*,END=10) line
    C. while (<xfile>) {
    D. for line in xfile:
_Answer is D. for line in xfile:_
### 7.	What is the purpose of the following Python code?
    fhand = open('mbox.txt')
    x = 0
    for line in fhand:
      x = x + 1
    print(x)
Choose the correct answer:

    A. Count the lines in the file 'mbox.txt'
    B. Reverse the order of the lines in mbox.txt
    C. Remove the leading and trailing spaces from each line in mbox.txt
    D. Convert the lines in mbox.txt to upper case
_Answer is A. Count the lines in the file 'mbox.txt'_
### 8.	If you write a Python program to read a text file and you see extra blank lines in the output that are not present in the file input as shown below, what Python string function will likely solve the problem?
    From: stephen.marquard@uct.ac.za
    
    From: louis@media.berkeley.edu
    
    From: zqian@umich.edu
    
    From: rjlowe@iupui.edu
    
    ...
Choose the correct answer:

    A. startswith()
    B. rstrip()
    C. find()
    D. ljust()
_Answer is B. rstrip()_
### 9.	The following code sequence fails with a traceback when the user enters a file that does not exist. How would you avoid the traceback and make it so you could print out your own error message when a bad file name was entered?
    fname = input('Enter the file name: ')
    fhand = open(fname) 
Choose the correct answer:

    A. setjmp / longjmp
    B. begin / rescue / end
    C. on error resume next
    D. try / except
_Answer is D. try / except_
### 10.	What does the following Python code do?
    fhand = open('mbox-short.txt')
    inp = fhand.read()
Choose the correct answer:

    A. Turns the text in the file into a graphic image like a PNG or JPG
    B. Reads the entire file into the variable inp as a string
    C. Prompts the user for a file name
    D. Checks to see if the file exists and can be written
_Answer is B. Reads the entire file into the variable inp as a string_
