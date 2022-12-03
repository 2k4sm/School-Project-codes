import time

bookstr = []
def welcome():
    print("\nWelcome to Book Library.\n")
    print("Menu:")
    print(
        "1.Add Book\n"
        "2.Remove Last Added Book\n"
        "3.Display Books\n"
        "4.Exit\n"

        )
        
def main():
    menu = input("Enter The command from menu:")
    if menu =="1":
        push()
    elif menu =="2":
        print("Last added element removed.")
        pop()
    elif menu == "3":
        if len(bookstr) == 0:
            print("Empty library")
        else:
            print("The books are:")
            for i in bookstr:
                print(i[1])
    elif menu == "4":
        print("Exiting the program:")
        exit()
    else:
        print("Invalid command.")

def push():
    bookno = input("Enter Book-Number:")
    book = input("Enter Book-Name:")
    bookdet = [bookno, book]
    bookstr.append(bookdet)
    #print(bookstr)

def pop():
    try:
        bookstr.pop()
        #print(bookstr)
    except IndexError:
        print("There is nothing to remove.")

#Driver code:

while True:
    time.sleep(0.2)
    welcome()
    main()



