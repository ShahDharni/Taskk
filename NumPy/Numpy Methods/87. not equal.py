import numpy as np
  
d  = np.not_equal([1., 2.], [1., 3.])
print("Check to be not Equal : \n", d, "\n")
  
d1 = np.not_equal([1, 2], [[1, 3],[1, 4]])
print("Check to be not Equal : \n", d1, "\n")