# The numpy.isposinf() function tests element-wise whether it is positive infinity or not and returns the result as a boolean array. 

import numpy as np

print("Positive :\n", np.isposinf(0))
print()
print("Positive :\n", np.isposinf(np.nan))
print()
print("Positive :\n", np.isposinf(np.inf))
print()
print("Positive :\n",np.isposinf(np.NINF))
print()

x=np.array([-np.inf,0.,np.inf])
y=np.array([2,2,2])
print("Checking for negativity :", np.isposinf(x,y))