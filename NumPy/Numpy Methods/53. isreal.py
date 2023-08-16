# numpy.isreal(array) : Test element-wise whether it is a real number or not(not infinity or not Not a Number) and return the result as a boolean array. 

import numpy as np
d=np.arange(10).reshape(2,5)
print("Original Array :\n",d)
print("Real Array :\n",np.isreal(d))
print()
print("Real Array :\n ",np.isreal([1j+0,1]))
print()
print("Real Array :\n ",np.isreal([1,3]))
