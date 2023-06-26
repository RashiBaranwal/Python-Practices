# Method 1
from array import*

arr1 = array('i',[10,20,30,40,50])
arr1.remove(40)

for x in arr1:
    print(x)
    
# Method 2
import array as arr  
number = arr.array('i',[10,20,30,90,40]) 
del number[2] 
print(number)