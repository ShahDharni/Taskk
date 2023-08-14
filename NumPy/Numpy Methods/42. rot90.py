import numpy as np
d=np.arange(10).reshape(2,5)
print("d :\n",d)

print()
d1=np.rot90(d)
print("d1 :\n",d1)

print()
d2=np.rot90(d,4)
print("d2 :\n",d2)