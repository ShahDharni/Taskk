# Python program explaining fv() function

import numpy as np
#				 rate	 np	 pmt pv
Solution = np.fv(0.05/12, 10*12, -100, -100)

print("Solution : ", Solution)

# This method was removed from numpy version 1.20