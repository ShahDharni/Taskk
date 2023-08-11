import numpy as np
num1_d=np.arange(7)
print(num1_d)

print()
num2_d=np.arange(21).reshape(3,7)
print(num2_d)



## nditer is used to traverse an array

for a,b in np.nditer([num1_d,num2_d]):
    print("%d:%d" % (a,b),)