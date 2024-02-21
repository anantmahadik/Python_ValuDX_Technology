import day9_Composition_One

class B:
    def b(self):
        a1 = day9_Composition_One.A()
        a1.a()
        print("derived b")
b1 = B()
b1.b()
