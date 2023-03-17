import mariadb

try:
    con = mariadb.connect(host = "localhost",username = "sm2k4", database = "vehiclesales", passwd = "1234")
    print(f"Successfully connected to the database with connection ID:{con.connection_id}")
except:
    print("There is some problem in connecting with the database...")

cursor = con.cursor()


def tablecreate():
    '''
     This creates a table if not exist in the database...
     It cheks for the tables present and creates the specified table if not exist...
    '''
    tablename = str(input("Enter the table name to create: "))
    # querries
    fetchtable = '''show tables;'''
    tablecreator = f'''create table {tablename} (SNo varchar(5), VehName varchar(20), VehType varchar(20), VehColour varchar(20), CustNo varchar(20));'''

    cursor.execute(fetchtable)

    tablexist = cursor.fetchall()

    if len(tablexist) == 0:
        print(f"The Table with name {tablename} is created")
        cursor.execute(tablecreator)
    else:
        for i in tablexist:
            if i == tablename:
                print(f"The table {tablename} already exists...")
                break
        else:
            try:
                cursor.execute(tablecreator)
                print(f"The Table with name {tablename} is Created")
            except mariadb.OperationalError:
                print(f"This table {tablename} already exists...")

    
    con.close()