# This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.
# The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

import sqlite3

# Database Connection:
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Table Creation
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# File Handling
fname = input('Enter file name: ')
if (len(fname) < 1): fname = '  mbox.txt'
fh = open(fname)

# Processing the File
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    splits = email.split('@')
    org = splits[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    # Database Update 
    if row is None:
        cur.execute('INSERT INTO Counts (org, count)VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    # Committing the Changes
    conn.commit()
  
# Displaying the Results
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
  
# Closing the Connection
cur.close()
