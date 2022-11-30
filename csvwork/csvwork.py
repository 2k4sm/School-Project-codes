import csv

def write():
    # writing into csv files.

    file = open("csvfile.csv",'w')
    headings = ['itemNo','itemName','quantity','price']
    rows = []
    doAdd = "y"
    while doAdd == "y":
        no = input("Enter itemNo:")
        name = input("Enter itemName:")
        quantity = input("Enter Quantity:")
        price = input("Enter Price:")
        row = [no,name,quantity,price]
        rows.append(row)
        doAdd =input("Want to Add(y/n):")
    
    
    writer = csv.writer(file)
    writer.writerow(headings)
    writer.writerows(rows)
    file.close()

def read():
    # read from csv file.
    file = open("csvfile.csv",'r')
    reader = csv.reader(file)
    print("Reading CSV File:")
    headings = next(reader)

    print("File Format:",headings)
    rows = []

    for i in reader:
        for j in i:
            print(j,end=',')
        print()

def append():
    # appending  into existing csv files.

    file = open("csvfile.csv",'a')
    rows = []
    doAdd = "y"
    while doAdd == "y":
        no = input("Enter itemNo:")
        name = input("Enter itemName:")
        quantity = input("Enter Quantity:")
        price = input("Enter Price:")
        row = [no,name,quantity,price]
        rows.append(row)
        doAdd =input("Want to Add(y/n):")
    
    
    writer = csv.writer(file)
    writer.writerows(rows)
    file.close()


def scan():
    # Scanning from a existing CSV file.
    file = open("csvfile.csv",'r')
    ino = input("Enter the itemNo to search for:")
    reader = csv.reader(file)    
    for i in reader:
        if ino == i[0]:
            print("The Searched column is:",i)
            

#Driver Code

write()    
append()
read()
scan()
