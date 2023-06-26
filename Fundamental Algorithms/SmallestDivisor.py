# Method 1
num = int(input("Enter a number: "))

for i in range(2,num+1):
    if num%i == 0:
        print("The smallest divisor is: ",i)
        break
    
# Method 2
n = int(input("Enter an integer: "))
a=[]
for i in range(2,n+1):
    if(n%i == 0):
        a.append(i)
a.sort()
print("Smallest divisor is: ",a[0])            