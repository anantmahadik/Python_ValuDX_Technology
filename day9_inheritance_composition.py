class A:
    def a(self):
        print("base a")
class B(A):
    def b(self):
        print("derived b")

b1 = B()
b1.b()
b1.a()
