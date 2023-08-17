

import numpy as np
a = np.arctan2([0., 0., np.inf], [+0., -0., np.inf])
b = np.arctan2([1., -1.], [0., 0.])
print ("a : ", a)
print ("b : ", b)
