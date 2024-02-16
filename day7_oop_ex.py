

class test:
    roll = 0
    name = " "
    def getdata(self):      # current object ref this pointer
        self.name="abc"
        self.roll=int(input("enter roll : ")) # instance / object  variable
        a = 100
        print("hi",a)

        def putdata(self):
            print(self.name,self.roll)

t = test()
t1 = test()
t.getdata()
t1.getdata()


