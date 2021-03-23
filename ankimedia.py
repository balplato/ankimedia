import os
import requests
from bs4 import BeautifulSoup

WORD = input("Enter your word below \n")
USERNAME = os.getlogin()
PATH = f'C:\\Users\\{USERNAME}\\AppData\\Roaming\\Anki2\\User 1\\collection.media\\'
URL = f'https://dictionary.cambridge.org/dictionary/english/{WORD}'
HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
           }

r = requests.get(URL, headers=HEADERS)

print(r.status_code)
