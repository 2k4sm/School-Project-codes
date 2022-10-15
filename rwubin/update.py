
"""
"Import the pickle module for using dump and load functions."
This is a python program which uses functions to read a binary file or if (not exist creates one for writing.) then reads fom it.

Read:
    *opens the binary file.
    *access the file and decodes it to text format.
    *iterates through it and prints the text in the defined order.
Write:
    *opens the binary file.
    *takes the recieves the text to write and encodes it to binary.
    *then writes the text as binary code in the file.
Update:
    *opens the binary file.
    *takes the "text to search for and its type(num/txt)."
    *iterates through the file and returns the changes the text if found
        else update unsucessful text not found in the file.
"""
"""
function for writing onto the binary file.Cursor starts from the end.
"""
import pickle
def write_bin():
    fo = open("./binary.dat","wb+")
    lines = int(input("Number of records to enter:"))
    arr = []
    i = 0
    while i<lines:
        name = str(input("Enter Name:"))
        roll = str(input("Enter Roll:"))
        mark = str(input("Enter Marks:"))
        dat = [name,roll,mark]
        arr.append(dat)
        i+=1
    pickle.dump(arr,fo)
    fo.close()
"""
function for reading the existing binary file.Cursor starts from the begenning.
"""

def read_bin():
    fo = open("./binary.dat","rb+")
    file = pickle.load(fo)
    print("\nThe records are:")

    for i in file:
        name = i[0]
        roll = i[1]
        mark = i[2]
        print(f"\nName:{name}\nRoll:{roll}\nMark:{mark}\n")
    fo.close()

"""
function to update a record from the records.Cursor starts from the begenning.
"""
def update_bin():
    fo = open("./binary.dat","rb+")
    fo.seek(0)
    file = pickle.load(fo)
    wupd = str(input("Enter What To Update:"))
    for i in file:
        for j in i:
            if j == wupd:
                upd = str(input("Enter Update:"))
                index = i.index(j)
                i[index] = upd
    fo.seek(0)
    pickle.dump(file,fo)
    fo.close()


write_bin()
read_bin()
update_bin()
read_bin()
