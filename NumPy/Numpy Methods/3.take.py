import numpy as np
a=[[1,2,3,9,8],
   [4,6,7,12,15]]

print("Original Array",a)
print("Taking Indices",np.take(a,[0,4]))
print("\nTaking Indices\n",np.take(a,[0,4],axis=1))