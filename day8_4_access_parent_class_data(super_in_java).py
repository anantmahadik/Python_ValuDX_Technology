class company:
    def company_name(self):
        return "fb"

class emp(company):
    def info(self):
        c_name = super().company_name()
        print("emp work at ",c_name)

obj = emp()

obj.info()

