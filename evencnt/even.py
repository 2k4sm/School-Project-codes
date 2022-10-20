def sumev():
    file = open("story.txt","r")
    cont = file.read()
    sumev = 0
    for i in cont:
        if i.isdigit() and int(i)%2 == 0 :
            sumev+=int(i)
        else:
            continue
    file.close()
    return sumev       
print(f"The sum of all even numbers is: {sumev()}")
