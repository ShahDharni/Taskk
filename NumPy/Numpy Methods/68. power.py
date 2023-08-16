# numpy.power(arr1, arr2, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) :
# Array element from first array is raised to the power of element from second element(all happens element-wise). 
# Both arr1 and arr2 must have same shape and each element in arr1 must be raised to corresponding +ve value from arr2; otherwise it will raise a ValueError.

import numpy as np
d=[2,2,2,2,2]
d1=[1,2,3,4,5]

res=np.power(d,d1)
print("result : \n ",res)


