import numpy as np

d = np.matrix([[1, 21, 30], 
                 [63 ,434, 3], 
                 [54, 54, 56]])
print("Original elements \n",np.triu(d))
print("Original elements \n",np.triu(d,1))
print("Original elements \n",np.triu(d,-1))

