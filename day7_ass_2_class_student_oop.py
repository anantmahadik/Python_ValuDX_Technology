# define a class students having roll no, name and marks of english, maths ,scince, sub find avg of
# each sttudent and avg
# of each sub of entire division
class student:
    rollno = 0
    name = " "
    english = 0
    maths = 0
    science = 0
    t_english = 0
    t_maths = 0
    t_science = 0

    def getdata(self):
        self.rollno=int(input("enter roll number : "))
        self.name = input("enter the name : ")
        self.english=int(input("enter english marks : "))
        self.maths=int(input("enter maths marks : "))
        self.science=int(input("enter science marks : "))

    def avg_student(self):
        print("player name : ",self.name," student avg marks is : ",(self.english+self.maths+self.science)/3)
        student.t_english += self.english
        student.t_maths += self.maths
        student.t_science += self.science

    def sub_avg(self,n):
        print(student.t_english/n)
        print(student.t_maths/n)
        print(student.t_science/n)


#main()

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



