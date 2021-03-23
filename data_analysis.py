# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:07:39 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""

class DataAnalysis:
    def __init__(self, connection):
        self.__mydb = connection
        self.__cursor = self.__mydb.cursor(buffered = True)
        

        