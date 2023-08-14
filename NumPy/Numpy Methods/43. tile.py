import numpy as np

arr = np.arange(5)
print("arr : \n", arr)

repetitions = 2
print("Repeating arr 2 times : \n", np.tile(arr, repetitions))

repetitions = 3
print("\nRepeating arr 3 times : \n", np.tile(arr, repetitions))

