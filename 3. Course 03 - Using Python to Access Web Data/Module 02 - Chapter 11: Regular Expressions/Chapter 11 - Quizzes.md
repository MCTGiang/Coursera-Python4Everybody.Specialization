### 1.	Which of the following best describes "Regular Expressions"?
    A. A way to solve Algebra formulas for the unknown value
    B. A small programming language unto itself
    C. The way Python handles and recovers from errors that would otherwise cause a traceback
    D. A way to calculate mathematical values paying attention to operator precedence
_Answer is C. The way Python handles and recovers from errors that would otherwise cause a traceback_
### 2.	Which of the following is the way we match the "start of a line" in a regular expression?
    A. ^
    B. str.startswith()
    C. \linestart
    D. String.startsWith()
    E. variable[0:1]
_Answer is A. ^_
### 3.	What would the following mean in a regular expression? [a-z0-9]
    A. Match a lowercase letter or a digit
    B. Match any text that is surrounded by square braces
    C. Match anything but a lowercase letter or digit
    D. Match any number of lowercase letters followed by any number of digits
    E. Match an entire line as long as it is lowercase letters or digits
_Answer is  A. Match a lowercase letter or a digit_
### 4.	What is the type of the return value of the re.findall() method?
    A. An integer
    B. A list of strings
    C. A boolean
    D. A single character
    E. A string
_Answer is B. A list of strings_
### 5.	What is the "wild card" character in a regular expression (i.e., the character that matches any character)?
    A. .
    B. +
    C. *
    D. ^
    E. $
    F. ?
_Answer is A. ._
### 6.	What is the difference between the "+" and "*" character in regular expressions?
    A. The "+" matches at least one character and the "*" matches zero or more characters
    B. The "+" matches upper case characters and the "*" matches lowercase characters
    C. The "+" matches the beginning of a line and the "*" matches the end of a line
    D. The "+" matches the actual plus character and the "*" matches any character
    E. The "+" indicates "start of extraction" and the "*" indicates the "end of extraction"
_Answer is A. The "+" matches at least one character and the "*" matches zero or more characters_
### 7.	What does the "[0-9]+" match in a regular expression?
    A. Zero or more digits
    B. Any mathematical expression
    C. Any number of digits at the beginning of a line
    D. One or more digits
    E. Several digits followed by a plus sign
_Answer is D. One or more digits_
### 8.	What does the following Python sequence print out?
    x = 'From: Using the : character'
    y = re.findall('^F.+:', x)
    print(y)
Choose the correct answer:

    A. :
    B. ['From: Using the :']
    C. From:
    D. ['From:']
    E. ^F.+:
_Answer is B. ['From: Using the :']_
### 9.	What character do you add to the "+" or "*" to indicate that the match is to be done in a non-greedy manner?
    A. ?
    B. ^
    C. \g
    D. ++
    E. **
    F. $
_Answer is A. ?_
### 10.	Given the following line of text:
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
What would the regular expression '\S+?@\S+' match?

    A. marquard@uct
    B. d@uct.ac.za
    C. From
    D. \@\
    E. stephen.marquard@uct.ac.za
_Answer is E. stephen.marquard@uct.ac.za_
