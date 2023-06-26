num = int(input("Enter a number: "))
temp = num
reverse = 0
while(num>0):
    digit = num %10
    reverse = reverse*10+digit
    num = num//10
print("The reverse of given num is : ",reverse)

if temp == reverse:
    print("The number is Palindrone!")
else:
    print("The number is not a palindrone!")