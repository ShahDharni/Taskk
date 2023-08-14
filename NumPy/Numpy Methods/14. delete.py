# Boolean Masking :- known as Boolean Indexing it is feature in Python Numpy that allows for the filtering of values in numpy array.

import numpy as np

#Working on 1D
arr = np.arange(12).reshape(3, 4)
print("arr : \n", arr)
print("Shape : ", arr.shape)

# deletion from 2D array
d = np.delete(arr, 1, 0)

print("\ndeleting arr 2 times : \n", d)
print("Shape : ", d.shape)

# deletion from 2D array
d = np.delete(arr, 1, 1)

print("\ndeleting arr 2 times : \n", d)
print("Shape : ", d.shape)



print()

# Boolean Masking/Boolean Indexing
arr=np.arange(5)
print("Original Array",arr)
mask=np.ones(len(arr),dtype=bool)

## here np.ones(len(arr),dtype=bool) is equivalent to np.delete([0,2,4], axis=0)
print(mask)
mask[[0,2]]= False
print("Mask",mask)

