# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:41:56 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import requests
from bs4 import BeautifulSoup
import datetime

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
        self.today = self.__filter_table(table_today, datetime.date.today())

        # Create list of data for yesterday
        self.yesterday = self.__filter_table(table_yesterday, datetime.date.today() - datetime.timedelta(1))

        # Create list of data for 2 days ago
        self.yesterday2 = self.__filter_table(table_yesterday2, datetime.date.today() - datetime.timedelta(2))

    # Parse the table html and filter out useless rows and add the appropriate date
    def __filter_table(self, table, date):
        # t: Initialized filtered list
        t = []
        for tr in table.find_all("tr"):
            cols = []
            for td in tr.find_all(["td", "th"]):
                text = td.get_text(strip=True)
                cols.append(text)
            if not cols[0] == "" and not cols[0] == "#":
                cols.append(date.isoformat())
                # Remove the first index of the cols because it serves no purpose
                # It is not a unique number and depending on the day a different number 
                # is given to a different country, it is inconsistent
                t.append(cols[1:])
        return t
