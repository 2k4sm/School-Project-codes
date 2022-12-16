import mariadb as md

con = md.connect(host = 'localhost',user = 'root',passwd = 'heaven',database = 'AISSCE2023XII')

curs = con.cursor()

Bno = int(input("BookNo To Update:"))

newBname = str(input("Enter New BookName:"))
newBprice = int(input("Enter New Price:"))

curs.execute(f"update Book set BookName = '{newBname}',Price = {newBprice} where BookNO = {Bno}")
print(f"Book with Book No {Bno} Updated")
con.commit()
exit(0)
