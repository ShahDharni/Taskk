import numpy as np

print("NaN :\n", np.isnan(0))
print()
print("NaN :\n", np.isnan(np.nan))
print()
print("NaN :\n", np.isnan(np.inf))
print()
print("NaN :\n",np.isnan(np.NINF))
print()

x=np.array([-np.inf,0.,np.inf])
y=np.array([2,2,2])
print("Checking for negativity :", np.isnan(x,y))