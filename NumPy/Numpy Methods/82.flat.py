# The numpy.ndarray.flat() function is used as a 1_D iterator over N-dimensional arrays. 
# It is not a subclass of, Python’s built-in iterator object, otherwise it a numpy.flatiter instance

import numpy as np
d=np.arange(15).reshape(3,5)
print(d)
print()

print(d.flat[0:3])
print()

print(d.flat[1:15])