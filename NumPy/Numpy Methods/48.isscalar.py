# numpy.isscalar(num) : This is a logical function that returns true if the type of input num is scalar.
# True, if input is scalar; else False

import numpy as np
d=[2,3,4,5,6,8]
print("Original Array :\n",d)

print()
print("Scalar Value :\n", np.isscalar(d))
print()
print("Scalar Value :\n", np.isscalar(600))
print()
print("Scalar Value :\n", np.isscalar({-7000}))
print()
print("Scalar Value :\n", np.isscalar([600]))