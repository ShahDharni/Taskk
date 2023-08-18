import pandas as pd
import numpy as np

# 1. How do you filter out rows which contain the same integer as the row immediately above?
# You should be left with a column containing the following values:
# 1, 2, 3, 4, 5, 6, 7

d = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
print(d)

print(d.loc[d['A'].shift() != d['A']])
print(d.drop_duplicates(subset='A'))



# 2. df = pd.DataFrame(np.random.random(size=(5, 3))) # this is a 5x3 DataFrame of float values
# how do you subtract the row mean from each element in the row?

d1=pd.DataFrame(np.random.random(size=(5,3)))
print("d1",d1)
print(d.sub(d.mean(axis=1),axis=0))


# 3. df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
# Which column of numbers has the smallest sum? Return that column's label.

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
print("DataFrame :\n",df)
print(df.sum().idxmin())