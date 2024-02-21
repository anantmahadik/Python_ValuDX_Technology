username = ""
with open("student.txt","w") as f1:       # write data
    while username != "end":
        username = input("enter the username : ")
        if username == "end":
            break
        name = input("enter the name : ")
        surname = input("enter the surname : ")
        gender = input("enter the gender : ")
        year = int(input("enter the year : "))
        f1.write(username+" "+name+" "+surname+" "+gender+" "+str(year)+'\n')


