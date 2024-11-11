### 1.	Who is credited with the REST approach to web services?
    A. Vint Cerf
    B. Leonard Klienrock
    C. Roy Fielding
    D. Daphne Koller
    E. Bjarne Stroustrup
_Answer is C. Roy Fielding_
### 2.	Which of the following is true about an API?
    A. An API keeps servers running even when the power is off
    B. An API defines the pin-outs for the USB connectors
    C. An API defines the header bits in the first 8 bits of all IP packets
    D. An API is a contract that defines how to use a software library
_Answer is D. An API is a contract that defines how to use a software library_
### 3.	What is the method used to parse a string containing JSON data so that you can work with the data in Python?
    A. json.loads()
    B. json.read()
    C. json.connect()
    D. json.parse()
_Answer is A. json.loads()_
### 4.	What kind of variable will you get in Python when the following JSON is parsed:
    {   "id": "001",
        "x": "2",
        "name": "Chuck"
    }
Choose the correct answer:

    A. A tuple with three items
    B. A list of tuples
    C. A list with three items
    D. A dictionary with three key / value pairs
    E. A list with six items
_Answer is D. A dictionary with three key / value pairs_
### 5.	Which of the following is not true about the service-oriented approach?
    A. An application makes use of the services provided by other applications
    B. An application runs together all in one place
    C. Web services and APIs are used to transfer data between applications
    D. Standards are developed where many pairs of applications must work together
_Answer is B. An application runs together all in one place_
### 6.	If the following JSON were parsed and put into the variable x, 
    {
        "users": [
            {
                "status": {
                    "text": "@jazzychad I just bought one .__.",
                },
                "location": "San Francisco, California",
                "screen_name": "leahculver",
                "name": "Leah Culver",
            },
        ...
what Python code would extract "Leah Culver" from the JSON?

    A. x[0]["name"]
    B. x["name"]
    C. x->name
    D. x["users"]["name"]
    E. x["users"][0]["name"]
_Answer is E. x["users"][0]["name"]_
### 7.	What library call do you make to append properly encoded parameters to the end of a URL like the following:
http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI

    A. urllib.urlcat()
    B. urllib.parse.urlencode() 
    C. re.encode()
    D. re.match()
_Answer is B. urllib.parse.urlencode()_
### 8.	What happens when you exceed the Google geocoding API rate limit?
    A. Your application starts to perform very slowly
    B. The API starts to perform very slowly
    C. You cannot use the API for 24 hours
    D. You cannot use the API until you respond to an email that contains a survey question
_Answer is C. You cannot use the API for 24 hours_
### 9.	What protocol does Twitter use to protect its API?
    A. Java Web Tokens
    B. SHA1-MD5
    C. OAuth
    D. WS*Security
    E. SOAP
    F. PKI-HMAC
_Answer is C. OAuth_
### 10.	What header does Twitter use to tell you how many more API requests you can make before you will be rate limited?
    A. x-rate-limit-remaining 
    B. x-max-requests
    C. content-type
    D. x-request-count-down
_Answer is A. x-rate-limit-remaining_
