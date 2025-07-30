# <span class="red">Heavens! what a virulent attack!</span> replied
# <span class="green">the prince</span>, not in the least disconcerted

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
try : 
  bs = BeautifulSoup(html.read() , 'html.parser')

  namelist = bs.find_all('span' , {'class' : 'green'})

  for name in namelist : 
    print(name.get_text())

except HTTPError as e :
  print(e)

except URLError as e :
  print('The server could not be found!')