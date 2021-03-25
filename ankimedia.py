import os
import requests
from bs4 import BeautifulSoup

WORD = input("Enter your word below \n")
american = ''
british = ''
USERNAME = os.getlogin()
PATH = f'C:\\Users\\{USERNAME}\\AppData\\Roaming\\Anki2\\User 1\\collection.media\\'
URL = f'https://dictionary.cambridge.org/dictionary/english/{WORD}'
HEADERS = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}

r = requests.get(URL, headers=HEADERS)

html = r.text

soup = BeautifulSoup(html, 'html.parser')

item = soup.find_all('source')

mp3 = set()

for i in item:
    if '.ogg' in str(i):
        pass
    else:
        mp3.add((i['src']))

for m in mp3:
    if 'us_pron' in m:
        american += m
        print(f"American: {american}")
    else:
        british += m
        print(f'British: {british}')

link = f'https://dictionary.cambridge.org{american}'
print(link)

r = requests.get(link, headers=HEADERS)
with open(f'{PATH}{WORD}_us.mp3', 'wb') as f:
    f.write(r.content)
