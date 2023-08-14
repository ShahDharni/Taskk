import numpy as np

d=np.arange(12).reshape(3,4)
print("d :",d)

print()

## Shifting 1 place 
print("Shifting one place :\n",np.roll(d,1))

print()
## Shifting 5 place 
print("Shifting one place :\n",np.roll(d,5))

print()
## Shifting 5 place with 0th axis
print("Shifting one place with 0th axis :\n",np.roll(d,5,axis=0))