# In an array of +ve integers, the numpy.bincount() method counts the occurrence of each element.
# Each bin value is the occurrence of its index. One can also set the bin size accordingly.

import numpy as np
d=[1,2,3,2,2,2,2,2,2,3,4,4,2,1,2]
print(np.bincount(d))

d1=[3,3,3,3,3,1,2,3,2,0,6,1]
print(np.bincount(d1))
