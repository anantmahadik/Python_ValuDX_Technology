class retailer:
    def __init__(self,a):
        self.x= a  #initialize value to instances

    def putdata(self):
        self.x = input("enter item : ")

#main

n = int(input("enter how many items : "))
li=[]
for i in range(0,n):

    obj = retailer()
    obj.putdata()
    li.append(obj)

print(len(li)*75)



