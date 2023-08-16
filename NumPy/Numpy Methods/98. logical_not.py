# numpy.logical_not(arr, out=None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None, ufunc ‘logical_not’) : 
# This is a logical function that computes the truth value of NOT arr element-wise.

import numpy as np
d=[1,0,False,5,True]
d1=[9,4,0,True,False]
d2=np.logical_not(d)
d3=np.logical_not(d1)

print("Logical not :\n",d2)
print("Logical not :\n",d3)