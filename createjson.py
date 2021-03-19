# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 18:33:21 2021

@author: Sergio Segrera & Nael Louis
@id: 1933693, 1934115
"""
import json

class CreateJson:
    def __init__(self):
        self.__filename = 'country_neighbour_dist_file.json'
        
    def write2file(self, data):
        with open(self.__filename, 'w') as write_file:
            for alist in data:
                json.dump(alist, write_file)
                write_file.write('\n')