import numpy as np
d=np.arange(15).reshape(3,5)
print("Original Array :\n",d)

print()
print("Ravel :\n",d.ravel())
print()
## Here we can say that ravel is equivalent to reshape(-1)
print("reshape :\n",d.reshape(-1))