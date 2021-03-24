

from scrapper import Scrapper
from json_creator import JsonCreator
from data_archiver import DataArchiver
from data_analysis import DataAnalysis
from bar_plot import BarPlot

s = Scrapper()

'''
#print to verify the data
print("-- TODAY --")
for i in s.today:
    print(i)

print("-- YESTERDAY --")
for i in s.yesterday:
    print(i)

print("-- YESTERDAY II --")
for i in s.yesterday2:
    print(i)
'''
#Create one big list to send to createjson
allData = s.today + s.yesterday + s.yesterday2

filename = 'country_neighbour_dist_file.json'


#ask for the user credentials
user = input('enter username for db: ')
pw = input('enter password for db: ')
db = input('enter database: ')

#Create the CreateJson object
jsn = JsonCreator(filename)

#Call write2file to write the json file
jsn.write2file(allData)

#Create the archivedata object
db = DataArchiver(filename, user, pw, db)

#Call the createtable to create the table
db.createtable()

#create dataAnalysis object

#create plot object
#plot = BarPlot(user, pw, db)

#plot.totaldeath()

#plot.totalrecovered()

print("done!")

