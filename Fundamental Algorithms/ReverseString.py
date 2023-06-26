def reverse_str(str):
    str1 = str[::-1]
    return str1

str = input("Enter string : ")
temp = str
print("Original string: ",str)
print("After reversing string: ",reverse_str(str))
