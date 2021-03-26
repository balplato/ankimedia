import os
import requests
from bs4 import BeautifulSoup


def get(page):
    r = requests.get(page, headers=HEADERS)
    return r


WORD = input("Enter your word below \n")
USERNAME = os.getlogin()
LOCAL_PATH = f'C:\\Users\\{USERNAME}\\AppData\\Roaming\\Anki2\\User 1\\collection.media\\'
SITE = 'https://dictionary.cambridge.org'
URL = f'{SITE}/dictionary/english/{WORD}'
HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'}

html = get(URL).text

soup = BeautifulSoup(html, 'html.parser')

item = soup.find_all('source')

mp3 = set()
american = ''
british = ''

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

link = f'{SITE}{american}'

with open(f'{LOCAL_PATH}{WORD}_us.mp3', 'wb') as f:
    f.write(get(link).content)
