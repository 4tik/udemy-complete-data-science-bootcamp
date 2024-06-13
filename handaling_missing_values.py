# Handling Missing Values
# Missing value/data is define as the values/datas that is not stored/present in given data set

import pandas as pd

data_set = pd.read_csv("placement_data_full_class.csv")
# print(data_set)
# print(data_set.isnull().sum())
print(data_set['salary'].mode()[0])
data_set['salary'] = data_set['salary'].fillna(data_set['salary'].mode()[0])
print(data_set['salary'])