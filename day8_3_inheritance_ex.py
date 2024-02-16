class student:
    def getdata(self):
        self.r=int(input("enter roll no : "))
        self.name=int(input("enter name : "))
        self.__sport()
    def putdata(self):
        print("roll no : ",self.r,"name : ",self.name)

    def __sport(self):
        game=input("enter sport name : ")
        print("gme = ",game)

class test(student):     # single inheritance
    def get_marks(self):
        self.m=int(input("enter marks : "))
        if self.m>35:
            print("pass")
        else:
            print("fail")

t=test()
t.getdata()
t.putdata()

