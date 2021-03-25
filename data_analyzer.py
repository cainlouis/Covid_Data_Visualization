# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:07:39 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import mysql.connector
import datetime
import pandas as pd
import matplotlib.pyplot as plt

class DataAnalyzer:
    def __init__(self, connection):
        self.__mydb = connection
        self.__cursor = self.__mydb.cursor(buffered = True)

    def __get_country_information(self, country, date):
        try:
            self.__cursor.execute("SELECT totalcases, newcases, deaths_per_1m, tests_per_1m FROM covid WHERE country = %s AND day = %s", (country, date.isoformat()))
        except mysql.connector.Error:
            print("Could not retrieve information for " + country)
        return self.__cursor.fetchone()


    # For every country in countries
    # select the data for today, yesterday and two days ago
    # calculate the evolution of "key numbers" and return it
    def analyze(self, countries):
        for country in countries:
            today = self.__get_country_information(country, datetime.date.today())
            yesterday = self.__get_country_information(country, datetime.date.today() - datetime.timedelta(1))
            yesterday2 = self.__get_country_information(country, datetime.date.today() - datetime.timedelta(2))

            combined = []
            combined.append(yesterday2)
            combined.append(yesterday)
            combined.append(today)

            df = pd.DataFrame(combined, index=["2 days ago", "yesterday", "today"], columns=["totalcases", "newcases", "deaths_per_1m", "tests_per_1m"])
            plot = df.pct_change().fillna(0).plot(title=country)
            plot.set_ylabel("% change")

            plt.show()

        self.__cursor.close()