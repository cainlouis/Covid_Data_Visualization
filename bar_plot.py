# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:06:56 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import matplotlib.pyplot as plt
from datetime import datetime
import mysql.connector 

class BarPlot:
    def __init__(self, connection):
        self.__mydb = connection
        self.__cursor = self.__mydb.cursor(buffered = True)
        self.__country_list2 = ['Spain', 'Russia', 'Brazil', 'Chile', 'Canada']
        self.__today_date = datetime.today().strftime('%Y-%m-%d')
    
    def totaldeath(self):
        try:
            country_list = ['France', 'USA', 'India', 'Italy', 'UK']
            death_list = []
            for country in country_list:
                self.__cursor.execute("SELECT deaths_per_1m FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                data = self.__cursor.fetchone() 
                death_list.append(data[0])
        
            death_dict = {
                country_list[0]: death_list[0],
                country_list[1]: death_list[1],
                country_list[2]: death_list[2],
                country_list[3]: death_list[3],
                country_list[4]: death_list[4]}
        
            print(death_dict)
            #Graphics
            plt.bar(range(len(death_dict)), list(death_dict.values()), align='center')
            plt.xticks(range(len(death_dict)), list(death_dict.keys()))
            plt.legend(labels=['Deaths/1m'])
            plt.show()
        except mysql.connector.Error:
            print('Could not find the deaths_per_1m')
        
    def totalrecovered(self):
        try:
            recovered_list = []
            for country in self.__country_list2:
                self.__cursor.execute("SELECT totalRecovered FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                recovered = self.__cursor.fetchone() 
                recovered_list.append(recovered[0])
            
            recovered_dict = {
                self.__country_list2[0]: recovered_list[0],
                self.__country_list2[1]: recovered_list[1],
                self.__country_list2[2]: recovered_list[2],
                self.__country_list2[3]: recovered_list[3],
                self.__country_list2[4]: recovered_list[4]}
            
            print(recovered_dict)
            #Graphics
            plt.bar(range(len(recovered_dict)), list(recovered_dict.values()), align='center')
            plt.xticks(range(len(recovered_dict)), list(recovered_dict.keys()))
            plt.legend(labels=['TotalRecoveredToday'])
            plt.show()
        
            self.__totaltest()
        except mysql.connector.Error:
            print('Could not find the totalRecovered')
        
    def __totaltest(self):
        try:
            test_list = []
            for country in self.__country_list2:
                self.__cursor.execute("SELECT totaltests FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                tests = self.__cursor.fetchone() 
                test_list.append(tests[0])
            
            tests_dict = {
                self.__country_list2[0]: test_list[0],
                self.__country_list2[1]: test_list[1],
                self.__country_list2[2]: test_list[2],
                self.__country_list2[3]: test_list[3],
                self.__country_list2[4]: test_list[4]}
            
            print(tests_dict)
            #Graphics
            plt.bar(range(len(tests_dict)), list(tests_dict.values()), align='center')
            plt.xticks(range(len(tests_dict)), list(tests_dict.keys()))
            plt.legend(labels=['TotalTestsToday'])
            plt.show()
        except mysql.connector.Error:
            print('Could not find the totaltests')
        