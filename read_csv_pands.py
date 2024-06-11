# read CSV file using pands
import pandas as pd

get_data = pd.read_csv('airport.csv')

# print(get_data)

# getting a quick overview of DataFrame using head() method
# head() method returns headers and number of row 

print(get_data.head())

print('==============================================================')
print(get_data.head(10)) # top 10 row of data
print(get_data.tail(10)) # last 10 row of data
print(get_data.info()) # get info about data set datatype

# describe() method work for numerical data

print(get_data.describe())