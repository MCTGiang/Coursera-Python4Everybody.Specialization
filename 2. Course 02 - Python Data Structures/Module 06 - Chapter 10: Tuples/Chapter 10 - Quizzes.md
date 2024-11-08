### 1.	What is the difference between a Python tuple and Python list?
    A. Lists are mutable and tuples are not mutable
    B. Lists are indexed by integers and tuples are indexed by strings
    C. Tuples can be expanded after they are created and lists cannot
    D. Lists maintain the order of the items and tuples do not maintain order
_Answer is A.	Lists are mutable and tuples are not mutable_
### 2.	Which of the following methods work both in Python lists and Python tuples?
    A. append()
    B. index()
    C. reverse()
    D. pop()
    E. sort()
_Answer is B.	index()_
### 3.	What will end up in the variable y after this code is executed?
    x , y = 3, 4
Choose the correct answer

    A. A two item tuple
    B. 3
    C. 4
    D. A dictionary with the key 3 mapped to the value 4
    E. A two item list
_Answer is C.	4_
### 4.	In the following Python code, what will end up in the variable y?
    x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
    y = x.items()
Choose the correct answer:

    A. A list of tuples
    B. A list of strings
    C. A list of integers
    D. A tuple with three integers
_Answer is D.	A tuple with three integers_
### 5.	Which of the following tuples is greater than x in the following Python sequence?
    x = (5, 1, 3)
    if ??? > x :
       ...
Choose the correct answer:

    A. (0, 1000, 2000) 
    B. (6, 0, 0) 
    C. (5, 0, 300)
    D. (4, 100, 200)
_Answer is D.	(4, 100, 200)_
### 6.	What does the following Python code accomplish, assuming the c is a non-empty dictionary?
    tmp = list()
    for k, v in c.items() :
        tmp.append( (v, k) ) 
Choose the correct answer:

    A. It creates a list of tuples where each tuple is a value, key pair
    B. It sorts the dictionary based on its key values
    C. It computes the largest of all of the values in the dictionary
    D. It computes the average of all of the values in the dictionary
_Answer is A.	It creates a list of tuples where each tuple is a value, key pair_
### 7.	If the variable data is a Python list, how do we sort it in reverse order?
    A. data.sort.reverse()
    B. data = data.sort(-1)
    C. data = sortrev(data)
    D. data.sort(reverse=True)
_Answer is D.	data.sort(reverse=True)_
### 8.	Using the following tuple, how would you print 'Wed'?
    days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
Choose the correct answer:

    A. print(days[2])
    B. print[days(2)]
    C. print(days(2))
    D. print(days.get(1,-1))
    E. print(days[1])
    F. print(days{2})
_Answer is A.	print(days[2])_
### 9.	In the following Python loop, why are there two iteration variables (k and v)?
    c = {'a':10, 'b':1, 'c':22}
    for k, v in c.items() :
        ...
Choose the correct answer:

    A. Because for each item we want the previous and current key
    B. Because there are two items in the dictionary
    C. Because the items() method in dictionaries returns a list of tuples
    D. Because the keys for the dictionary are strings
_Answer is C.	Because the items() method in dictionaries returns a list of tuples_
### 10.	Given that Python lists and Python tuples are quite similar - when might you prefer to use a tuple over a list?
    A. For a list of items that want to use strings as key values instead of integers
    B. For a list of items that will be extended as new items are found
    C. For a list of items you intend to sort in place
    D. For a temporary variable that you will use and discard without modifying
_Answer is D.	For a temporary variable that you will use and discard without modifying_
