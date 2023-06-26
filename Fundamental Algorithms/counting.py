n = int(input("Enter the number"))
count = 0
while(n>0):
    count = count+1
    n = n//10
    # print(n)
print("The number of digits in the number are: ",count)    

num = int(input("Enter a number: "))
print(len(str(num)))