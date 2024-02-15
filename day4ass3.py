
dict = {'sham': 1000, 'ram': 2000, 'naman': 3000}

fees = int(input("Enter fees: "))

keys = list(dict.keys())
values = list(dict.values())

for i in range(0,len(dict)):
    if fees == values[i]:
        print(keys[i])
