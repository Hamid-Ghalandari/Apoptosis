# a = 4
# if a == 5:
#     print("true")

import csv

CsvFile = open ('data.csv')
CsvReader = csv.DictReader(CsvFile)

lisOfDic = []
 
for item in CsvReader:
    lisOfDic.append(item)
    print(item)
