import numpy as np
a = np.array_equiv([1, 2], [[1, 2, 1, 2], [1, 2, 1, 2]])
  
b = np.array_equiv([1, 2], [[1, 2], [1, 2]])
  
print ("\n\na : ", a)
print ("\nb : ", b)

## Difference between array_equal and array_equivalent :-
# Both methods array_equal(~) and array_equiv(~) are similar in that they both return a single Boolean when all the elements in the given arrays are equal pair-wise.

# The key difference is that array_equal returns True when the shape of the arrays exactly match,
#  whereas array_equiv will also return True if the one array can be broadcasted to take on the same shape. 


# for example
d=np.array_equiv([1,2], [[1,2],[1,2]])   # True
d1=np.array_equal([1,2], [[1,2],[1,2]])   # False
print(d)
print(d1)