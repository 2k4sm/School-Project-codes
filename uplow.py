# Define the function to accept a string and calculate uppercase and lowercase characters.

def uplow(str1):
    up =0
    low=0
    #iterating through each character.
    for i in str1:
        #checking each character
        if i.isupper():
            up+=1
        if i.islower():
            low+=1
    
    return up,low
string1 = str(input("Enter the string:"))
print(f"The number of uppercase and lowercase characters are:{uplow(string1)}")
