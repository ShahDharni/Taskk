import numpy as np
d= np.arange(10).reshape(5,2)
print("Array :\n",np.iscomplex(d))

# d1= np.arange(30).reshape(6,5).dtype=complex
# print("Array :\n",np.iscomplex(d1))
print()
d1=[[1j+0],
    [3]]
print("Iscomplex Array :\n",np.iscomplex(d1))

print()
## Another Example
d2=[[1+0j], ## Here Complex number is with 0 so it will return False
    [1j+0]]

print("Is Complex Array :\n",np.iscomplex(d2))