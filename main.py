from scrapper import Scrapper
from createjson import CreateJson

s = Scrapper()

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

#Create one big list to send to createjson
allData = s.today + s.yesterday + s.yesterday2

#Create the CreateJson object
jsn = CreateJson()

#Call write2file to write the json file
jsn.write2file(allData)

print("done!")

