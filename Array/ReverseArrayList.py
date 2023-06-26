# Method 1
arr = [1,2,3,4,5]
print("Original array: ")
for i in range(0,len(arr)):
    print(arr[i])
print("Array in reverse order: ")

# Loop through the array in reverse order
for i in range(len(arr)-1,-1,-1):
    print(arr[i])    

# Method 2
arri = [11,22,33,44,55]
print("Array is: ",arri)

res = arri[::-1]
print("Resultant new reversed array: ",res)

# Method 3
arr = [11,22,33,44,55]
print("Before reversal Array is : ",arr)

arr.reverse()
print("After reversing Array: ",arr)

# Method 4
ar = [12,34,56,78]
print("Original Array is: ",ar)

result = list(reversed(ar))
print("Resultant new reversed Array: ",result)