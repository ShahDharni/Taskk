import numpy as np
#                 rate        np       pmt   fv
Solution = np.pv(0.05/12, 10*12, -100, 15692.93)
  
print("present value (fv) : ", Solution)


# This method was removed from numpy version 1.20