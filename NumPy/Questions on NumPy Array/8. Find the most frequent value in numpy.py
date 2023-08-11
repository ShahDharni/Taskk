import numpy as np

a=np.array([2,3,4,5,6,7,2,8,9,9,8,8,9])
print("Original array",a)

print(np.bincount(a).argmax())







## If there are more than one most repeated value

x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3, ])
print("original array :",x)

y=np.bincount(x)
maximum=max(y)

for i in range(len(y)):
    if y[i]==maximum:
        print(i,end=" ")