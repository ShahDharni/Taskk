import numpy as np
import math
 
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)
 
tanh_values = np.tanh(in_array)
print ("\ntanh_values  : \n", tanh_values)