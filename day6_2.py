# recursion fun call itself
def total(n):
    if n == 0:
        return 0
    else:
        n=int(input("enter num : "))
        return  n+total(n)
n = 1
s=total(n)
print(s)

