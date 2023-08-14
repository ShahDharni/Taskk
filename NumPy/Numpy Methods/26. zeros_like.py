import numpy as np

d=np.arange(10).reshape(2,5)
print("original array :\n",d)

d1=np.zeros_like(d,dtype=float)
print("zeros like : \n",d1)

d2=np.arange(8)
dh=np.zeros_like(d2,dtype=float)
print("dh :\n",dh)
