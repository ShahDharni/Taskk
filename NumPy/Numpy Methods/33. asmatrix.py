import numpy as np
d=np.matrix([[4,5,6],[5,7]])
print("d :",d)

print()
d1=np.asmatrix(d)
d[0,1]=10
print("asmatrix :",d1)