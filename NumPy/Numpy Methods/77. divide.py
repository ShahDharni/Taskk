# numpy.divide(arr1, arr2, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) :
# Array element from first array is divided by elements from second element (all happens element-wise). 
# Both arr1 and arr2 must have same shape and element in arr2 must not be zero; otherwise it will raise an error.

import numpy as np
d=[22,33,21,23,12]
d1=[11,2,3,23,3]
print(np.divide(d,d1))