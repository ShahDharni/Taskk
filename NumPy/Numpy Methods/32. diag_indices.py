import numpy as np
d=np.diag_indices(8)
print("Indices of diagonal elements as tuple : ")
print(d, "\n")

print()

array=np.arange(16).reshape(4,4)
print("Initial Array :\n",array)

print()
d=np.diag_indices(4)
array[d]=25
print("New Array :\n",array)