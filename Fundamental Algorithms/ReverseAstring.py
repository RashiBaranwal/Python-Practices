def reverse_str(str):
    str1 = ""
    for i in str:
        str1 = i+str1 
    return str1

str = input("Enter string: ")    
print("Original string: ",str)
print("After reversing string: ",reverse_str(str))