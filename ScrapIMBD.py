from bs4 import BeautifulSoup
import requests

try: 
    source = requests.get("https://www.imdb.com/fr/chart/top/")
    source.raise_for_status()
    soup = BeautifulSoup(source.text , 'html.parser')

    movies = soup.find('tbody' , class_ = 'ipc-metadata-list ipc-metadata-list--dividers-between sc-2b8fdbce-0 emPbxy compact-list-view ipc-metadata-list--base').find_all('li')
    print(len(movies))









except Exception as e :
    print("Error fetching the page:", e)
    exit()
    
