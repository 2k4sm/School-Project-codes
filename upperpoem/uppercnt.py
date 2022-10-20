
def uppernum():
    file = open("poem.txt","r")
    cont = file.read()
    uppernum = 0
    for i in cont:
        if i.isupper():
            uppernum+=1
        else:
            continue
    file.close()
    return uppernum
print(f"The number of uppercase letters in the file 'poem.txt' are {uppernum()}")

