#!/usr/bin/env python3
import requests
import csv
import json

link = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/OpenData_Slovakia_Covid_DailyStats.csv'

data_list = []
r = requests.get(link)
data = r.text
# data = data.split("\n",1)[1]
for line in data.splitlines():
    row = line.split(";")
    data_list.append(row)
    # print(row)

for item in data_list[0]:
    print(item)

file_name = link.split('/')[-1]
print("FILE NAME", file_name)

with open(file_name, 'w', newline='') as f:
        write = csv.writer(f, quoting = csv.QUOTE_MINIMAL, quotechar = "'") 
        write.writerows(data_list)
        print("Rows:", len(data_list))
        print("CSV file saved!")
