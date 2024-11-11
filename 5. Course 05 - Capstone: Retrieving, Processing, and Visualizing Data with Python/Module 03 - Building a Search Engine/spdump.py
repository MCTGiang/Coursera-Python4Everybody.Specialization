# Page Rank: First you will spider 100 pages from http://python-data.dr-chuck.net/ run the page rank algorithm and take some screen shots.
# Then you will reset the spider process and spider 100 pages from any other site on the Internet, run the page rank algorithm, and take some screen shots.

import sqlite3

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')

count = 0
for row in cur :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
cur.close()
