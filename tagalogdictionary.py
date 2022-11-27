# Scraping through https://tagalog.pinoydictionary.com/list/

import string
import requests
import os
import bs4
from bs4 import BeautifulSoup

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

with open('tagalog_wordlist.txt','w')as f:

    try:
        siteurl = "https://tagalog.pinoydictionary.com/list/a/"
    except Exception as e:
        print(e)

    try:
        r = requests.get(url=siteurl,headers=header)
        print(r.status_code)
        soup = bs4.BeautifulSoup(r.text,'lxml')
        for h2 in soup.find_all(class_="word-entry"):
            atags=h2.find_all('a')
            for words in atags:
                tagalogword = words.text
                f.write(tagalogword+"\n")
                print(tagalogword)
    except Exception as e:
        print(e)
