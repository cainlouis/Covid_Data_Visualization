

from scrapper import Scrapper
from json_creator import JsonCreator
from data_archiver import DataArchiver
from bar_plot import BarPlot
from data_analyzer import DataAnalyzer


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
# Create one big list to send to createjson
allData = s.today + s.yesterday + s.yesterday2

filename = 'country_neighbour_dist_file.json'

# Create the JsonCreator object
jsn = JsonCreator(filename)

# Call write2file to write the json file
jsn.write2file(allData)

# Create the archivedata object
db = DataArchiver(filename)

# Call the createtable to create the table
db.createtable()

# Re use the db connection
connection = db.get_connection()

# Create the DataAnalyzer object
analyzer = DataAnalyzer(connection)

analyzer.analyze(["Canada", "Colombia"])

#create plot object
plot = BarPlot(connection)

plot.totaldeath()

plot.totalrecovered()

# Close the db connection!
connection.close()

print("done!")

