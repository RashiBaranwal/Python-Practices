#Method 1
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a,b = b,a
print("After swapping")
print("a=",a,"b=",b)

#Method 2
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a = a+b
b = a - b
a = a-b
print("After swapping")
print("a=",a,"b=",b)

#Method 3
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a = a*b
b = a/b
a = a/b
print("After swapping")
print("a=",a,"b=",b)

#Method 4
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
temp = a
a = b
b = temp
print("After swapping")
print("a=",a,"b=",b)

#Method 5
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a = (a+b)-(b==a)
print("After swapping")
print("a=",a,"b=",b)

#Method 6
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a = a^b
b = a^b
a = a^b
print("After swapping")
print("a=",a,"b=",b)

#Method 7
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print("Before swapping")
print("a=",a,"b=",b)
a = (a and b) + (a or b)
b = a + (~b) + 1
a = a + (~b) + 1
print("After swapping")
print("a=",a,"b=",b)
