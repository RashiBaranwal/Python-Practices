import numpy as np

#The original NumPy array
new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
print("Original Array is :",new_arr)
#reversing using flip() Method
res_arr=np.flip(new_arr)
print("Resultant Reversed Array:",res_arr)

#Method 2
#The original NumPy array
new_arr=np.array(['A','s','k','P','y','t','h','o','n'])
print("Original Array is :",new_arr)
#reversing using flipud() Method
res_arr=np.flipud(new_arr)
print("Resultant Reversed Array:",res_arr)

#Method 3
#The original NumPy array
new_arr=np.array([1,3,5,7,9])
print("Original Array is :",new_arr)
#reversing using array slicing
res_arr=new_arr[::-1]
print("Resultant Reversed Array:",res_arr)