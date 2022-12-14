import mariadb as md

con = md.connect(host = 'localhost',user ='root',passwd = 'heaven')
curs = con.cursor()

try:
    curs.execute(f"create database AISSCE2023XII")
    print(f"Database created")
    curs.execute(f"use AISSCE2023XII")
    curs.execute(f"create table Book (BookNo int, BookName varchar(20),Price int)")
    print("Table created.")
except md.ProgrammingError:
    print(f"Database already exists.")
    try:
        curs.execute(f"use AISSCE2023XII")
        curs.execute(f"create table Book (BookNo int, BookName varchar(20),Price int)")
        print("Table created.")
    except md.OperationalError:
        print(f"Table already exixts.")

