import numpy as np

d=np.arange(12).reshape(3,4)
print("d :\n",d)

d1=np.place(d,d>5,[15,25,35])
print("d1 :\n",d)