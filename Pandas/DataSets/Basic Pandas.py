import pandas as pd

## Checking Pandas version
print(pd.__version__)


## Working on one dimensional array :- Pandas Series
d=[3,4,5,6,7,8,9,10]
d1=pd.Series(d)
print(d1)
print()

print(d[0])

print()

## Creating labels
d=[3,4,5,6,7,8,9,10]
d1=pd.Series(d,index=["A","B","C","D","E","F","G","H"])
print(d1)

## Creating labels using name attribute
d=[3,4,5,6,7,8,9,10]
d1=pd.Series(d,index=["A","B","C","D","E","F","G","H"],name="Multiples of 3")
print(d1)


## If you have labels access an item with labels
print(d1["D"])

print()

## Key value pairs as a series
d2={"day1":340,"day2":670,"day3":456,"day4":98}
print(pd.Series(d2))

print()

## Access items by using keys
print(d2['day1'])


## DataFrame
d3={'calories':[345,456,678,342],
    'duration':[45,67,89,23]}
d4=pd.DataFrame(d3)
print(d4)


## Index 
print(d4.index)


## Locate row
print(d4.loc[0])

## Access Multiple Rows
print(d4.loc[[0,1]])


## Name Indexes
d3={'calories':[345,456,678,342],
    'duration':[45,67,89,23]}
d4=pd.DataFrame(d3,index=['day1','day2','day3','day4'])
print(d4) 

print()

## Located Name Indexes
print(d4.loc['day1'])