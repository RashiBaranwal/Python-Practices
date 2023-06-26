#Without using recursion
num = int(input("Enter a number: "))

factorial = 1
if num<0:
    print("Sorry,factorial does not exist for this! ")
elif num == 0:
    print("Factorial of 0 is 1 ")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("The favtoral of the number ",num ,"is ",factorial)    
print(' ')

#Using recursion
def factorial(num):
    if num == 1:
       return 1
    else:
       return (num*factorial(num-1))
 

num = int(input("Enter a number: "))
print("Factorial is: ", factorial(num))
