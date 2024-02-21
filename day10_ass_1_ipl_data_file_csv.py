#SJ Davis seach umpire data

import csv
count = 0
with open("IPL_matches.csv") as file1:
    rec = csv.reader(file1)   # data in list format
    rec1 = csv.DictReader(file1)   # data in Dictonary format
    # cont = 0
    #print(rec)
    for i in rec:
        x = "SJ Davis"
        #print(i,type(i))

        if "SJ Davis" in i:
            count += 1
            print(i)
print(count)
