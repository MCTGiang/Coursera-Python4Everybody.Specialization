### 1.	Which of the following Python data structures is most similar to the value returned in this line of Python:
    x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
Choose the correct answer:

    A. regular expression
    B. socket
    C. dictionary
    D. list
    E. file handle
_Answer is E. file handle_
### 2.	In this Python code, which line actually reads the data?
    import socket
    
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close()
Choose the correct answer:

    A. mysock.recv()
    B. socket.socket()
    C. mysock.close()
    D. mysock.connect()
    E. mysock.send()
_Answer is A. mysock.recv()_
### 3.	Which of the following regular expressions would extract the URL from this line of HTML:
    <p>Please click <a href="http://www.dr-chuck.com">here</a></p>
Choose the correct answer:

    A. href="(.+)"
    B. href=".+"
    C. http://.*
    D. <.*>
_Answer is A. href="(.+)"_
### 4.	In this Python code, which line is most like the open() call to read a file:
    import socket
    
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysock.close() 
 Choose the correct answer:
 
    A. mysock.connect()
    B. import socket
    C. mysock.recv()
    D. mysock.send()
    E. socket.socket()
_Answer is A. mysock.connect()_
### 5.	Which HTTP header tells the browser the kind of document that is being returned?
    A. HTML-Document:
    B. Document-Type:
    C. Metadata:
    D. ETag:
    E. Content-Type:
_Answer is E. Content-Type:_
### 6.	What should you check before scraping a web site?
    A. That the web site allows scraping
    B. That the web site supports the HTTP GET command
    C. That the web site returns HTML for all pages
    D. That the web site only has links within the same site
_Answer is A. That the web site allows scraping_
### 7.	What is the purpose of the BeautifulSoup Python library?
    A. It repairs and parses HTML to make it easier for a program to understand
    B. It optimizes files that are retrieved many times
    C. It allows a web site to choose an attractive skin
    D. It animates web operations to make them more attractive
    E. It builds word clouds from web pages
_Answer is A. It repairs and parses HTML to make it easier for a program to understand_
### 8.	What ends up in the "x" variable in the following code:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    x = soup('a') 
Choose the correct answer:

    A. A list of all the anchor tags (<a..) in the HTML from the URL
    B. True if there were any anchor tags in the HTML from the URL
    C. All of the externally linked CSS files in the HTML from the URL
    D. All of the paragraphs of the HTML from the URL
_Answer is A. A list of all the anchor tags (<a..) in the HTML from the URL
### 9.	What is the most common Unicode encoding when moving data between systems?
    A. UTF-16
    B. UTF-128
    C. UTF-32
    D. UTF-8
    E. UTF-64
_Answer is D. UTF-8_
### 10.	What is the ASCII character that is associated with the decimal value 42?
    A. *
    B. /
    C. ^
    D. +
    E. !
_Answer is A. *_
### 11.	What word does the following sequence of numbers represent in ASCII:
    108, 105, 110, 101
    A. line
    B. ping
    C. lost
    D. func
    E. tree
_Answer is A. line_
### 12.	How are strings stored internally in Python 3?
    A. Unicode
    B. UTF-8
    C. ASCII
    D. Byte Code
    E. EBCDIC
_Answer is A. Unicode_
### 13.	When reading data across the network (i.e. from a URL) in Python 3, what method must be used to convert it to the internal format used by strings?
    A. trim()
    B. decode()
    C. upper()
    D. encode()
    E. find()
_Answer is B. decode()_
