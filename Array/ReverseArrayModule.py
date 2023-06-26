import array as a

#The original array
new_arr = a.array('i',[2,4,6,8,10,12])
print("Original Array is: ",new_arr)

#reversing using reverse()
new_arr.reverse()
print("Reversed Array: ",new_arr)

# Method 2

arr = a.array('i',[10,20,30,40])
print("Original Array is: ",arr)

res_arr = a.array('i',reversed(arr))
print("Resulted Revesed Array: ",res_arr)
