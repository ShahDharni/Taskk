import numpy as np
array1 =[[1, 2], [3, 4]]

array2 = np.prod(array1, axis = 1)

print("product", array2)


# unsigned Integer
x = np.array([1, 2, 3], dtype = np.uint8)
print()
print(np.prod(x).dtype == np.uint)
