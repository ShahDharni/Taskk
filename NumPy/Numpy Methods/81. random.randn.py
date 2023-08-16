# The numpy.random.randn() function creates an array of specified shape and fills it with random values as per standard normal distribution. 
# If positive arguments are provided, randn generates an array of shape (d0, d1, …, dn), filled with random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1 (if any of the d_i are floats, they are first converted to integers by truncation). 
# A single float randomly sampled from the distribution is returned if no argument is provided.


import numpy as np
d=np.random.randn(8)
print(d)
print()

d1=np.random.randn(2,3)
print(d1)
print()

d2=np.random.randn(2,2,2)
print(d2)