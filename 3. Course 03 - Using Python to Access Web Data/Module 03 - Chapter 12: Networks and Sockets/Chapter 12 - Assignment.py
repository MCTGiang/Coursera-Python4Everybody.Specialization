# Exploring the HyperText Transport Protocol
# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers: http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and look at the response headers:
# Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
# Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.

import socket
# Define the host and the port
host = 'data.pr4e.org'
port = 80
# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
sock.connect((host, port))
# Send an HTTP GET request
request = f"GET /intro-short.txt HTTP/1.0\r\nHost: {host}\r\n\r\n"
sock.send(request.encode())
# Receive the response
response = b""
while True:
    data = sock.recv(1024)
    if not data:
        break
    response += data
# Close the socket
sock.close()

# Decode the response to get a string
response_str = response.decode()
# Split the headers and body
headers, body = response_str.split("\r\n\r\n", 1)
# Print the headers
print("HTTP Response Headers:")
print(headers)
# Print the body
print("\nHTTP Response Body:")
print(body)

