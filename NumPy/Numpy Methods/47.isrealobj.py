import numpy as np

d=[2,3,8]
print("Original Array :\n",d)
d1=np.isrealobj(d)
print("isrealobject :",d1)


# If it contains any complex number then it will return False

d2=[2,3,8j]  ## As here 8j is a complex number it will return False
print("Original Array :\n",d2)
d3=np.isrealobj(d2)
print("isrealobject :",d3)

