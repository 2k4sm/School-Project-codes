import mariadb

try:
    con = mariadb.connect(host = "localhost",username = "sm2k4", database = "vehiclesales", passwd = "1234")
    print(f"Successfully connected to the database with connection ID:{con.connection_id}")
except:
    print("There is some problem in connecting with the database...")

cursor = con.cursor()

def tableinsert():

    '''
    This is used to insert into the table...
    '''

    tabname = str(input("Enter the table name:"))

    sno = str(input("Enter the seriel number of vehicle:"))
    vehname = str(input("Enter the name of the vehicle:"))
    vehtype = str(input("Enter the type of vehicle:"))
    vehcolor = str(input("Enter the color of the vehicle:"))
    custno = str(input("Enter the customer number:"))

    filldet = f"""insert into {tabname} values ('{sno}', '{vehname}', '{vehtype}', '{vehcolor}', '{custno}');"""
    
    tabexist = f"""show tables;"""
    cursor.execute(tabexist)
    tabexist = cursor.fetchall()
    
    for i in tabexist:
        if i == tabname:
            try:
                cursor.execute(filldet)
                con.commit()
                print(f"Data inserted to table {tabname} successfully..")
                break
            except:
                print("Some error occured while inserting data...")
                break
    else:
        print("The table you are trying to insert does exist...")
    con.close()
