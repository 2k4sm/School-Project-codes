import mariadb as md

con = md.connect(host = 'localhost',user = 'root',passwd = 'heaven',database = 'AISSCE2023XII')

curs = con.cursor()

cond = input("Enter Delete Condition:")

curs.execute(f"select * from Book where {cond}")
delt = curs.fetchall()
for i in delt:
    print(f"Deleted Book: {i}")
curs.execute(f"delete from Book where {cond}")
con.commit()
exit(0)

