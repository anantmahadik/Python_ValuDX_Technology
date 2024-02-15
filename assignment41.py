#list = [8, 7, 2 , 5, 3,1 ]
#print all the pairs with the given sum = 10

list = [8, 7, 2, 5, 3, 1]
target_sum = 10

pairs = []

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] + list[j] == target_sum:
            pairs.append((list[i], list[j]))

print("Pairs with sum 10:", pairs)
