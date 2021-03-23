# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:33:21 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import json

#This class write in a json file
class CreateJson:
    def __init__(self, filename):
        self.__filename = filename
        
    def write2file(self, data):
        #With file open to write 
        with open(self.__filename, 'w') as write_file:
            #go through every line of the data
            for alist in data:
                #and dump the list in the file
                json.dump(alist, write_file)
                #and print so skip to the next line
                write_file.write('\n')