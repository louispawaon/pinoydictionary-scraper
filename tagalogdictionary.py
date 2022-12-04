# Scraping through https://tagalog.pinoydictionary.com/list/

import string
import re
import requests
import os
import bs4
from bs4 import BeautifulSoup

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
letters = list(string.ascii_lowercase)

def main():

    page_index = 87
    letter_index = 0  

    with open('tagalog_wordlist.txt','wt')as f:
        while True:
            try:
                configuredurl = 'http://tagalog.pinoydictionary.com/list/' + letters[letter_index] + '/' + str(page_index) + '/'
                req = requests.get(url=configuredurl,headers=header)
                wordsoup = bs4.BeautifulSoup(req.text,'lxml')
            except Exception as e:
                print(e)
                break

            print('Extracting from', configuredurl)
            
            if(wordsoup.find_all(class_="page-not-found")):
                page_index=1
                letter_index+=1
                continue
        
            try:
                for h2 in wordsoup.find_all(class_="word-entry"):
                    atags=h2.find_all('a')
                    for words in atags:
                        tagalogword = words.text
                        print(tagalogword)
                        f.write(tagalogword+"\n")
            except Exception as e:
                print(e)
            
            page_index+=1
        

if __name__ == '__main__':
    main()
