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
items = soup.find_all('source')
tracks = 0

for item in items:
    if '.mp3' in str(item) and 'us_pron' in str(item) and tracks < 1:
        link = f'{SITE}{item["src"]}'
        with open(f'{LOCAL_PATH}{WORD}.mp3', 'wb') as f:
            f.write(get(link).content)
        tracks += 1
