## Pandas Series is a one dimensional array capable of holding any type of data(float,integer,boolean,string, python objects ). 
# The axis labells collectively called as indexes. 
# The column in excel sheet is known as pandas series. 
# The labels need not be unique but its of hashable type.

import pandas as pd
import numpy as np

d=np.array(['g','e','e','k','s'])
print("d : \n",d)

d1=pd.Series(d,index=[1,2,3,4,5])
print("Series :\n",d1)