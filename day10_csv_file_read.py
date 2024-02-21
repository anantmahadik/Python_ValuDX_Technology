# import csv
#
# with open("BP_data.csv") as file1:
#     rec = csv.reader(file1)   # data in list format
#     rec = csv.DictReader(file1)   # data in Dictonary format
#
#     print(rec)
#     for i in rec:
#         print(i,type(i))


# import csv
#
# with open('C:\\Users\\Lenovo\\Desktop\\BP_data.csv') as file1:
#     rec = csv.reader(file1)
#     print(rec)
#     for i in rec:
#         print(i)
import csv

data = open("C:\\Users\\Lenovo\\Desktop\\Python\\BP_data.csv")
data = csv.reader(data)         # it for list
data1 = csv.reader(data)        # it getting data in dictonary format
print(data)
for i in data:
    print(i)
