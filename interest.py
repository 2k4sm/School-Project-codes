# Defining the simple interest function.
def simpleI(p,r,t=1):
    return (p*r*t)/100
# Defining the compound interest function.
def compoundI(p,r,t=1):
    return (p*(1+r/100)**t)-p
# Taking principle,rate and time as user input../time is defaulted to 1 if no user input given.    
x = int(input("Enter the principle amount:"))
y = int(input("Enter the rate of interest:"))
z = int(input("Enter the time of interest calculation:"))

#Print simple interest.
print(f"The simple interest calculated is: {simpleI(x, y,z)}")
#Print compound interest.
print(f"The compound interest calculated is:{compoundI(x, y,z)}")
