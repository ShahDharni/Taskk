# Syntax: numpy.put(array, indices, p_array, mode = 'raise')

# array   : array_like, target array
# indices : index of the values to be fetched
# p_array : array_like, values to be placed in target array
# mode    : [{‘raise’, ‘wrap’, ‘clip’}, optional] mentions how out-of-bound indices will behave
#                   raise : [default]raise an error 
#                   wrap  : wrap around
#                   clip  : clip to the range




import numpy as np
 
a = np.arange(5)
np.put(a, 22, -5, mode='clip')   # we can also use wrap in mode 
print("After put : \n", a)

