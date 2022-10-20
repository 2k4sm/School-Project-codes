#Taking string as user input.
string1 = str(input("Enter the string to be evaluated:"))
# pre defining the calculating constants.
alpha = 0
upper = 0
lower = 0
digit = 0
# defining the logic for calculating:
#       1.alphabets
#       2.uppeercase
#       3.Lowercase
#       4.Digits.    
   
for i in string1:
    if i.isalpha():
        alpha+=1
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
    if i.isdigit():
        digit+=1
# Print statement to Print out calculated objects.
print(f"Number of alphabets: {alpha}\n",
      f"Number of uppercase: {upper}\n",
      f"Number of lowercase: {lower}\n",
      f"Number of digits: {digit}")
