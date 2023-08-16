import numpy as np
  
d  = np.less_equal([1., 2.], [1., 3.])
print("Check to be less_equal : \n", d, "\n")
  
d1 = np.less_equal([1, 2], [[1, 3],[1, 4]])
print("Check to be less_equal : \n", d1, "\n")

d=[[2,3]]
d1=[[8,1]]
print(np.less_equal(d,d1))