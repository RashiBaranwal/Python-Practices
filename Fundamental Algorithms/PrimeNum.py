x = int(input("Enter a number: "))

for i in range(2,x+1):
    prime = True
    for j in range(2,i):
        if(i%j==0):
            prime = False
    if(prime == True):
        print(i)        