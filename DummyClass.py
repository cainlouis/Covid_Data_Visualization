# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:41:56 2021

@author: Sergio Segrera & Nael Louis
@id: *, 1934115
"""
'''
This class is a dummy class to see if I could create a class to collect the data.
Was not working so I have another file to do the job
'''
import requests
from bs4 import BeautifulSoup


class CollectData:
    def __init__(self):
        self.url = "https://www.worldometers.info/coronavirus/"
        self.webpage_response  = requests.get(self.url)
        
    def __getData(self):
        #soup = BeautifulSoup(self.__webpage_response.content, 'html.parser')
        #target_content = soup.find(id='nav-tabContent')
        target_content = self.webpage_response.content
        print(target_content)
        
        '''
        results = soup.find(id="nav-tabContent")
        tables = results.find_all('table', class_='table table-bordered table-hover main_table_countries dataTable no-footer')
        for table in tables:
            table_today  = table.find()
            '''
