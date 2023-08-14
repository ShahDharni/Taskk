import numpy as np

# Syntax: numpy.all(array,axis = None,out = None,  keepdims = class numpy._globals._NoValue at 0x40ba726c)                 



# Python Program illustrating
# numpy.all() method

import numpy as np


print("Bool Value with axis = NONE : ",
	np.all([[True,False],[True,True]]))

print("\nBool Value with axis = 0 : ",
	np.all([[True,False],[True,True]], axis = 0))

print("\nBool : ", np.all([-1, 4, 5]))
print("\nBool : ", np.all([1.0, np.nan]))

print("\nBool Value : ", np.all([[0, 0],[0, 0]]))
