def reverse_str(str):
   str1 = str[::-1]
   return str1


str = input("Enter string: ")
temp = str
print("Orignal string: ", str)
print("After reversing string: ", reverse_str(str))
if temp == reverse_str(str):
    print("The string is Palindrom!")
else:
    print("The string is not Palindrom!")
