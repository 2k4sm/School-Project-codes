import pymysql as cntr

db = cntr.connect(host = 'localhost' , user = 'root' , passwd = 'heaven')
db.autocommit(True)
cur = db.cursor()
cur.execute("create database if not exists book_shop")
cur.execute("use book_shop")
cur.execute("create table stock\
            (Book_No bigint primary key,\
Book_Name varchar(255),\
Author varchar(255),\
Publisher varchar(255),\
Cost_per_Book float,\
Available_Stock bigint,\
qty_purchased bigint,\
purchased_on date)")
cur.execute("create table users(username varchar(255) , password varchar(255) , check (username <> 'ADMIN'))")
cur.execute("create table purchased (Book_no bigint , purchased_on date , foreign key(Book_no) references stock(Book_No))")
cur.execute("create unique index Book_Index on stock(Book_No)")
cur.execute("insert into users values('admin' , 'admin@123')")
print("Database and Tables created successfully")
c = input("Press any key to continue---->")
cur.close()
db.close()
