import csv

with open("pipe.csv",'r',newline='') as fl:
    data = csv.DictReader(fl)
    for i in data:
        print(i)