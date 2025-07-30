from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
#######
#this code will outputs the complete HTML of Page1.html in pythonscraping.com
#looks at the Python module request (found within the urllib library) and imports only the function urlopen
#urlopen is used to open a remote object across a network and read it. Because it is a fairly generic function (it can read HTML files, image files, or any other file stream with ease), we will be using it quite frequently throughout the book.
#######