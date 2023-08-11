## Squeeze :- Squeeze is used to remove single dimension entries from the shape of an array.

import numpy as np
in_arr=np.array([[[2,2,2],[2,2,2]]])
print("Input :",in_arr)
print("Shape of the input :",in_arr.shape)

out_arr=np.squeeze(in_arr)
print("Output Array :",out_arr)
print("Shape of the input :",out_arr.shape)
