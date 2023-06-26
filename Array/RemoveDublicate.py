# Method 1
a = [1,1,1,3,4,5,5,5,5,7,7,7,9,9]
for i in range(len(a)-1,0,-1):
   if a[i] == a[i-1]:
    del a[i]
print(a)

# Method 2

a=[1,1,1,3,4,5,5,5,5,7,7,7,9,9]
i =0
l = len(a)-1
while i < l :
    if a[i] == a[i+1]:
      del a[i+1]
      l -= 1
    else:
      i += 1
print(a)

#Method 3

from collections import OrderedDict
a = [2, 3, 3, 2, 5, 4, 4, 6]
b = list(OrderedDict.fromkeys(a))
print(b)

# Method 4

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : ", test_list)
# using naive method to remove duplicates from
list
res = []
for i in test_list:
    if i not in res:
       res.append(i)
# printing list after removal
print ("The list after removing duplicates : ", res)



