import numpy as np

print("tri with k=1  \n",np.tri(2,3,1,dtype=float))
print()
print("tri with main diagonal \n",np.tri(3,5,0))
print()
print("tri with k=-1 \n",np.tri(3,5,-1))

