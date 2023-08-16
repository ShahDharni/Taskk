# The numpy.isfinite() function tests element-wise whether it is finite or not(not infinity or not Not a Number) and return the result as a boolean array

import numpy as np
print("Finite :\n", np.isfinite(0))
print()
print("Finite :\n", np.isfinite(np.nan))
print()
print("Finite :\n", np.isfinite(np.inf))
print()
print("Finite :\n",np.isfinite(np.NINF))
print()

x=np.array([-np.inf,0.,np.inf])
y=np.array([2,2,2])
print("Checking for negativity :", np.isfinite(x,y))



## Another Example
d=np.arange(20).reshape(4,5)
print("Original Array :\n",d)
print()
print("Finite Array :\n",np.isfinite(d))
print()

d1=[[1j],
    [np.nan]]
print("Finite Array :\n",np.isfinite(d1))
