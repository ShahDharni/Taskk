# numpy.npv(rate, value) : This financial function helps user to calculate the NPV(Net Present Value) of a cash flow series.

import numpy as np

# #		 rate		 values	
a = np.npv(0.281,[-100, 19, 49, 58, 200])
print("Net Present Value(npv) : ", a)


# This method was removed from numpy version 1.20