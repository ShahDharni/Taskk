import pandas as pd
df=pd.read_csv('StudentsPerformance.csv')
df

json_data = df.to_dict(orient="records")
json_data