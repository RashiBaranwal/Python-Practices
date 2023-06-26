# Method 1
numbers = [9, 34, 11, -4, 27]
# find the maximum number
max_number = max(numbers)
print(max_number)

# Method 2

# Python code to get the maximum element from a set
def MAX(sets):
    return max(sets)


sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(MAX(sets))

# Method 3

# Python code to get the minimum element from a set
def MIN(sets):
    return (min(sets))


sets = set([4, 12, 10, 9, 4, 13])
print(MIN(sets))

#Method 4.
#Initialize array
arr = [25, 11, 7, 75, 56];

#Initialize max with first element of array
max = arr[0];

#Loop through the array
for i in range(0, len(arr)):
 #Compare elements of array with max
   if arr[i] > max:
     max = arr[i];

print("Largest element present in given array: " + str(max));