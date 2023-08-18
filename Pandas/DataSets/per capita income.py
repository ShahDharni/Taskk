import pandas as pd

d=pd.read_csv("canada_per_capita_income.csv")
d

## Chnaging the index column
d=pd.read_csv("canada_per_capita_income.csv",index_col="year")
print(d)

## Manipulating the index
d=pd.read_csv("canada_per_capita_income.csv")
d.set_index("year")


## Use to_string to print the data
print(d.to_string())

## Conditional selection
print(d.year==1970)

## max_rows
print(pd.options.display.max_rows)

print()

## Increase the maximum number of rows to print the entire data
pd.options.display.max_rows = 999
print(pd.options.display.max_rows)



## min_rows
print(pd.options.display.min_rows)

print()

## Increase the maximum number of rows to print the entire data
pd.options.display.min_rows = 50
print(pd.options.display.min_rows)


## Viewing the data
d1=pd.read_csv('canada_per_capita_income.csv')
print(d1.head(5))
print()
print(d1.tail(10))


## Info
print(d1.info())