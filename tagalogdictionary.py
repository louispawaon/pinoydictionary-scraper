# Scraping through https://tagalog.pinoydictionary.com/list/

import string
import re
import requests
import os
import bs4
from bs4 import BeautifulSoup

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
letters = list(string.ascii_lowercase)
letter_index = 0
page_index = 1

try:
    siteurl = 'http://tagalog.pinoydictionary.com/list/' + letters[letter_index] + '/'
    r = requests.get(url=siteurl,headers=header)
    print(r.status_code)
    soup = bs4.BeautifulSoup(r.text,'lxml')
    num= soup.find('a',{'title':'Last Page'})['href']
    lastPage=int(re.sub(r'[\W_]+', '', num)[-2:])
    print(lastPage)
except Exception as e:
    print(e)


with open('tagalog_wordlist.txt','a')as f:

    while page_index<=lastPage:
        try:
            configuredurl = 'http://tagalog.pinoydictionary.com/list/' + letters[letter_index] + '/' + str(page_index) + '/'
            req = requests.get(url=configuredurl,headers=header)
            print(r.status_code)
            wordsoup = bs4.BeautifulSoup(req.text,'lxml')
        except Exception as e:
            print(e)

        print('Extracting from', configuredurl)
        
        try:
            for h2 in wordsoup.find_all(class_="word-entry"):
                atags=h2.find_all('a')
                for words in atags:
                    tagalogword = words.text
                    f.write(tagalogword+"\n")
                    print(tagalogword)
        except Exception as e:
            print(e)
        
        page_index+=1
        
#format files para mas paspas pag paste sa ts file
#dle similar ang words na naa 