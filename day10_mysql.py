import postgresql.connector


def display():
    sql = "select * from bookd"
    rec = cr.execute(sql)
    print(rec)
    con = postgresql.connector.connect(host="localhost",user="postgres",password="1234",database="Demo")

cr = con.cursor()
display()
