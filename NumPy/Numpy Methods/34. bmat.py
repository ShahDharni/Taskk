import numpy as np
  
A = np.mat('4 1; 22 1')
B = np.mat('5 2; 5 2')
C = np.mat('8 4; 6 6')

# array like bmat
d=np.bmat([[A,B],[C,A]])

print("Array like bmat :\n",d)

d1=np.bmat('A,B;A,A')
print("string like bmat :\n",d1)
