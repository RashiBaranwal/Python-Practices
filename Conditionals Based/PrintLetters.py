# Print all the letters in the string except ‘o’ and ‘t’?
i = 0
str1 = 'Hello to the world of Python'

while i <len(str1):
    if str1[i] == 'o' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter : ',str1[i])
    i += 1