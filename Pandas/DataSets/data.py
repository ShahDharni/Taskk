## Pandas Data Cleaning

import pandas as pd
df=pd.read_csv('data.csv')
print(df)

print()

## Replace Empty values

df=df.fillna(140)
print(df)

print()

## Using Pandas Replace method
df=df.replace(450,45)
print(df)


## Replace only for specified users
df=pd.read_csv('data.csv')
new_df=df['Calories'].fillna(130)
print(new_df)


## dropna()

# By default, the dropna() method returns a new DataFrame, and will not change the original

# If you want to change the original DataFrame, use the inplace = True argument

# The dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame

df=pd.read_csv('data.csv')
new_df=df['Calories'].dropna()
print(new_df)


## mean
df=pd.read_csv('data.csv')
new_df1=df['Calories'].mean()
df['Calories'].fillna(new_df1)
print("mean",new_df1)


## median
df=pd.read_csv('data.csv')
new_df1=df['Calories'].median()
df['Calories'].fillna(new_df1)
print("median",new_df1)



## mode
df=pd.read_csv('data.csv')
new_df1=df['Calories'].mode()[0]
df['Calories'].fillna(new_df1)
print("median",new_df1)




## Pandas Cleaning data of wrong format

## Convert into correct format
df=pd.read_csv('data.csv')
print(df['Date'])


# Pandas has a to_datetime() method for Converting Date to right Format
df=pd.read_csv('data.csv')
df['Date']=pd.to_datetime(df['Date'])
print(df['Date'])

print()


## Pandas- Fixing Wrong Data
df=pd.read_csv('data.csv')
print(df['Duration'])

print()

## Replacing values
df.loc[7,'Duration']=45
print(df['Duration'])


df=pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x,"Duration"]>60:
        df.loc[x,"Duration"]=60

df['Duration']


## Removing Duplicates

# Duplicate rows are rows that have been registered more than one time
# To discover duplicates, we can use the duplicated() method
# The duplicated() method returns a Boolean values for each row

df=pd.read_csv('data.csv')
print(df.duplicated())


## Removing Duplicates

df=pd.read_csv('data.csv')
print(df.drop_duplicates())
print(df)


# Pandas - Data Correlations:-

# Finding Relationships:-
# The corr() method calculates the relationship between each column in your data set
# The corr() method ignores "not numeric" columns
# The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns
# The number varies from -1 to 1
# 1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well

# Perfect Correlation:-
# We can see that "Duration" and "Duration" got the number 1.000000, which makes sense, each column always has a perfect relationship with itself

# Good Correlation:-
# "Duration" and "Calories" got a 0.922721 correlation, which is a very good correlation, and we can predict that the longer you work out, the more calories you burn, and the other way around: if you burned a lot of calories, you probably had a long work out

# Bad Correlation:-
# "Duration" and "Maxpulse" got a 0.009403 correlation, which is a very bad correlation, meaning that we can not predict the max pulse by just looking at the duration of the work out, and vice versa

print()
print(df.corr())

print()

## loc and iloc function

## Index based Selection
print(df.iloc[0])


## Index Selection Using List
print(df.iloc[[1,3,5],1])


## Label-based selection
print(df.loc[0,"Calories"])


## Label-based selection with conditions
print(df.loc[df.Duration==60])


## Label-based selection with multiple conditions using and
print(df.loc[(df.Pulse==110) & (df.Duration==60)])



## Label-based selection with multiple conditions using or
print(df.loc[(df.Pulse==110)  | (df.Duration==60)])

## isnull Built in conditional Selector

# isnull() methods let you highlight values which are (or are not) empty (NaN)
print(df.loc[df.Calories.notnull()])


## isin Built in conditinal Selector
# isin() lets you select data whose value "is in" a list of values


print(df.loc[df.Pulse.isin([100,92])])


# isnull() Conditional Selector
# To select NaN entries you can use pd.isnull()

print(df[pd.isnull(df.Calories)])


print()
## Summary Functions
df=pd.read_csv('data.csv')
print(df.Pulse.describe())
print()

print(df.Pulse.unique())
print()

print(df.Pulse.value_counts())


## Renaming 
print(df.rename(columns={"Duration":"Time"}))

## Sorting
print(df.sort_values(by='Duration'))

## Sorting as per ascending order
print(df.sort_values(by='Duration',ascending=True))

## Sorting as per descending order
print(df.sort_values(by='Duration',ascending=False))

# To sort by index value we can also use sort_index
print(df.sort_index())



## Grouping
# count() and len Function both gives the same result but count() gives the output as Series and len gives the output as Data Frame

df=pd.read_csv('data.csv')
print(df.groupby("Duration").Duration.count())

print(type(df.groupby("Duration").Duration.count()))

print(df.groupby(['Duration']).agg([len]))

print(type(df.groupby(['Duration']).agg([len])))

print(df.groupby("Duration").Pulse.min())