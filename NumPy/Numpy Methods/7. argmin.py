import numpy as np

array = np.arange(8)
print("INPUT ARRAY : \n", array)
  

print("\nIndices of min element : ", np.argmin(array, axis=0))