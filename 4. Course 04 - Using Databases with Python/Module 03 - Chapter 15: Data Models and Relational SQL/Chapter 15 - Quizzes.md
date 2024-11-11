### 1. What is the primary added value of relational databases over flat files?
    A. Ability to execute JavaScript in the file
    B. Ability to execute Python code within the file
    C. Ability to quickly convert data to HTML
    D. Ability to scan large amounts of data quickly
    E. Ability to store data in a format that can be sent across a network
_Answer is D.	Ability to scan large amounts of data quickly_ 
### 2.	What is the purpose of a primary key?
    A. To point to a particular row in another table
    B. To look up a particular row in a table very quickly
    C. To track the number of duplicate values in another column
    D. To look up a row based on a string that comes from outside the program
_Answer is B.	To look up a particular row in a table very quickly_
### 3.	Which of the following is NOT a good rule to follow when developing a database model?
    A. Model each "object" in the application as one or more tables
    B. Never repeat string data in more than one table in a data model
    C. Use a person's email address as their primary key
    D. Use integers as primary keys
_Answer is C.	Use a person's email address as their primary key_
### 4.	If our user interface (i.e., like iTunes) has repeated strings on one column of the user interface, how should we model this properly in a database?
    A. Put the string in the last row where it occurs and put the number of that row in the column of all of the rest of the rows where the string occurs
    B. Make a table that maps the strings in the column to numbers and then use those numbers in the column
    C. Put the string in the first row where it occurs and then put that row number in the column of all of the rest of the rows where the string occurs
    D. Put the string in the first row where it occurs and then put NULL in all of the other rows
    E. Encode the entire row as JSON and store it in a TEXT column in the database
_Answer is B.	Make a table that maps the strings in the column to numbers and then use those numbers in the column_
### 5.	Which of the following is the label we give a column that the "outside world" uses to look up a particular row?
    A. Local key
    B. Primary key
    C. Remote key
    D. Logical key
    E. Foreign key
_Answer is D.	Logical key_
### 6.	What is the label we give to a column that is an integer and used to point to a row in a different table?
    A. Remote key
    B. Foreign key
    C. Local key
    D. Primary key
    E. Logical key
_Answer is B.	Foreign key_
### 7.	What SQLite keyword is added to primary keys in a CREATE TABLE statement to indicate that the database is to provide a value for the column when records are inserted?
    A. AUTOINCREMENT 
    B. AUTO_INCREMENT
    C. ASSERT_UNIQUE
    D. INSERT_AUTO_PROVIDE
_Answer is A.	AUTOINCREMENT_
### 8.	What is the SQL keyword that reconnects rows that have foreign keys with the corresponding data in the table that the foreign key points to?
    A. CONSTRAINT
    B. APPEND
    C. JOIN
    D. COUNT
    E. CONNECT
_Answer is C. JOIN_
### 9.	What happens when you JOIN two tables together without an ON clause?
    A. You get no rows at all
    B. You get all of the rows of the left table in the JOIN and NULLs in all of the columns of the right table
    C. Leaving out the ON clause when joining two tables in SQLite is a syntax error
    D. The rows of the left table are connected to the rows in the right table when their primary key matches
    E. The number of rows you get is the number of rows in the first table times the number of rows in the second table
_Answer is E.	The number of rows you get is the number of rows in the first table times the number of rows in the second table_
### 10.	When you are doing a SELECT with a JOIN across multiple tables with identical column names, how do you distinguish the column names?
    A. tablename['columnname']
    B. tablename/columnname
    C. tablename->columnname
    D. tablename.columnname
_Answer is D.	tablename.columnname_
