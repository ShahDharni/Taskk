# The numpy.radians() is a mathematical function that helps user to convert angles from degree to radians.
## here 1 radians = 57.2958 degree

import numpy as np
d=np.arange(10) * 90
print("d :\n",d)
#  [  0  90 180 270 360 450 540 630 720 810]
print("Radians :\n",np.radians(d))
#  [  0 , 90/57.2958 , 180/57.2958 , 270/57.2958 , 360/57.2958 , 450/57.2958 , 540/57.2958 , 630/57.2958 , 720/57.2958 , 810/57.2958]
# [ 0. , 1.57079633 , 3.14159265 , 4.71238898 , 6.28318531 , 7.85398163 , 9.42477796 , 10.99557429 , 12.56637061 , 14.13716694]