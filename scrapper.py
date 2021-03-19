# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:41:56 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self):
        # Get the html from website
        response = requests.get("https://www.worldometers.info/coronavirus/", timeout=5)

        # Create html parser
        soup = BeautifulSoup(response.text, "html.parser")

        # Create data lists
        table_containers = soup.find(id="nav-tabContent")

        table_today = table_containers.find("table", id="main_table_countries_today")
        table_yesterday = table_containers.find("table", id="main_table_countries_yesterday")
        table_yesterday2 = table_containers.find("table", id="main_table_countries_yesterday2")

        # Create list of data for today
        self.today = []

        for tr in table_today.find_all('tr'):
            cols = []
            for td in tr.find_all(['td', 'th']):
                td_text = td.get_text(strip=True) 
                if len(td_text):
                    cols.append(td_text)
            self.today.append(cols)

        # Create list of data for yesterday
        self.yesterday = []

        for tr in table_yesterday.find_all('tr'):
            cols = []
            for td in tr.find_all(['td', 'th']):
                td_text = td.get_text(strip=True) 
                if len(td_text):
                    cols.append(td_text)
            self.yesterday.append(cols)

        # Create list of data for 2 days ago
        self.yesterday2 = []

        for tr in table_yesterday2.find_all('tr'):
            cols = []
            for td in tr.find_all(['td', 'th']):
                td_text = td.get_text(strip=True) 
                if len(td_text):
                    cols.append(td_text)
            self.yesterday2.append(cols)
