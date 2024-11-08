### 1.	What do we do to a Python statement that is immediately after an if statement to indicate that the statement is to be executed only when the if statement is true?
    A. Underline all of the conditional code
    B. Begin the statement with a curly brace {
    C. Start the statement with a "#" character
    D. Indent the line below the if statement
_Answer is D.	Indent the line below the if statement_
### 2.	Which of these operators is not a comparison / logical operator?
    A. !=
    B. >=
    C. ==
    D. >
    E. =
_Answer is E. =_
### 3.	What is true about the following code segment:
    if  x == 5 :
      print('Is 5')
      print('Is Still 5')
      print('Third 5')
Choose the correct answer:
    
    A. Depending on the value of x, either all three of the print statements will execute or none of the statements will execute
    B. The string 'Is 5' will always print out regardless of the value for x.
    C. The string 'Is 5' will never print out regardless of the value for x.
    D. Only two of the three print statements will print out if the value of x is less than zero.
_Answer is A. Depending on the value of x, either all three of the print statements will execute or none of the statements will execute_
### 4.	When you have multiple lines in an if block, how do you indicate the end of the if block?
    A. You de-indent the next line past the if block to the same level of indent as the original if statement
    B. You omit the semicolon ; on the last line of the if block
    C. You use a curly brace { after the last line of the if block
    D. You put the colon : character on a line by itself to indicate we are done with the if block
_Answer is A. You de-indent the next line past the if block to the same level of indent as the original if statement_
### 5.	You look at the following text:
    if x == 6 :
      print('Is 6')
      print('Is Still 6')
      print('Third 6')
It looks perfect but Python is giving you an 'Indentation Error' on the second print statement. What is the most likely reason?

    A. Python has reached its limit on the largest Python program that can be run
    B. In order to make humans feel inadequate, Python randomly emits 'Indentation Errors' on perfectly good code - after about an hour the error will just go away without any changes to your program
    C. Python thinks 'Still' is a mis-spelled word in the string
    D. You have mixed tabs and spaces in the file
_Answer is D. You have mixed tabs and spaces in the file_ 
### 6.	What is the Python reserved word that we use in two-way if tests to indicate the block of code that is to be executed if the logical test is false?
    A. otherwise
    B. A closing curly brace followed by an open curly brace like this }{
    C. iterate
    D. else
_Answer is D. else_
### 7.	What will the following code print out?
    x = 0
    if x < 2 :
      print('Small')
    elif x < 10 :
      print('Medium'0
    else :
      print('LARGE')
    print('All done')
Choose the correct answer:

    A. Small
       Medium
       LARGE
       All done
    B. Small
       All done
    C. Medium
       All done
    D. Small
_Answer is B. Small
              All done_
### 8.	For the following code, 
    if x < 2 :
      print('Below 2')
    elif x >= 2 :
      print('Two or more')
    else :
      print('Something else')
What value of 'x' will cause 'Something else' to print out?

    A. x = -2
    B. x = 2.0
    C. This code will never print 'Something else' regardless of the value for 'x'
    D. x = -2.0
_Answer is C. This code will never print 'Something else' regardless of the value for 'x'_
### 9.	In the following code (numbers added)
    (1)   astr = 'Hello Bob'
    (2)   istr = int(astr)
    (3)   print('First', istr)
    (4)   astr = '123'
    (5)   istr = int(astr)
    (6)   print('Second', istr)
Which will be the last line to execute successfully?   

    A. 5
    B. 1
    C. 2
    D. 4
_Answer is B. 1_
### 10.	For the following code:
    astr = 'Hello Bob'
    istr = 0
    try:
      istr = int(astr)
    except:
      istr = -1
What will the value be for istr after this code executes?

    A. It will be the 'Not a number' value (i.e. NaN)
    B. -1
    C. It depends on the position in the collating sequence for the letter 'H'
    D. The istr variable will not have a value
_Answer is B. -1_
