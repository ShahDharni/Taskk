import numpy as np
 
# Using a 3D array
geek_array = np.arange(16).reshape(2, 2, 4)
print("geek array  :\n", geek_array)
 
print("\nfunc sum : \n ", np.apply_over_axes(np.sum, geek_array, [1, 1, 0]))
 
print("\nfunc min : \n ", np.apply_over_axes(np.min, geek_array, [1, 1, 0]))