# numpy.logical_or(arr1, arr2, out=None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None, ufunc ‘logical_or’) :
#  This is a logical function and it helps user to find out the truth value of arr1 OR arr2 element-wise.
#  Both the arrays must be of same shape.

import numpy as np
d=[1,0,False,5,True]
d1=[9,4,0,True,False]
d2=np.logical_or(d,d1)
print("Logical or :\n",d2)