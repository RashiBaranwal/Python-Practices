# Method 1
def Fibonacci(n):
    if n<=0:
        print("Incorrect input")
    elif n ==1:
        return(0)
    elif n == 2:
        return(1)
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))

num = int(input("Enter the Nth term : "))
print(Fibonacci(num)) 

# Method 2
def fibonacci(n):
    a = 0
    b = 1
    if n<= 0:
        print("Incorrect input")
    elif n==1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b   


numb = int(input("Enter the Nth term : "))
print(fibonacci(numb))    
        
       