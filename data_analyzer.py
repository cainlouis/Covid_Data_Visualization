# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:07:39 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import datetime

class DataAnalyzer:
    def __init__(self, connection):
        self.__mydb = connection
        self.__cursor = self.__mydb.cursor(buffered = True)

    def __get_country_information(self, country, date):
        self.__cursor.execute("SELECT * FROM covid WHERE country = %s AND day = %s", (country, date.isoformat()))

        return self.__cursor.fetchone()


    # For every country in countries
    # select the data for today, yesterday and two days ago
    # calculate the evolution of "key numbers" and return it
    def analyze(self, countries):
        for country in countries:
            today = self.__get_country_information(country, datetime.date.today())
            yesterday = self.__get_country_information(country, datetime.date.today() - datetime.timedelta(1))
            yesterday2 = self.__get_country_information(country, datetime.date.today() - datetime.timedelta(2))

            print(yesterday2)
            # TODO: Calculate change

        self.__cursor.close()