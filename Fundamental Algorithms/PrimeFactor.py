# Method 1
x = eval(input("Enter a number: "))
while x!= 1:
    for i in range(2,x+1):
        if x%i == 0:
            print(i)
            x = x//i
            break
        
# Method 2
        def prime_factors(n):
            #even number divisible
            while n%2 == 0:
                print(2),
                n = int(n/2)
             
             # n becomes odd   
            for i in range(3,n+1,2):
                
                while(n%i == 0):
                    print(i)
                    n = int(n/i)
            if n >2:
              print(n)       
              
n = int(input("Enter the number for calculating its prime factors: ")) 
prime_factors(n)         

# Method 3

n = int(input("Enter an integer: "))
print("Factors are: ")
i = 1
while(i<=n):
    k = 0
    if(n%i==0):
        j = 1
        while(j<=i):
            if(i%j==0):
                k = k + 1
            j = j + 1
        if(k==2):
            print(i)
    i = i + 1                        