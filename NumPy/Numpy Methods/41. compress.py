import numpy as np
d=np.arange(12).reshape(3,4)
print("d :\n",d)

d1=np.compress([0,1],d,axis=0)
print("d1 :\n",d1)

d2=np.compress([0,1],d,axis=1)
print("d2 :\n",d2)

d3=np.compress([False,True],d,axis=1)
print("d3 :\n",d3)