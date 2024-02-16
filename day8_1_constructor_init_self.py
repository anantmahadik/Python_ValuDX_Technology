class student:
    def __init__(self,a,b):
        self.x=a    #initialize value to instances
        self.y=b
    def putdata(self):
        print("x",self.x,"y",self.y)

#main
a=int(input("enter a "))
b=int(input("enter b "))

s=student(a,b)
s.putdata()
