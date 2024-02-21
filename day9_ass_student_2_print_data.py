with open("student.txt","r") as f2:         # read data
    rec=f2.readline()
    while rec != "":
        field = rec.split(" ")
        if field[3]=="f":
            #if int(field[4])>10:
            print("username ",field[0]," name ",field[1]," surname ",field[2]," gender ",field[3])

        rec = f2.readline()
