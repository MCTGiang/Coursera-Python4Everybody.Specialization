### 1.	What is "serialization" when we are talking about web services?
    A. The act of taking data stored in a program and formatting it so it can be sent across the network
    B. Sorting all the data stored in a tuple
    C. Making it so that dictionaries can maintain their keys in sorted order
    D. Marking each network packet so it can be put back into order on the receiving system
_Answer is A. The act of taking data stored in a program and formatting it so it can be sent across the network_
### 2.	What is the method to cause Python to parse XML that is stored in a string?
    A. fromstring()
    B. parse()
    C. readall()
    D. extract()
    E. xpath()
_Answer is A. fromstring()_
### 3.	In this XML, which are the "simple elements"?
    <people>
        <person>
           <name>Chuck</name>
           <phone>303 4456</phone>
        </person>
        <person>
           <name>Noah</name>
           <phone>622 7421</phone>
        </person>
    </people>
Choose the correct answer:

    ☐ person
    ☐ phone
    ☐ name
    ☐ people
    ☐ Noah
_Answer is phone and name_
### 4.	In the following XML, which are attributes?
    <person>
      <name>Chuck</name>
      <phone type="intl">
         +1 734 303 4456
      </phone>
      <email hide="yes" />
    </person>
Choose the correct answer:

    ☐ type
    ☐ person
    ☐ hide
    ☐ name
    ☐ email
_Answer is type and hide_
### 5.	In the following XML, which node is the parent node of node e
    <a>
      <b>X</b>
      <c>
        <d>Y</d>
        <e>Z</e>
      </c>
    </a>
Choose the correct answer:

    A. a
    B. b
    C. c
    D. e
_Answer is C. c_
### 6.	Looking at the following XML, what text value would we find at path "/a/c/e"
    <a>
      <b>X</b>
      <c>
        <d>Y</d>
        <e>Z</e>
      </c>
    </a>
Choose the correct answer:

    A. a
    B. b
    C. Z
    D. Y
    E. e
_Answer is C. Z_
### 7.	What is the purpose of XML Schema?
    A. To establish a contract as to what is valid XML
    B. A Python program to tranform XML files
    C. To transfer XML data reliably during network outages
    D. To compute SHA1 checksums on data to make sure it is not modified in transit
_Answer is A. To establish a contract as to what is valid XML_
### 8.	For this XML Schema:
    <xs:complexType name=”person”>
      <xs:sequence>
        <xs:element name="lastname" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
        <xs:element name="dateborn" type="xs:date"/>
      </xs:sequence>
    </xs:complexType>
And this XML,
    <person>
       <lastname>Severance</lastname>
       <Age>17</Age>
       <dateborn>2001-04-17</dateborn>
    </person>
Which tag is incorrect?

    A. person
    B. dateborn
    C. age
    D. lastname
    E. Age
_Answer is E. Age_
### 9.	What does the "Z" mean in this representation of a time:
    2002-05-30T09:30:10Z
Choose the correct answer:

    A. This time is in the UTC timezone
    B. The hours value is in the range 0-12
    C. The local timezone for this time is New Zealand
    D. This time is Daylight Savings Time
_Answer is A. This time is in the UTC timezone_
### 10.	Which of the following dates is in ISO8601 format?
    A. 05/30/2002
    B. May 30, 2002
    C. 2002-May-30
    D. 2002-05-30T09:30:10Z
_Answer is D. 2002-05-30T09:30:10Z_
### 11.	What is the name of the Python 2.x library to parse XML data?
    A. xml.json
    B. xml.etree.ElementTree 
    C. xml-misc
    D. xml2
_Answer is B. xml.etree.ElementTree_
### 12.	In this XML, which are the "complex elements"?
    <person>
       <lastname>Severance</lastname>
       <Age>17</Age>
       <dateborn>2001-04-17</dateborn>
    </person>
Choose the correct answer:

    ☐ person
    ☐ phone
    ☐ name
    ☐ people
    ☐ Noah
_Answer is person and people_
