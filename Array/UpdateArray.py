from array import*
array1 = array('i',[10,20,30,40,50])
array1[2] = 90

for x in array1:
    print(x)
    
# 2nd Program
import array as arr
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
print("Before update: ")
print(numbers)
# changing first element
print("After updates: ")
numbers[0] = 0
print(numbers)

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)

print(len(numbers))
