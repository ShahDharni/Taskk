import numpy as np
arr=np.array([[1,2,3,4,5],
      [6,7,8,9,10],
      [11,12,13,14,15],
      [16,17,18,19,20]])

print(arr)
print()
print([1,2,3,4,5] in arr.tolist())
print([16,17,18,19,21] in arr.tolist())
print([4,2,1,5,6,7] in arr.tolist())
print([6,7,8,9,10] in arr.tolist())