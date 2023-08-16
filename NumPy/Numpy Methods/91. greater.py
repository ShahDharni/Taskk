
import numpy as np
  
d  = np.greater([1., 2.], [1., 3.])
print("Check to be greater : \n", d, "\n")
  
d1 = np.greater([1, 2], [[1, 3],[1, 4]])
print("Check to be greater : \n", d1, "\n")

d=[[2,3]]
d1=[[8,1]]
print(np.greater(d,d1))