import numpy as np

## Two array
array1=np.array([1,4])
array2=np.array([3,6])
print(array1)
print(array2)
print()
comb_array = np.array(np.meshgrid(array1, array2)).T.reshape(-4, 2)
print(comb_array)

print()

## Three arrays
array1=np.array([1,4,3])
array2=np.array([3,6,2])
array3=np.array([1,4])
print(array1)
print(array2)
print()
comb_array = np.array(np.meshgrid(array1, array2, array3)).T.reshape(-4, 3)
print(comb_array)

print()


## Four arrays
array1=np.array([1,4])
array2=np.array([3,6])
array3=np.array([1,4])
array4=np.array([3,2])

print(array1)
print(array2)
print(array3)
print(array4)
print()
comb_array = np.array(np.meshgrid(array1, array2, array3,array4)).T.reshape(-1,4)
print(comb_array)