# numpy.absolute(arr, out = None, ufunc ‘absolute’) : This mathematical function helps user to calculate absolute value of each element. 
# For complex input, a + ib, the absolute value is  \sqrt { a^2 + b^2 }.

import numpy as np
d= [1,-2,-500,100]
print("Absolute :\n", np.absolute(d))

## Another Example 
# For complex number  \sqrt {a^2 + b^2}.
d1=[1+2j]         
print("Absolute :\n", np.absolute(d1))

d2=[16j+5]
print("Absolute :\n", np.absolute(d2))

d3=[1j+2j]         
print("Absolute :\n", np.absolute(d3))
