from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# for child in bs.find('table' , {'id' : 'giftList'}).children :
#     if child.name == 'tr':
#         for item in child.find_all('td'):
#             print(item.get_text())
#         print('---')  # Separator for each row

### for sibbling : 
# for siblings in bs.find('table' , {'id' : 'giftList'}).tr.next_siblings:
#   print(siblings)

### for Parent previous_sibling :
print(bs.find('img',
{'src':'../img/gifts/img1.jpg'})
.parent.previous_sibling.get_text())
