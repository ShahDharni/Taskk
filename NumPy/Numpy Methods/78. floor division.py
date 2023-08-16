# numpy.floor_divide(arr1, arr2, /, out = None, where = True, casting = ‘same_kind’, order = ‘K’, dtype = None) : Array element from first array is divided by the elements from second array(all happens element-wise). 
# Both arr1 and arr2 must have same shape.
#  It is equivalent to the Python // operator and pairs with the Python % (remainder), function so that b = a % b + b * (a // b) up to roundoff. 

import numpy as np
d=[22,33,21,23,12]
d1=[11,2,3,23,3]
print(np.floor_divide(d,d1))