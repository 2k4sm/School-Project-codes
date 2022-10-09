import pickle
# a function to create/open a binary file and write content to it.
def write_bin():
    fo = open("binary.dat","wb")
    # number of file entry as a user input.
    ent = int(input("How many datas to store?: "))
    i = 0
    # loops through to get  userinput and dumps it in the binary file as a list.
    while i < ent :
        a = input("Name: " )
        b = int(input("Roll.no: "))
        c = int(input("Marks: "))
        dat = [a,b,c]
        pickle.dump(dat,fo)
        i+=1
    fo.close()
# function to read the content of a binary file.
def read_bin():
    fo = open("binary.dat","rb")
    # while true loops through and tries to load the file content from the binary file unless a exception is encountered.
    while True: 
        try:
            x = pickle.load(fo)
            t = True
            # while true loops through the file content and prints the file content in the specified format.
            while t:
                name = x[0]
                roll = x[1]
                marks = x[2]
                print(f"Name of candidate: {name}\nRoll.no of candidate:{roll}\nMarks of candidate: {marks}")
                t =False
        # if exception is encountered breaks out of the loop and stops the function.
        except EOFError:
            break
    fo.close()
# function to search the desired content of a file.
def search_bin():
    name = str(input("Enter the name to search for:"))
    fo = open("binary.dat","rb")
    # while true loops through and tries to load the file content from the binary file unless a exception is encountered.
    while True: 
        try:
            x = pickle.load(fo)
            t = True
            # while true loops through the file content and prints the file content in the specified format.
            while t:
                if name == x[0] :
                    print(f"The Searched Item Is:{x}")
                    break
                else:
                    break
        # if exception is encountered breaks out of the loop and stops the function.
        except EOFError:
            break
    fo.close()

#Driver Code
write_bin()
read_bin()
search_bin()