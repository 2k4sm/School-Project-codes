def fact():
    num=int(input("Enter your number:"))
    fact=num
    while num != 1:
        num=num-1
        fact=fact*num
    return fact
print(f"The factorial of the number is :{fact()}")
