import mariadb as md

con = md.connect(host = 'localhost',user = 'root', passwd = 'heaven',database = 'AISSCE2023XII')

curs = con.cursor()

nrec = int(input("Enter the number of records to insert:"))

counter = 1

while counter <= nrec:
    BookNO = int(input("Enter Book number:"))
    BookName = str(input("Enter Book Name:"))
    Price = int(input("Enter the Price of the book:"))
    curs.execute(f"insert into Book values({BookNO},'{BookName}',{Price})")
    con.commit()
    print(f"Record No:{counter} Inserted.")
    counter+=1