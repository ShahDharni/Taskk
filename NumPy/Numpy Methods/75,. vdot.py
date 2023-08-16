# numpy.vdot(vector_a, vector_b) returns the dot product of vectors a and b.
#  If first argument is complex the complex conjugate of the first argument(this is where vdot() differs working of dot() method) is used for the calculation of the dot product.
# It can handle multi-dimensional arrays but working on it as a flattened array.


import numpy as np
d=np.array([[1,2],[5,6]])
d1=np.array([[3,4],[2,4]])
d2=np.vdot(d,d1)
print("vdot :\n",d2)


