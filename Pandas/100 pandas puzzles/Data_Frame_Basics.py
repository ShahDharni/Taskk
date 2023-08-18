import pandas as pd
print(pd.__version__)
print(pd.show_versions)

import numpy as np
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels=['a','b','c','d','e','f','g','h','i','j']

df=pd.DataFrame(data,index=labels)
print(df)


print(df.info())
print()
print(df.describe())
print()
print(df.iloc[:3])
print()
print(df.head(3))
print()
print(df.loc[:,['animal','age']])

##or
print(df[['animal','age']])

print(df.loc[df.index[[3,4,8]],['animal','age']])