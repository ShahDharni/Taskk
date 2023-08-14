import numpy as np

d = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print("Original Array : ",d)

round_off=np.around(d)
print("Round off d :",round_off )

print()
d1 = [.5538, 1.33354, .71445]
round_off=np.around(d1)
print("Round off d1 :",round_off )