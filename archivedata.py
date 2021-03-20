# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 21:27:25 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import mysql.connector
import json

class ArchiveData:
    def __init__(self, filename):
        self.__filename = filename
        self.__mydb = self.__connectiontodb()
        self.__cursor = self.__mydb.cursor(buffered = True)
        
    def __connectiontodb(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user= input('enter username for db: '),
            password= input('enter password for db: '),
            auth_plugin='mysql_native_password',
            database= input('enter database: '))
        
        print(mydb)
        return mydb
        
    def createtable(self):
        try:
            self.__cursor.execute('DROP TABLE IF EXISTS covid')
            print('covid has been dropped')
        except mysql.connector.Error:
            print('covid is not in database')
        self.__cursor.execute('CREATE TABLE covid (country VARCHAR(255), totalcases INT, newcases INT, totaldeaths INT, newdeaths INT, totalRecovered INT, newrecovered INT, activecases INT, critical INT, totalcases_per_1m INT, deaths_per_1m INT, totaltests INT, tests_per_1m INT, population INT, continent VARCHAR(255), 1case_every_x_ppl INT, 1death_every_x_ppl INT, 1test_every_x_ppl INT, day DATE)')
        self.__mydb.commit()
        self.__insertdata()
        
    def __insertdata(self):
        data = []
        for line in open(self.__filename, 'r'):
            data.append(json.loads(line))
            #print(data)
        for line in data:
            print(line)
            query = 'INSERT INTO covid VALUES (%s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            self.__cursor.execute(query, line)
        self.__mydb.commit()
        self.__cursor.close()
            