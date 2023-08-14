import numpy as np
d=np.arange(10,dtype=int).reshape(2,5)
print("original array : \n",d)
print()
print("after full like : \n",np.full_like(d,10.0))



d1=np.arange(10,dtype=float).reshape(2,5)
print("original array : \n",d1)
print()
print("after full like : \n",np.full_like(d1,0.01))
