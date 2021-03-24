# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:27:25 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import mysql.connector
import json

#This class get the file from parent class and connect to the db to add the data from the json file 
class DataArchiver: 
    def __init__(self, filename):
        self.__filename = filename
        self.__mydb = self.__connectiontodb()
        self.__cursor = self.__mydb.cursor(buffered = True)
    
    #connect to the db with the information we get as input then return the connection
    def __connectiontodb(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user= input('Enter username for db: '),
            password= input('Enter password for db: '),
            auth_plugin='mysql_native_password',
            database= input('Enter database: '))
        
        print(mydb)
        return mydb
    
    #creates the table covid and call insert data    
    def createtable(self):
        #If the table covid already exist drop it else print that it is not in db
        try:
            
            self.__cursor.execute('DROP TABLE IF EXISTS covid')
            print('covid has been dropped')
            #Create the table
            self.__cursor.execute('CREATE TABLE covid (\
                country VARCHAR(255), \
                totalcases INT, \
                newcases INT, \
                totaldeaths INT, \
                newdeaths INT, \
                totalRecovered INT, \
                newrecovered INT, \
                activecases INT, \
                critical INT, \
                totalcases_per_1m INT, \
                deaths_per_1m INT, \
                totaltests INT, \
                tests_per_1m INT, \
                population INT, \
                continent VARCHAR(255), \
                1case_every_x_ppl INT, \
                1death_every_x_ppl INT, \
                1test_every_x_ppl INT, \
                day DATE)')
            self.__mydb.commit()
            #then call insertdata
            self.__insertdata()
        except mysql.connector.Error:
            print('covid is not in database')
    
    #insert the data we get from the  json file to the database
    def __insertdata(self):
        try:
            data = []
            #for every line in the json line append it to data
            for line in open(self.__filename, 'r'):
                data.append(json.loads(line))
                #print(data)
            #then insert it to the db
            for line in data:
                query = 'INSERT INTO covid VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                self.__cursor.execute(query, line)
            self.__mydb.commit()
            self.__cursor.close()
            print('Data inserted in covid')
        except mysql.connector.Error:
            print('Could not insert the data')
    
    def get_connection(self):
        return self.__mydb