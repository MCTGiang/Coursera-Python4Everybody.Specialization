# Extracting Data from XML: write a Python program somewhat similar to http://www.py4e.com/code3/xml3.py.
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# Actual data: http://py4e-data.dr-chuck.net/comments_2122556.xml (Sum ends with 95)
# The data consists of a number of names and comment counts in XML as follows:
# <comment>
#  <name>Matthias</name>
#  <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is xml3.py.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code: counts = tree.findall('.//count')

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input("Enter - ")
uh = urllib.request.urlopen(url)
data = uh.read()

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
count =0
sum=0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print ("Count : ",count)
print ("Sum : ",sum)
