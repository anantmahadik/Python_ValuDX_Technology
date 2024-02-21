import csv

# with open("BP_data.csv") as file1:
#     rec = csv.reader(file1)   # data in list format
#     rec1 = csv.DictReader(file1)   # data in Dictonary format
#
#     print(rec)
#     for i in rec1:
#         print(i.keys())
#         #print(i,type(i))
#         #print(i['i>>¿patient_name'],i['patient_bp_after'])

with open('C:\\Users\\Lenovo\\Desktop\\BP_data.csv',"a") as file2:
    rec = csv.writer(file2)
    rec.writerow(["ram","male","30-50","90","110"])
