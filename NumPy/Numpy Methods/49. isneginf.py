# The numpy.isneginf() function tests element-wise whether it is negative infinity or not, and returns the result as a boolean array. 

import numpy as np

print("Negative :\n", np.isneginf(0))
print()
print("Negative :\n", np.isneginf(np.nan))
print()
print("Negative :\n", np.isneginf(np.inf))
print()
print("Negative :\n",np.isneginf(np.NINF))
print()

x=np.array([-np.inf,0.,np.inf])
y=np.array([2,2,2])
print("Checking for negativity :", np.isneginf(x,y))