# Initialising the dictionary.
dict1 = {}
i = int(input("Enter the number of names to store:"))
# creating a loop to take the name:value pairs as user input.
while i > 0:
    dict2 = {str(input("Enter the name:")):int(input("Enter the roll number:"))}
    dict1.update(dict2)
    i-=1
# To print the dictionary items.
print("The dictionary is:")
print(dict1)

print()

#storing the items in a list
list1 = dict1.items()
#loop to print the list items.
print("The dictionary items are:")
for i in list1:
    print(i)
