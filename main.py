from scrapper import Scrapper

s = Scrapper()

print("-- TODAY --")
for i in s.today:
    print(i)

print("-- YESTERDAY --")
for i in s.yesterday:
    print(i)

print("-- YESTERDAY II --")
for i in s.yesterday2:
    print(i)

print("done!")