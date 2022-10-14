import pickle
# a function to create/open a binary file and write content to it.
def write_bin():
    fo = open("binary.dat","wb+")
    # number of file entry as a user input.
    ent = int(input("How many datas to store?: "))
    i = 0
    # loops through to get  userinput and dumps it in the binary file as a list.
    arr = []
    while i < ent :
        a = input("Name: " )
        b = int(input("Roll.no: "))
        c = int(input("Marks: "))
        dat = [a,b,c]
        arr.append(dat)
        i+=1
    pickle.dump(arr,fo)
    fo.close()
# function to read the content of a binary file.
def read_bin():
    fo = open("binary.dat","rb+")
    # while true loops through and tries to load the file content from the binary file unless a exception is encountered.
    while True: 
        try:
            x = pickle.load(fo)
            for i in x:
                t = True
                # while true loops through the file content and prints the file content in the specified format.
                while t:
                    name = i[0]
                    roll = i[1]
                    marks = i[2]
                    print(f"Name of candidate: {name}\nRoll.no of candidate:{roll}\nMarks of candidate: {marks}")
                    t =False
            # if exception is encountered breaks out of the loop and stops the function.
        except EOFError:
            break
    fo.close()
# function to search the desired content of a file.
def update_bin():
    old = input("Enter the old data to change:")
    new = input("Enter the new  data to update:")
    fo = open("binary.dat","ab+")
    while True:
        try:
            x = pickle.load(fo)
            # changes the old data with the new
            for i in x:
                for j in i:
                    if j == old:
                        #j = new
                        index = i.index(j)
                        i[index] = new
            pickle.dump(x,fo)
        except EOFError:
            break
    fo.close()

write_bin()
read_bin()
update_bin()
read_bin()