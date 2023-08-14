import numpy as np
array=np.arange(8).reshape(2,2,2)

print("\n Original array \n:",array)
d=np.flip(array,axis=0)
print("Flipped Array \n",d)