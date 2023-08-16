import numpy as np

d=np.array([[1,2,3,4,5],[6,7,8,9,10]],order='C')
print("Fortran :",np.isfortran(d))

print()
d1=np.array([[1,2,3,4,5],[6,7,8,9,10]],order='F')
print("Fortran :",np.isfortran(d1))

print()
d2=np.array([[1,2,3,4,5],[6,7,8,9,10]],order='A')
print("Fortran :",np.isfortran(d2))