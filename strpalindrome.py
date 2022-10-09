def strinv(str1):
    rev = str1[::-1]
    if str1 == rev:
        return 0
    else:
        return 1

string = str(input("Enter the string to be checked:"))

if strinv(string) == 0:
    print(f"The string {string} is a palindrome.")
else:
    print(f"The string {string} is not palindrome.")
