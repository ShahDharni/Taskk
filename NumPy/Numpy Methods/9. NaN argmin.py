# numpy.nanargmin(array, axis = None)

# array : Input array to work on 
# axis  : [int, optional]Along a specified axis like 0 or 1



import numpy as geek

array = [geek.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)

array2 = geek.array([[geek.nan, 4], [1, 3]])

print("\nIndices of min in array1 : ",
	geek.nanargmin(array))

print("\nINPUT ARRAY 2 : \n", array2)
print("\nIndices of min in array2 : ",
	geek.nanargmin(array2))

print("\nIndices at axis 1 of array2 : ",
	geek.nanargmin(array2, axis = 1))
