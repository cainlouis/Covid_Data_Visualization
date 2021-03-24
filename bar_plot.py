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
    
    #connect to the db with the information we get as input then return the connection
    def __connectiontodb2(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user= self.__user,
            password= self.__pw,
            auth_plugin='mysql_native_password',
            database= self.__db)
        
        print(mydb)
        return mydb
    
    def totaldeath(self):
        try:
            country_list = ['France', 'USA', 'India', 'Italy', 'UK']
            death_list = []
            for country in country_list:
                query = "SELECT deaths_per_1m FROM covid WHERE country = '" + country + "' AND day = '" + self.__today_date + "'"
                print(query)
                data = self.__cursor.execute(query)
                print(data)
                death_list.append(data)
        
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
            plt.show()
        except mysql.connector.Error:
            print('Could not find the deaths_per_1m')
        
    def totalrecovered(self):
        recovered_list = []
        for country in self.__country_list2:
            query = "SELECT totalrecovered FROM covid WHERE country = '" + country + "' AND day = '" + self.__today_date + "'"
            recovered = self.__cursor.execute(query)
            recovered_list.append(recovered)
            
        recovered_dict = {
            self.__country_list2[0]: recovered_list[0],
            self.__country_list2[1]: recovered_list[1],
            self.__country_list2[2]: recovered_list[2],
            self.__country_list2[3]: recovered_list[3],
            self.__country_list2[4]: recovered_list[4]}
        
        #Graphics
        plt.bar(range(len(recovered_dict)), list(recovered_dict.values()), align='center')
        plt.xticks(range(len(recovered_dict)), list(recovered_dict.keys()))
        plt.set_ylabel('Total Recovered')
        plt.set_title('Total Recovered Today')
        plt.legend(labels=['TotalRecoveredToday'])
        plt.show()
        
        self.__totaltest()
        
    def __totaltest(self):
        test_list = []
        for country in self.__dcountry_list2:
            query = "SELECT totaltests FROM covid WHERE country = '" + country + "' AND day = '" + self.__today_date + "'"
            tests = self.__cursor.execute(query)
            test_list.append(tests)
            
        tests_dict = {
            self.__country_list2[0]: test_list[0],
            self.__country_list2[1]: test_list[1],
            self.__country_list2[2]: test_list[2],
            self.__country_list2[3]: test_list[3],
            self.__country_list2[4]: test_list[4]}
        
        #Graphics
        plt.bar(range(len(tests_dict)), list(tests_dict.values()), align='center', color='o')
        plt.xticks(range(len(tests_dict)), list(tests_dict.keys()))
        plt.set_ylabel('Total Tests')
        plt.set_title('Total Tests Today')
        plt.legend(labels=['TotalTestsToday'])
        plt.show()
        
        