import pandas as pd
#A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.

# Dictonary to pandas dataframe
# Dictionary to dataframe
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data)
# print(df)
# singleRecord = df.loc[1]  # Returns a pandas series
# print(singleRecord)

# use a list of indexes:
# print(df.loc[[0, 1]])


# With the index argument, you can name your own indexes.
# df = pd.DataFrame(data, index=['Day1', 'Day2', 'Day3'])
# print(df)
# print(df.loc['Day3'])


# Load a comma separated file (CSV file) into a DataFrame:
df = pd.read_csv('data.csv')
# print(df.ndim)
# print(df.shape)
# print(df.to_string())  # use to_string() to print the entire DataFrame.

print(df)


# Read json
# df = pd.read_json('data.json')