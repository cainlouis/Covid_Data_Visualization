# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:41:56 2021

@author: Sergio Segrera & Nael Louis
@id: *, 1934115
"""

import requests
from bs4 import BeautifulSoup

#Get the html from the website
url = 'https://www.worldometers.info/coronavirus/'
webpage_response = requests.get(url)

#Parser to create the BeautifulSoup object
soup = BeautifulSoup(webpage_response.text, 'html.parser')
#Identifying the parts which contains the info we are looking for

target_container = soup.find(id='nav-tabContent')
table_today = target_container.find('table', id='main_table_countries_today')
table_yesterday = target_container.find('table', id='main_table_countries_yesterday')
table_yesterday2 = target_container.find('table', id='main_table_countries_yesterday2')

rows = []

for tr in table_today.find_all('tr'):
    cols = []
    for td in tr.find_all(['td', 'th']):
       td_text = td.get_text(strip=True) 
       if len(td_text):
          cols.append(td_text)
    rows.append(cols)
    
for tr in table_yesterday.find_all('tr'):
    cols = []
    for td in tr.find_all(['td', 'th']):
       td_text = td.get_text(strip=True) 
       if len(td_text):
          cols.append(td_text)
    rows.append(cols)
    
for tr in table_yesterday2.find_all('tr'):
    cols = []
    for td in tr.find_all(['td', 'th']):
       td_text = td.get_text(strip=True) 
       if len(td_text):
          cols.append(td_text)
    rows.append(cols)
    
print(rows)

