import numpy as np

array = np.arange(10).reshape(5, 2)
print("Original array : \n", array)

a = np.mod(array, 4) !=0
print("\nArray Condition a : \n", a)

print("\nElements that satisfy condition a : \n", np.extract(a, array))



b = array - 4 == 1
print("\nArray Condition b : \n", b)

print("\nElements that satisfy condition b : \n", np.extract(b, array))
