import requests
import os
from bs4 import BeautifulSoup

url='https://xkcd.com/1/'
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')
while True:
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text,'html.parser')
    comic_elem=soup.select('#comic img')
    if not comic_elem:
        print("Couldnt download the comics")
    else:
        comic_url='https:'+comic_elem[0].get('src')
        print(f"downloading{comic_url}......")
        res=requests.get(comic_url)
        res.raise_for_status()
        in_file=open(os.path.join('xkcd_comics',os.path.basename(comic_url)),'wb')
        for chunk in res.iter_content(100000):
            in_file.write(chunk)
        in_file.close()
        prev_link=soup.select('a[rel="prev"]')[0]
        if not prev_link:
            break
        url='https://xkcd.com'+prev_link.get('href')
        print("Completed")