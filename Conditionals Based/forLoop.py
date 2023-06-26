str = "Python"
for i in str:
    print(i)
    
list = [10,30,23,43,65,12]
sum = 0
for i in list:
    sum = sum + i
print("The sum is ",sum)    

list1 = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list1:
    c = n *i
    print(c)
    
p = int(input("Enter the number"))
for i in range(1,11):
    c = p*i    
    print(p,"*",i,"=",c)
    
for q in range(1, 6):
    print('*' * q)
