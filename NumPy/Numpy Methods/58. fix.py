# The numpy.fix() is a mathematical function that rounds elements of the array to the nearest integer towards zero. The rounded values are returned as floats.

import numpy as np
d=np.array([1.5,2.5,3.5,4.5,5.5])
print("d",np.fix(d))

d1=np.array([0.1,0.2,0.9,0.4,0.5])
print("d1",np.fix(d1))

d2= [.53, 1.54, .71]
print("d2",np.fix(d2))
