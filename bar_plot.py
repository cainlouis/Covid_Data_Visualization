# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 19:06:56 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import matplotlib.pyplot as plt
from datetime import datetime
import mysql.connector
import numpy as np 

class BarPlot:
    def __init__(self, connection):
        self.__mydb = connection
        self.__cursor = self.__mydb.cursor(buffered = True)
        self.__country_list2 = ['Spain', 'Russia', 'Brazil', 'Chile', 'Canada']
        self.__today_date = datetime.today().strftime('%Y-%m-%d')
    
    #this function get the total of death for each country in country lis and create a bar plot for them
    def totaldeath(self):
        try:
            #Create the list of country we want the info from and a list for each number we get
            country_list = ['France', 'USA', 'India', 'Italy', 'UK']
            death_list = []
            #go through the list of country
            for country in country_list:
                #and take from the database the number of death per millions
                self.__cursor.execute("SELECT deaths_per_1m FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                data = self.__cursor.fetchone() 
                #append the number we get to the death list
                death_list.append(data[0])
            
            #With the data we got from the database create a dictionary 
            death_dict = {
                country_list[0]: death_list[0],
                country_list[1]: death_list[1],
                country_list[2]: death_list[2],
                country_list[3]: death_list[3],
                country_list[4]: death_list[4]}
            
            #print statement for readability  
            print('\n')
            print(death_dict)
           
            #And then create the bar plot for the dictionary
            plt.bar(range(len(death_dict)), list(death_dict.values()), align='center')
            plt.xticks(range(len(death_dict)), list(death_dict.keys()))
            #Create the limit we want for the y axis and the steps we wants
            plt.ylim([0,2000])
            plt.yticks(np.arange(0,2000, 250))
            #then the labels ofthe graph
            plt.ylabel('Deaths per millions')
            plt.title('Deaths Per Millions Today')
            plt.legend(labels=['Deaths/1m'])
            plt.show()
            
            #print statement for readability  
            print('\n')
        except mysql.connector.Error:
            print('Could not find the deaths_per_1m')
            
    #this function get the total recovered for each country in country lis and create a bar plot for them    
    def totalrecovered(self):
        try:
            #Because the country list for this function and the next are the same is was initialized in __init__
            #I could not be bothered to pass it 
            #Create a list for the number we get from database
            recovered_list = []
            
            #go through the list of country
            for country in self.__country_list2:
                #and take from the database the number of total recovered
                self.__cursor.execute("SELECT totalRecovered FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                recovered = self.__cursor.fetchone()
                #append the number we get to the recovered list
                recovered_list.append(recovered[0])
            
            #With the data we got from the database create a dictionary 
            recovered_dict = {
                self.__country_list2[0]: recovered_list[0],
                self.__country_list2[1]: recovered_list[1],
                self.__country_list2[2]: recovered_list[2],
                self.__country_list2[3]: recovered_list[3],
                self.__country_list2[4]: recovered_list[4]}
            
            print(recovered_dict)
            
            #And then create the bar plot for the dictionary
            plt.bar(range(len(recovered_dict)), list(recovered_dict.values()), align='center')
            plt.xticks(range(len(recovered_dict)), list(recovered_dict.keys()))
            #the limit of the  y axis was already correct so i didn't write one
            #Create the labels for the graph
            plt.ylabel('Total recovered per 10 thousands')
            plt.title('Total Recovered Today')
            plt.legend(labels=['TotalrecoveredToday'])
            plt.show()
            
            #print statement for readability  
            print('\n')
            #call total tests to compare graph
            self.__totaltest()
        except mysql.connector.Error:
            print('Could not find the totalRecovered')
        
    def __totaltest(self):
        try:
            #Create a list for the number we get from database
            test_list = []
            #go through the list of country
            for country in self.__country_list2:
                #and take from the database the number of total tests for today
                self.__cursor.execute("SELECT totaltests FROM covid WHERE country = %s AND day = %s", (country, self.__today_date))
                tests = self.__cursor.fetchone()
                #append the number we get to the tests list
                test_list.append(tests[0])
            
            #With the data we got from the database create a dictionary
            tests_dict = {
                self.__country_list2[0]: test_list[0],
                self.__country_list2[1]: test_list[1],
                self.__country_list2[2]: test_list[2],
                self.__country_list2[3]: test_list[3],
                self.__country_list2[4]: test_list[4]}
            
            print(tests_dict)
            
            #And then create the bar plot for the dictionary
            plt.bar(range(len(tests_dict)), list(tests_dict.values()), align='center')
            plt.xticks(range(len(tests_dict)), list(tests_dict.keys()))
            #Create the limit we want for the y axis and the steps we wants
            plt.ylim([0, 135000000])
            plt.yticks(np.arange(0, 135000000, 15000000))
            #then the labels ofthe graph
            plt.ylabel('Total tests per 100 millions')
            plt.title('Total Tests Today')
            plt.legend(labels=['TotalTestsToday'])
            plt.show()
            
            #Close cursor
            self.__cursor.close()
        except mysql.connector.Error:
            print('Could not find the totaltests')
        