# Assignment 3 :

li = []

i = ""

while i != "end":
    name = input("Enter name : ")
    li.append(name)
    if name == "end":
        break
    
#print(li)

length = len(li)

count = 0

while count!= length/2:
    
    print(li[count])
    count+=1

