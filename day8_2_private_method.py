class student:
    __x=0                   # private var
    def __init__(self,a,b):
        self.x=a    #initialize value to instances
        self.y=b
    def __fun(self):
        print("private fun ")
    def putdata(self):
        c=90
        print("x",self.x,"y",self.y)
        self.__fun()
        return  c
#main
a=int(input("enter a "))
b=int(input("enter b "))

s=student(a,b)
c1=s.putdata()
print(c1)
#print(__x) cant access is private

