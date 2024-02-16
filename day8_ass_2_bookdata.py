class book:
    def getdata(self):
        self.author=input("enter author : ")
        self.title=input("enter title : ")
        self.prise=int(input("enter price : "))

    def putdata(self):
        print("author : ",self.author,"title : ",self.title,"price ",self.prise,"stock ")

class bookinfo(book):
    def getdata1(self):
        self.stocks=int(input("enter stock : "))
    def putdata(self):

        print("author : ",self.author,"title : ",self.title,"price ",self.prise,"stock ",self.stocks)

for i in range(0,3):

    b=bookinfo()
    b.getdata()
    b.getdata1()
    b.putdata()

