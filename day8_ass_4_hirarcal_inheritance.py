class person:
    def code(self, code,name):
        self.a = code
        self.z=name
        print("code", self.a,"name ",self.z)
class account(person):
    def pay(self, pay):
        self.b = pay
        print("pay", self.b)
class admin(person):
    def experience(self, experience):
        self.c = experience
        print("experience", self.c)
class master(account, admin):
    def __init__(self, pay, experience, code,name):

        self.code(code,name)
        self.pay(pay)
        self.experience(experience)
m1 = master(pay="11", experience="5 yr", code=" c",name="xyz")
