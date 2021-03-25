# python_project1
# author: Sergio Segrera & Nael Louis
# id: 1933693, 1934115

This project contains a json file containing the table found in https://www.worldometers.info/coronavirus/. 

There's a total of 6 python files each which fulfills a distinct role:
main.py: which is the file that takes an object for each of the following files.
scrapper.py: which scraps the website and insert the data in a list
json_creator.py: which creates the json file with the data we scrapped
data_archiver.py: which inserts in the database of the user the data found in the json file
data_analyser.py: which analyzes the data of 5 countries
bar_plot.py: which create a bar plot for 3 informations; the deaths per millions of today, the total recovered today, the total tests today. There's 5 countries in each bar_plot  

Run main.py to operate the project 

First enter the required information to create a connection to a mysql database. The program assumes you are running the db in localhost and using the default port.

The program will then ask the user to input a country to compare differences in key covid numbers.