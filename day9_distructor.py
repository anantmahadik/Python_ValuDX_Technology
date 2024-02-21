class A:
    x = 0
    y = 0
    def __int__(self,a,b):
        self.x = a
        self.y = b

    def fun1(self):
        print("base a")

    def fun2(self):
        print("derived b",self.a)

    def __del__(self):
        print("delete data...")

a1 = A(1,2)

a1.fun1()
a1.fun2()
