
def wrdcnt():
    file = open("text_file.txt","r")
    cont = file.read()
    words = 0
    for i in cont:
        if i.isspace():
            words+=1
        elif i == ".":
            words+=1
        else:
            continue
    return words
    file.close

print(f"The total number of words in the file are: {wrdcnt()}")
