# This mathematical function helps user to calculate hypotenuse for the right angled triangle, given its side and perpendicular. 
# Result is equivalent to Equivalent to sqrt(x1**2 + x2**2), element-wise.


import numpy as np
d=np.array([12,3,4,6])   ## 12**2 =144, 3**2= 9,  6**2=36
d1=np.array([5,4,3,8])   ## 5**2 = 25,  4**2= 16, 8**2=64
output=np.hypot(d,d1)    ## total =169  total=25  total=100
print("Output :\n",output) ## 169 is 13 square, 25 is 5 square, 100 is 10 square
                           ## [13.,5.,5.,10.]
