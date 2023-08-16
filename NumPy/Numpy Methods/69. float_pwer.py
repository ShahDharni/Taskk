# numpy.float_power(arr1, arr2, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) :
# Array element from first array is raised to the power of element from second element(all happens element-wise). Both arr1 and arr2 must have same shape.
# float_power differs from the power function in that integers, float16, and float32 are promoted to floats with a minimum precision of float64 such that result is always inexact. 
# This function will return a usable result for negative powers and seldom overflow for +ve powers.

import numpy as np
d=[2,2,2,2,2]
d1=[1,2,3,4,5]

res=np.float_power(d,d1)
print("result : \n ",res)