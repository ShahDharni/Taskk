import numpy as np 
  
gfg = np.array((0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0))
  
res = np.trim_zeros(gfg)
print(res)