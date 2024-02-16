class hotel:
    name = " "
    address = " "
    grade = " "
    average_roo_charge = 0
    numbers_of_rooms = 0
    s_grade = []

    def getdata(self):
        self.name = input("enter the name : ")
        self.address = input("enter the address : ")
        self.grade=input("enter the grade : ")
        self.average_roo_charge=int(input("enter the avg room charge : "))
        self.numbers_of_rooms=int(input("enter the number of rooms : "))

    def grade_range(self,grd_name):
        if grd_name in hotel.s_grade:
            print(hotel.s_grade)

    def charge(self,charges):
        if self.average_roo_charge < charges:
            print(self.average_roo_charge)

#main()
obj = hotel()

a = "a"
obj.getdata()
obj.grade_range(a)



n = int(input("enter how many students : "))
li=[]
for i in range(0,n):

    obj = student()
    obj.getdata()
    print(obj.english)
    li.append(obj)
for i in li:
    i.obj.avg_student()
    print("eng ",i.english)
obj.sub_avg(n)


