### 1.	How do we model a many-to-many relationship between two database tables?
    A. We use the ARRAY column type in both of the tables
    B. We use a BLOB column in both tables
    C. We add 10 foreign keys to each table with names like artict_id_1, artist_id2, etc.
    D. We add a table with two foreign keys
_Answer is D. We add a table with two foreign keys_
### 2.	In Python, what is a database "cursor" most like?
    A. A Python dictionary
    B. A file handle
    C. A function
    D. A method within a class
_Answer is B.	A file handle_
### 3.	What method do you call in an SQLIte cursor object in Python to run an SQL command?
    A. run() 
    B. execute()
    C. send()
    D. socket()
_Answer is B. execute()_
### 4.	In the following SQL,
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
what is the purpose of the "?"?

    A. It is a syntax error
    B. It is a search wildcard
    C. It is a placeholder for the contents of the "org" variable
    D. It allows more than one boolean operation in the WHERE clause
_Answer is C. It is a placeholder for the contents of the "org" variable_
### 5.	In the following Python code sequence (assuming cur is a SQLite cursor object), 
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
what is the value in row if no rows match the WHERE clause?

    A. None
    B. An empty dictionary
    C. -1
    D. An empty list
_Answer is A. None_
### 6.	What does the LIMIT clause in the following SQL accomplish? 
    SELECT org, count FROM Counts 
       ORDER BY count DESC LIMIT 10
Choose the correct answer:

    A. It only retrieves the first 10 rows from the table
    B. It only sorts on the first 10 characters of the column
    C. It reverses the sort order if there are more than 10 rows
    D. It avoids reading data from any table other than Counts
_Answer is A. It only retrieves the first 10 rows from the table_
### 7.	What does the executescript() method in the Python SQLite cursor object do that the normal execute() method does not do?
    A. It allows embedded JavaScript to be executed
    B. It allows database tables to be created
    C. It allows multiple SQL statements separated by semicolons
    D. It allows embeded Python to be executed
_Answer is C. It allows multiple SQL statements separated by semicolons_
### 8.	What is the purpose of "OR IGNORE" in the following SQL:
    INSERT OR IGNORE INTO Course (title) VALUES ( ? )
Choose the correct answer:

    A. It makes sure that if a particular title is already in the table, there are no duplicate rows inserted
    B. It ignores errors in the SQL syntax for the statement
    C. It updates the created_at value if the title already exists in the table
    D. It ignores any foreign key constraint errors
_Answer is A. It makes sure that if a particular title is already in the table, there are no duplicate rows inserted_
### 9.	What do we generally avoid in a many-to-many junction table?
    ☐ An AUTOINCREMENT primary key column
    ☐ A logical key
    ☐ Two foreign keys
    ☐ Data items specific to the many-to-many relationship
_Answer is An AUTOINCREMENT primary key column and Data items specific to the many-to-many relationship_
### 10.	For the following Python code to work, what must be added to the title column in the CREATE TABLE statement for the Course table: 
        cur.execute('''INSERT OR IGNORE INTO Course (title)
            VALUES ( ? )''', ( title, ) )
        cur.execute('SELECT id FROM Course WHERE title = ? ', 
            (title, ))
        course_id = cur.fetchone()[0]
Choose the correct answer:

    A. An AUTOINCREMENT indication
    B. A PRIMARY KEY indication
    C. A NOT NULL constraint
    D. A UNIQUE constraint
_Answer is D. A UNIQUE constraint_
