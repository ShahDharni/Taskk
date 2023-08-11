## How to remove non numeric rows from array

import numpy as np
n_arr = np.array([[10.5, 22.5, 3.8],
                  [41, np.nan, np.nan]])
  

print(n_arr[~np.isnan(n_arr).any(axis=1)])