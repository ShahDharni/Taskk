import numpy as np
print("Finite :\n", np.isinf(1))
print()

print("Finite :\n", np.isinf(0))
print()
print("Finite :\n", np.isinf(np.nan))
print()
print("Finite :\n", np.isinf(np.inf))
print()
print("Finite :\n",np.isinf(np.NINF))
print()

x=np.array([-np.inf,0.,np.inf])
y=np.array([2,2,2])
print("Checking for Infinity :", np.isinf(x,y))