# # from urllib.request import urlopen
# # html = urlopen('http://pythonscraping.com/pages/page1.html')
# # print(html.read())
# #######
# #this code will outputs the complete HTML of Page1.html in pythonscraping.com
# #looks at the Python module request (found within the urllib library) and imports only the function urlopen
# #urlopen is used to open a remote object across a network and read it. Because it is a fairly generic function (it can read HTML files, image files, or any other file stream with ease), we will be using it quite frequently throughout the book.
# # #######
# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# # bs = BeautifulSoup(html.read(), 'html.parser')
# # print(bs.h1)
# ################
# from urllib.request import urlopen
# from urllib.error import HTTPError
# from urllib.error import URLError
# try:
#  html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
# except HTTPError as e:
#  print(e)
# except URLError as e:
#  print('The server could not be found!')
# else:
#  print('It Worked!')
#///////////////////////
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def getTitle(url) : 
  try : 
    html = urlopen(url)
  except HTTPError as e :
    return None
  
  try :
    bs = BeautifulSoup(html.read() , 'html.parser')
    title = bs.body.h1
  except AttributeError as e :
    return None
  
  return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None :
  print('Title could not be found')
else : 
  print(title)