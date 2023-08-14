import numpy as np

arr = np.arange(5)
print("1D arr : \n", arr)
print("Shape : ", arr.shape)

# value = 9
# index = 1
# Insertion before first index
d1 = np.insert(arr, 1, 9)
print("\nArray after insertion : ", d1)
print("Shape : ", d1.shape)


# Working on 2D array
arr = np.arange(12).reshape(3, 4)
print("\n\n2D arr : \n", arr)
print("Shape : ", arr.shape)

d = np.insert(arr, 1, 9, axis = 1)
print("\nArray after insertion : \n", d)
print("Shape : ", d.shape)
