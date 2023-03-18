import mariadb

try:
    con = mariadb.connect(host = "localhost", username = "sm2k4", password = "1234", database = "vehiclesales")
    print(f"The database successfully connected with session ID: {con.connection_id}")
except:
    print("There is some error connecting with the database.")

cursor = con.cursor()

def tableretr():
    

    tablename = str(input("Enter the table name: "))
    descquerry = f"""desc {tablename};"""
    dataquerry = f"""select * from {tablename};"""
    
    try:

        cursor.execute(descquerry)

        descquerry = cursor.fetchall()

        for i in descquerry:
            print(f"{i[0]:<12}",end="  ||  ")
        print()
        print(("-"*(18*len(descquerry))))

        cursor.execute(dataquerry)
        dataquerry = cursor.fetchall()

        for i in dataquerry:
            for j in i:
                print(f"{j:<12}",end="  ||  ")
            print()
        print()
    except:
        print("Error Occured: Table does not exist.")
        con.close()