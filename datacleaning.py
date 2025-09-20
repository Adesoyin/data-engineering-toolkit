import pandas as pd
import numpy as np
import datetime as dt

url = 'https://raw.githubusercontent.com/Oyeniran20/axia_class_cohort_7/refs/heads/main/Dataset%20.csv'
data = pd.read_csv(url)
data.head()

#Data cleaning
data.info()
# To check count of missing values in each column
missing_value = data.isna().sum().sort_values(ascending = False)
# To get the % of the missing values for the columns in the dataset.
missing_pct = (data.isna().sum().sort_values(ascending = False)/ len(data)) *100

missing_df = pd.DataFrame ({'Missing Values': missing_value,'Missing Pct': missing_pct})
print(missing_df)

