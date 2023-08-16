# numpy.dot(vector_a, vector_b, out = None) returns the dot product of vectors a and b.
# It can handle 2D arrays but considers them as matrix and will perform matrix multiplication. 
# For N dimensions it is a sum-product over the last axis of a and the second-to-last of b :


import numpy as np
d=np.array([[1,2],[5,6]])
d1=np.array([[3,4],[2,4]])
d2=np.dot(d,d1)
print("dot :\n",d2)




