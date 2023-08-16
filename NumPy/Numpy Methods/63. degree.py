# The numpy.degrees() is a mathematical function that helps user to convert angles from radians to degrees.

import numpy as np
import math
d=[0,math.pi/2,np.pi/3,np.pi] ## here math.pi and np.pi both are same values of both are 3.14
# [0,  3.14/2  , 3.14/3  , 3.14]
# [0, 1.5707963267948966, 1.0471975511965976, 3.141592653589793]
print("pi :\n",d)

# [0, 1.5707963267948966 * 57.2958 = 90, 1.0471975511965976 * 57.2958 = 60, 3.141592653589793 * 57.2958 = 180]
print("degree :\n",np.degrees(d))   

## here 1 radians = 57.2958 degree
