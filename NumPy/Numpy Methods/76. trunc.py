# The numpy.trunc() is a mathematical function that returns the truncated value of the elements of array. 
# The trunc of the scalar x is the nearest integer i which, closer to zero than x. 
# This simply means that, the fractional part of the signed number x is discarded by this function.

import numpy as np
d=[0.5,1.5,2.3,4.6,2.0,5.6,7,8.9]
print("Trunc : \n",np.trunc(d))

d1=[4.3,5.6,7.8,8.9,3.5,4.6]
print("Trunc : \n",np.trunc(d1))
