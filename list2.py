# Assignment 4 :

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

li2 = []

count2 = len(li2)

for li in li2:
    if li not in li2:
        li2.append(li)
    print(li2)
    