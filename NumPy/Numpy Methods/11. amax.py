import numpy as np
arr=np.arange(6)
print("Original Array :",arr)

arr1=np.arange(10).reshape(2,5)
print("2D Array :",arr1)

# When axis=None
print("\nMax of arr, axis = None : ", np.amax(arr))

# When axis=0
print("\nMax of arr, axis = 0 : ", np.amax(arr1,axis=0))

# When axis=1
print("\nMax of arr, axis = 1 : ", np.amax(arr1,axis=1))

