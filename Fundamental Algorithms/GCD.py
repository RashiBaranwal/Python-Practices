# Method 1
def findgcd(x,y):
    while(y):
        x,y = y,x%y
    return x

a = 60
b = 48

print("The gcd of 60 and 48 is: ",end="")
print(findgcd(60,48))    

# Method 2

import math

print("The gcd of 60 and 48 is: ",end="")
print(math.gcd(60,48))