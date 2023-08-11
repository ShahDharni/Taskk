import numpy as np
 

arr=np.array([[1,2,3,3,3],
                [3,3,3,2,4],
                [2,2,3,3,2],
                [3,3,5,6,3]])

print(arr)
print()
output=repr(arr).count("3")
print("Number of occurrences :",output)