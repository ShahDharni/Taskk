# The numpy.rint() is a mathematical function that rounds elements of the array to the nearest integer.

import numpy as np
  
d = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", d)
print ("Input array : \n", np.rint(d))


d1 = [.5538, 1.33354, .71445]
print ("\nInput array : \n", d1)
  
rintoff_values = np.rint(d1)
print ("\nRounded values : \n", rintoff_values)