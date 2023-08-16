# numpy.expm1(array, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) :
# This mathematical function helps user to calculate exponential of all the elements subtracting 1 from all the input array elements.


import numpy as np
d=[6,5,4]
print("original array :\n", d)
print()

d1=np.exp(d)
print("Exp :\n",d1)

print()
d2=np.expm1(d)
print("Expm1 :\n",d2)
