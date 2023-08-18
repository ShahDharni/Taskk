import pandas as pd
import numpy as np

d=pd.read_csv("dete_survey.csv")
print(d)

d1=pd.read_csv("tafe_survey.csv")
print(d1.head(5))


## Info
d.info()
d1.info()

## Identify missing values and remove unnecessary columns 

## Some columns are unnecessary and not useful for our analysis 
dete_survey_updated=d.drop(d.columns[28:46],axis=1)
tafe_survey_updated=d1.drop(d1.columns[17:66],axis=1)

## These are updated columns
print(dete_survey_updated.columns)
print(tafe_survey_updated.columns)


## Rename the columns
dete_survey_updated.columns=dete_survey_updated.columns.str.lower().str.strip().str.replace("_","")
print(dete_survey_updated.columns)

tafe_survey_updated = tafe_survey_updated.rename(columns={'Record ID': 'id', 
                                   'CESSATION YEAR': 'cease_date', 
                                   'Reason for ceasing employment': 'separationtype', 
                                   'Gender. What is your Gender?': 'gender', 
                                   'CurrentAge. Current Age': 'age',
                                   'Employment Type. Employment Type': 'employment_status', 
                                   'Classification. Classification': 'position', 
                                   'LengthofServiceOverall. Overall Length of Service at Institute (in years)': 'institute_service'})
print(tafe_survey_updated)



## Filter the data

## Here we will analyze survey respondents who have resigned so we will only select separation type containing the string resignation
print(dete_survey_updated['separationtype'].value_counts())
print()
print(tafe_survey_updated['separationtype'].value_counts())
print()
dete_survey_updated['separationtype']=dete_survey_updated['separationtype'].str.split("-").str[0]
print(dete_survey_updated['separationtype'].value_counts())


## Select only resignation separation types from each dataframe
dete_resignations=dete_survey_updated[dete_survey_updated['separationtype']=='Resignation'].copy()
print(dete_resignations)

tefe_resignations=tafe_survey_updated[tafe_survey_updated['separationtype']=='Resignation'].copy()
print(tefe_resignations)


# ## Verify the data
print(dete_resignations['cease date'].value_counts())
print()
print(tefe_resignations['cease_date'].value_counts())




## Check the unique values and look for outliers
print(dete_resignations['dete start date'].value_counts().sort_index())
print()
print(dete_resignations['cease date'].value_counts())


# ## Creating a new column
# dete_resignations['institute_service']=dete_resignations['cease date'] - dete_resignations['dete start date']
# dete_resignations['institute_service']



## Identify dissatisified employee

# verify the unique values
print(tefe_resignations['Contributing Factors. Dissatisfaction'].value_counts())

# verify the unique values
print(tefe_resignations['Contributing Factors. Job Dissatisfaction'].value_counts())

# print(dete_resignations['Job dissatisfaction'].value_counts())


# Update the values in the contributing factors columns to be either True, False, or NaN

def update_value(value):
    if pd.isnull(value):
        return np.nan
    elif value=="-":
        return False
    else:
        return True


tefe_resignations['dissatisfied']=tefe_resignations[['Contributing Factors. Dissatisfaction','Contributing Factors. Job Dissatisfaction']].applymap(update_value).any(1,skipna=False)
tefe_resignations_up=tefe_resignations.copy()
print(tefe_resignations_up['dissatisfied'].value_counts(dropna = False))


dete_resignations['dissatisfied'] = dete_resignations[['cease date', 'DETE Start Date', 'physical_work_environment', 'lack_of_recognition', 'lack_of_job_security', 'work_location', 'employment_conditions', 'work_life_balance', 'workload']].any(1, skipna=False)
dete_resignations_up = dete_resignations.copy()

# Check the unique values after the updates
dete_resignations_up['dissatisfied'].value_counts()



## Combine the data 
print(tefe_resignations_up['Institute']=="TEFE")




























