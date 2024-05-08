#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:53:00 2024

@author: chuntamy
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.gutenberg.org/browse/languages/zh'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# 找到包含書籍標題的元素
book_titles = soup.find_all(class_='pgdbetext')
# 只保留前 200 本書標題
book_titles = book_titles[:200]
titles=[]
for title in book_titles:
    print(title.text.strip())
    titles.append(title.text.strip())



    

links = soup.find_all('li', class_='pgdbetext')
links = links[:10]
for link in links:
    #如果文章已被刪除，連結為None
    if link.a != None:
        article_data = []   # 單篇文章的資料放入{}
        page_url = "https://www.gutenberg.org"+link.a["href"]
        article_data.append(page_url)
        
        # 進入文章頁面
        response = requests.get(page_url)
        result = BeautifulSoup(response.text, "html.parser")
        
        for single_tr in result.find("table", class_='bibrec').findAll("tr"):
            article_info = single_tr.findAll("td")
            author = article_info[0].string
            print(author)
            
        
        


    
    
    


    
#b=pd.DataFrame(titles, hrefs)
#b.to_csv('b.csv', encoding='utf-8')



#for i in range(len(hrefs)): #爬取兩頁
    #res = requests.get(url)
    #soup = BeautifulSoup(res.text, "html.parser")
    
    # 找到包含書籍標題的元素
    #book_titles = soup.find_all(class_='pgdbetext')
    # 只保留前 200 本書標題
    #book_titles = book_titles[:200]
    #titles=[]
    #for title in book_titles:
        #print(title.text.strip())
        #titles.append(title.text.strip())





