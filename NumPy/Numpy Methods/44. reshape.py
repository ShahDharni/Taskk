import numpy as np
d=np.arange(8)
print("Original Array :",d)

d1=np.arange(8).reshape(2,4)
print("Reshape Array :\n",d1)

d2=np.arange(8).reshape(4,2)
print("Reshape Array :\n",d2)

d3=np.arange(8).reshape(2,2,2)
print("Reshape Array :\n",d3)
