#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:00:40 2024

@author: chuntamy
"""

import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup

def get_articles(page_url):
    
    c_response = requests.get(page_url)
    soup = BeautifulSoup(c_response.text, "html.parser")
    
    
    main_content = soup.find("div", class_="container", id="pg-machine-header")
    title=main_content.find('p').text
    print(title)
    author=main_content.find('div', id="pg-header-authlist").text
    print(author)
    #content=main_content.find('div', id="pg-start-separator").text
    #print(content)
    
    main_content2 = soup.find("p",  id="id00001")
    content=main_content2.text
    print(content)



page_url = get_articles('https://www.gutenberg.org/cache/epub/25328/pg25328-images.html')
