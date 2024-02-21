# name = ""
# with open("valuedx_student.txt","w") as f1:       # write data
#     while name != "end":
#         name = input("enter the name : ")
#         if name == "end":
#             break
#         marks = int(input("enter the marks : "))
#         f1.write(name+" "+str(marks)+'\n')

with open("valuedx_student.txt","r") as f2:         # read data
    rec=f2.readline()
    while rec != "":
        field = rec.split(" ")
        if int(field[1])>2:
            print("name ",field[0]," pass")
        rec = f2.readline()
