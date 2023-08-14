import numpy as np

d = np.matrix([[1, 21, 30], 
                 [63 ,434, 3], 
                 [54, 54, 56]])
print("Original elements \n",np.tril(d))
print()
print("Original elements \n",np.tril(d,1))
print()
print("Original elements \n",np.tril(d,-1))

